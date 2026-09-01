---
name: qaip-cli
description: qaip CLI（`qaip api ...`・`qaip schema ...`）を AI エージェントから安全・確実に呼び出すための運用スキル。qaip の REST API / SDK / CLI に触る作業全般で必ず使うこと — completion / search / extract、source-groups や sources のメタデータ操作、crawls・google-drives・githubs・notions・local-file-groups によるデータ取り込み、secrets 管理、agent runs、タグ付けなど。ユーザーが「qaipで検索したい」「qaipに取り込む」「qaipの completion を叩く」「qaip CLI」「qaipのクロール設定」「qaipのソース」「qaipのエージェントラン」といった話題に触れた時点でこのスキルを引くこと。curl を自作したり SDK を Python スクリプト経由で直接叩くより前に、まず qaip CLI（および `qaip schema` による自己記述）を経由する方針で動くこと。
---

# qaip-cli スキル

qaip CLI は AI エージェント向けに設計されている。思い込みで引数を並べず、**CLI 自身が提供する 3 つの仕組み**を毎回使うこと。

1. **`qaip schema [resource]`** — リソースとメソッドの一次情報。必須/任意パラメータ、HTTP メソッド、パスが得られる。
2. **`--dry-run`** — ミューテーションをローカルで組み立てて標準出力に出すだけで、実 API は叩かない。
3. **`--json @file` / `--json -` / `--fields ...`** — 複雑な body はファイルや stdin 経由、レスポンスはフィールド絞り込みで扱う。

これらは「便利機能」ではなく**契約**。以下の運用原則はこの 3 つに依存している。

---

## 呼び出しの骨格

```
qaip [-k API_KEY] [-b BASE_URL] <top-level> ...
```

トップレベルは 2 つだけ。

- `qaip api <resource>.<method> ...` — 実 API 呼び出し。
- `qaip schema [resource]` — API の自己記述（イントロスペクション）。

リソース名のリストは「知っているつもり」にならず、必ず `qaip schema` の出力で確認する。ドキュメントより CLI のスキーマが正。

### CLI の呼び出し方

PyPI からインストールされた環境では **`qaip` コマンドが PATH に入っている**ので、そのまま `qaip api ...` / `qaip schema ...` で良い。ユーザー向け回答・スクリプト例はこの短い形を**既定**にすること。

ソースチェックアウトから未インストールで動かす場合は `uv run qaip ...` で十分。`uv run python -m qaip ...` のような長い呼び出しは冗長で、回答に書くと読み手を混乱させるので避ける。

### 認証

- 既定では環境変数 `QAIP_API_KEY` を読む。
- ベース URL は `QAIP_BASE_URL`、または `-b/--base-url` で上書き。
- CLI 引数に API キーを渡すとシェル履歴に残る。ユーザーに具体的な指示が無い限り **`-k` は使わず、環境変数経由を前提**にすること。新しくキーを発行して渡してきた場合は、そのキーを会話や commit に混ぜないこと（secrets と同じ扱い）。
- **起動時に setup check が走る**。`api_key`（引数 or env）が一切無い状態で `qaip api ...` を叩くと、API コールに到達する前に `missing_credentials` エラーで即終了する（exit code 3）。`qaip schema` と `--dry-run` は資格情報なしでも動くので、未認証時の偵察に使える。

### 出力と終了コード

- 成功時は stdout に **JSON（pretty）**、末尾改行 1 つ。パースして扱う前提で、目視 grep に頼らない。
- 失敗時は stderr にエラー文字列＋終了コード非 0。**`--error-format json`（または `QAIP_ERROR_FORMAT=json`）を付けると、エラーが `{"error":{"code","message","retryable","hint?","http_status?"}}` の構造化 JSON で stderr に出る**。エージェント側で分岐するなら json モードを推奨。
- 終了コード:
  - `0` 成功
  - `1` 一般エラー
  - `2` argparse usage（不明なフラグなど）。**この経路は `--error-format json` の対象外**で、stderr にプレーンテキストの usage が出る。stderr を JSON parse する前に exit code が 2 でないことを確認すること。
  - `3` 認証エラー（`missing_credentials` / API 401, 403）
  - `4` バリデーション（`invalid_id` / `invalid_argument` / `validation_error` / `confirmation_required` / API 400, 422）
  - `5` API エラー（上記以外の 4xx / 5xx）
- 主な error code: `missing_credentials`, `invalid_id`, `invalid_argument`, `validation_error`, `confirmation_required`, `api_error`, `cli_error`, `internal_error`。
- `agent.run` だけは特殊で、durable run を作成して persisted event stream を追跡し、AG-UI event を「1 イベント＝1 行」で stdout に流す（JSON のブロックではない）。

---

## 運用原則（Operating Rules）

### 1. 未知のリソース / メソッドを呼ぶ前に `qaip schema` で検算する

引数を勘で書かない。`qaip schema <resource>` は該当リソースの全メソッドを返す。最低限、`required_params` を満たしていることと、使おうとしているオプショナルパラメータが実在することを確認してから本実行する。

```bash
qaip schema crawls         # crawls の全メソッド + パラメータ
qaip schema                # リソース一覧だけ欲しい時
```

**Why:** CLI と SDK は Stainless で生成されている。思い込みの snake/camel のズレ（`maxDepth` vs `max_depth` 等）や、リソース名のハイフン/アンダースコアの取り違え（`source-groups` と `source_groups`）は実際に起きる。schema 出力は引数名の真実であり、静的ドキュメントより信頼できる。

### 2. ミューテーションは必ず一度 `--dry-run` を通す

`POST` / `PUT` / `DELETE` に該当するメソッド、および作成系（`*.create`・`*.update_*`・`*.delete*`・`*.batch_set_metadata` など）には、まず `--dry-run` を付けて実行し、その出力（`{"method", "path", "body"}` 形式）を確認してから本実行すること。

```bash
qaip api crawls.create --name demo --start-url https://example.com \
  --max-depth 2 --max-num-files 10 --dry-run
# => {"method":"POST","path":"/crawls","body":{...}} を目視/再処理
```

**Why:** 引数名ミスは `--dry-run` で `body` を見ればすぐ気づく。destructive な操作（`*.delete`、`*.delete_metadata`）や上書き系（`*.update_setting`、`*.update_metadata`、`*.batch_set_metadata` など）は、ユーザーの明示同意が無いまま本実行しない。

#### 承認必須コマンド（`--yes` ガード）

以下の **destructive コマンドは CLI 側で `--yes` を要求**する。`--yes` 無しで本実行すると `confirmation_required` エラー（exit code 4）で拒否される。`--dry-run` 時は不要。

| コマンド | 操作 |
| --- | --- |
| `crawls.delete` | クロールを削除 |
| `secrets.delete` | secret を削除 |
| `secrets.update` (`secret` 値を含む body) | secret 値のローテーション。`name` / `description` のみの更新では不要 |
| `githubs.delete` | GitHub 連携を削除 |
| `google-drives.delete` | Google Drive 連携を削除 |
| `notions.delete` | Notion 連携を削除 |
| `local-file-groups.delete` | local file group を削除 |
| `sources.delete_metadata` | source のメタデータを削除 |
| `source-groups.delete_metadata` | source group のメタデータを削除 |
| `tag-source-groups.delete` | タグと source group の関連を削除 |

運用フロー:

1. まず `--dry-run` で `{method, path}` を確認する。
2. ユーザーの明示同意を得てから `--yes` を付けて本実行する。

`*.update_setting` / `*.update_metadata` / `*.batch_set_metadata` は上書きで destructive 寄りだが現状 `--yes` 必須にはしていない。とはいえ既存値を壊しうるので、エージェントは **destructive と同じ扱いで dry-run → 同意 → 本実行** を守ること。

### 3. secret 値は stdin / ファイル経由。dry-run のマスクを信用する

`secrets.create` / `secrets.update` の `secret` フィールドは機微情報。**シェル履歴に生で残さない**。

- 小さな値: `--json -` で stdin から流す。
- JSON で定義済み: `--json @/tmp/foo.json`（使い終わったら削除）。
- dry-run 出力では `secret` フィールドが自動で `"***"` にマスクされる。逆に言えば、dry-run の出力で平文の秘密が見えたらそれはバグなので本実行せずに報告する。

### 4. 複雑な body は `--json` で一括、シンプルなものは named フラグ

**mutating サブコマンド**（`*.create` / `*.update_*` / `*.batch_set_metadata` / `*.cancel_run` など）は `--json <JSON>` と named フラグ（`--messages`, `--tags`, `--query`, `--start-url`, …）の両対応になっている。優先順位は:

- named フラグと `--json` の両方に値がある場合、**`--json` 側が優先**（`if X and X not in body` の順で埋まる）。
- 配列・ネストのあるフィールド（messages、metadata、path_filters など）は named フラグだと手間/誤りが多いので `--json @file` に倒す。

ただし **list / retrieve 系サブコマンド** (`*.list`, `*.retrieve`, `*.retrieve_metadata` など) は `--json` を持たず、named フラグのみ（`--limit`, `--after-id`, `--type` など）。このルールは mutating 側だけに当てはまる。

`--json` は 3 通りの読み取り元を受ける。

| 書き方 | 意味 |
| --- | --- |
| `--json '{"query":"x"}'` | 文字列を直接 JSON としてパース |
| `--json @path/to/body.json` | ファイルを読む |
| `--json -` | stdin を読む |

JSON パースに失敗すると `Invalid JSON for --json`、パースできても object でない（配列・文字列など）と `JSON body must be an object` で即失敗する。

### 5. レスポンスは `--fields <keys>` で絞る

ページネーションや list 系のレスポンスは肥大化しがち。Claude の context を消費しないよう、**欲しいキーが分かっているなら `--fields` で刈り込む**。`--fields` の挙動は実装上 2 通り:

- レスポンス top-level が **dict** のとき → dict 自身のキーを絞り込む。内側の配列要素には入らない。
- レスポンス top-level が **list** のとき → 各要素 dict に適用。

現状の qaip API で top-level が **素の list** を返すエンドポイントは存在せず、全ての list 系は `{<resource>: [...], pagination: {...}}`（例: `sources.list` → `{sources, pagination}`）という **dict**。したがって `--fields id,name` のような要素内キーを書いても全部落ちて `{}` になる。正しくは `--fields sources,pagination`（または `--fields sources` のみ）とし、要素内を覗くのは `jq '.sources[] | {id,name}'` に任せる。

一方 **retrieve 系（単体取得）** はレスポンス top-level 自体が対象リソースの dict なので、`id` / `status` / `name` のような要素内キーを `--fields` で直接絞れる（例: `crawls.retrieve -i <uuid> --fields id,status,name`）。list / retrieve で意味が反転するので混同しない。

### 6. ページネーションは `--after-id` + `--limit`、カーソルは `pagination.next_id`

ほとんどの list メソッドは `after_id`（= 直前ページの `pagination.next_id` を渡す）と `limit` の cursor 方式で、`offset` は使わない。

レスポンスの次ページカーソルは **`pagination.next_id`**（`has_more=false` のとき `null`）。list 要素の末尾 id を勝手にカーソルとして再利用しないこと — 末尾 id とサーバ側の `next_id` は一般に一致しない。

典型ループ:

```bash
after=""
while :; do
  page=$(qaip api sources.list --limit 100 ${after:+--after-id "$after"} \
    --fields sources,pagination)
  echo "$page" | jq -r '.sources[] | [.id, .name] | @tsv'
  after=$(echo "$page" | jq -r '.pagination.next_id // empty')
  [ -z "$after" ] && break
done
```

ただし `agent.list_run_events` **だけ**は例外で、カーソルが UUID でなく整数 event index。フラグ名も `--after <int>` で、`--after-id` ではない（`qaip schema agent` で確認）。レスポンス形も他の list と異なり `{events, next_index, run}` で `pagination` キーは無く、次ページカーソルは `next_index`。

### 7. ID は UUID 形式を渡す

`/contents/{id}` や `/sources/{id}` のような `{id}` 入りエンドポイントは、UUID でない文字列を渡すとサーバ側で 400 になる。`qaip schema` で `required_params` に `id` / `source_id` / `secret_id` / `run_id` が並んでいるものは全て UUID 前提。Claude が生成した ダミー ID（`"abc123"` 等）で叩かないこと。

**CLI 側でも本実行時に UUID 形式を強制している**ので、URL や path traversal を ID に渡すと `invalid_id`（exit code 4）で即拒否される。`--dry-run` 経由では緩和されるので、テンプレ確認時はダミー ID で OK。

**例外:** agent の run/thread ID は durable API が発行する文字列で、UUID 固定ではない。`agent.retrieve_run` / `agent.cancel_run` / `agent.retrieve_run_result` / `agent.list_run_events` / `agent.stream_run_events` などでは path-safe な文字列かだけを CLI で確認し、形式の検証はサーバ側に委ねる。

### 8. ファイルアップロードは順序一致で

`local-file-groups.create` は multipart。`--file` を複数回渡せるが、`--last-modified` をカンマ区切りで明示する場合は **個数と順序が `--file` と一致する必要がある**。単位は **Unix epoch ミリ秒**（秒で渡すと 1000 倍ずれる）。省略すれば CLI が `fstat` から自動で埋めるので、基本は省略推奨。

```bash
qaip api local-file-groups.create --name demo \
  --file a.pdf --file b.md --dry-run
# => last_modified は自動で [mtime_ms_a, mtime_ms_b] になる
```

### 9. agent.run は durable API の簡易フロー、agent.create_run は非同期ハンドル

- `agent.run` — `POST /agent/runs` で run を作成し、続けて `GET /agent/runs/{run_id}/events/stream` を追跡する CLI convenience。AG-UI event を **1 行 1 イベント**で標準出力に流すため、`--fields` は効かず、パース時は各行を個別に扱う。旧 `/agent/run` endpoint は使わない。
- `agent.create_run` → `agent.retrieve_run` / `agent.retrieve_run_result` / `agent.list_run_events` / `agent.cancel_run` — 非同期フロー。実行 ID を取得し、ポーリング or events でフォローアップする。
- どちらに使うか迷ったら **接続を維持できる短いワンショットは `run`、再接続・取消・別プロセスでの追跡が必要なら `create_run`** を既定にする。

### 10. エラーは 2 種類ある

- `Error: <CLI / API 側のメッセージ>` — 引数不足、JSON 不正、API 4xx/5xx など。ユーザーに原因を伝える前に、**schema 出力と照合してパラメータを直す**のが正解。
- Python の traceback（想定外の内部エラー）— これは CLI のバグ。傍観せずリポジトリの Issue 相当として記録する。

---

## よくある落とし穴

- リソース名の **ハイフン** を忘れる: `source-groups`（正） ↔ `source_groups`（間違い）。スキーマ出力の綴りに従う。
- `--citation` や `--html-only` のような **bool フラグ** は「指定すれば True」で、`--citation false` のような値渡しはできない。`false` にしたいなら `--json '{"citation":false}'` を使う。
- `--tags` はカンマ区切りの **タグ名**。`--tag-ids` とは別（後者が必要な場合は `--json` 経由で `tag_ids` を渡す）。
- `extract.create` には **`--schema` / `--prompt` / `--tags` の named フラグが実装されている**。最小構成は `--schema '{...JSON Schema...}'` だけ。schema が大きい / 入れ子が深い場合は `--json @file` に倒す。
- メタデータ系のエンドポイント (`*.update_metadata`, `*.batch_set_metadata`) は named フラグを持たない。必ず `--json` を使う。**body 形は実装と合わせる必要があり**、`metadata` は `{"records": [{"key","val","type"}]}` 形式（`{"k":"v"}` の直書きは通らない）。`batch_set_metadata` の item は `source_group_id`/`source_id` 等の識別子も必須。詳細は `references/recipes.md §8` を参照。
- `secrets.create` の `type` enum は `"google_drive" | "github" | "notion"` の 3 値のみ。`"github_token"` のような紛らわしい綴りは存在せず 422 になる。なお `secrets.update` には `type` フィールド自体が無く、変更したい時は作り直す運用（`src/qaip/types/secret_update_params.py`）。
- `after_id` パラメータのキー名は CLI では `--after-id`（ハイフン、アンダースコア版は存在しない）。**list / retrieve 系には `--json` フラグ自体が無い**ので、「`--json` 経由で `after_id`」という書き方は mutating 系（`create`/`update_*`/`batch_set_metadata` など）に限って有効。**`agent.list_run_events` だけは `--after <int>` で、UUID カーソルではなく整数 event index**。
- list 系の `--fields` に要素内キー（`id,name` 等）を指定すると何もマッチせず `{}` になる。正しくは top-level の `<resource>,pagination` を指定し、要素は `jq` で抜く。

---

## 最初に叩くと幸せになる 3 コマンド

新しいリソース / 環境に入ったら、まずこの 3 つ。

```bash
qaip --version                     # バージョン / CLI が通っているか
qaip schema                        # 使えるリソースの俯瞰
qaip api tags.list                 # 認証が通っているかの軽い疎通
```

本格的なワークフロー（取り込み → 待機 → 検索 → completion、crawls のスケジュール、agent 連携など）は `references/recipes.md` を参照する。

## さらに深掘りする時

- `references/recipes.md` — 典型的なエンドツーエンド手順集（取り込み〜検索〜completion、agent フロー、メタデータバルク更新、ページネーション）。
- `src/qaip/cli/_api/*.py` — 各サブコマンドの実装。named フラグの綴りと型、`--json` とのマージ規則、dry-run 時の path 組み立てが一次情報。
- `src/qaip/cli/_schema.py` — `qaip schema` のデータ源。オフラインでリソース一覧を眺めたい時に。
