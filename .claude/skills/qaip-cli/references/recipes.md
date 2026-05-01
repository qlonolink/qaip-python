# qaip CLI レシピ集

よく使うエンドツーエンド手順のサンプル。コピペで走らせる前に、必ず自分のタスクに合わせて ID・URL・メタデータを置き換え、**ミューテーション系は `--dry-run` を挟む**こと。

**secret を扱うレシピ（§9 など）では `--secret <値>` のような argv 直渡しを使わないこと**。必ず stdin (`--json -`) か `@file` 経由にする（シェル履歴・`ps` からの漏えい対策）。

---

## 0. 共通ヘルパー: secret を安全に対話入力する

§1 と §9 で使い回す。bash / zsh 両対応。`read -rsp` は zsh では `no coprocess` エラーになるので使わない。`stty` 設定を `stty -g` で保存＋`trap` で復元することで、Ctrl-C で中断されても端末エコーが OFF のまま残る事故を防ぐ。

```bash
# qaip_read_silent <変数名> <プロンプト>
# 例: qaip_read_silent SECRET 'GitHub token: '
qaip_read_silent() {
  local _var=$1 _prompt=$2 _stty _rc
  printf '%s' "$_prompt" >&2
  _stty=$(stty -g 2>/dev/null || true)
  trap '[ -n "$_stty" ] && stty "$_stty" 2>/dev/null; trap - EXIT INT TERM' EXIT INT TERM
  stty -echo 2>/dev/null || true
  IFS= read -r "$_var"; _rc=$?
  [ -n "$_stty" ] && stty "$_stty" 2>/dev/null
  trap - EXIT INT TERM
  printf '\n' >&2
  return $_rc
}
```

---

## 1. 疎通 & 認証確認

`QAIP_API_KEY` は事前にシェル rc（`~/.zshrc` 等）や安全なシークレットマネージャ経由で設定済みである前提にする。コマンドラインに `export QAIP_API_KEY=<値>` と直書きしない（履歴に残る）。

一時的にセッションだけ入れたい場合は、上の `qaip_read_silent` ヘルパを使う:

```bash
if [ -z "$QAIP_API_KEY" ]; then
  qaip_read_silent QAIP_API_KEY 'QAIP_API_KEY: ' || { unset QAIP_API_KEY; return 1 2>/dev/null || exit 1; }
  [ -z "$QAIP_API_KEY" ] && { echo "empty key; aborting" >&2; return 1 2>/dev/null || exit 1; }
  export QAIP_API_KEY
fi
# ベース URL を切り替えたい時だけ
# export QAIP_BASE_URL="https://api-staging.example.com"

qaip --version
qaip schema | jq 'keys'            # 使えるリソース一覧
qaip api tags.list | jq '.tags | length'  # 認証が通れば件数が出る
```

401 / 403 が出る場合、まずキーと `QAIP_BASE_URL` の組み合わせを確認する（staging キーで本番 URL を叩く等のミスが多い）。

---

## 2. Web クロールで取り込む

```bash
# 2-1. 設計を dry-run で確認
qaip api crawls.create \
  --name "dev-docs" \
  --start-url https://developer.qaip.com \
  --max-depth 2 --max-num-files 50 \
  --file-extensions .html,.md \
  --dry-run

# 2-2. 納得したら本実行、ID を保持
crawl_id=$(qaip api crawls.create \
  --name "dev-docs" \
  --start-url https://developer.qaip.com \
  --max-depth 2 --max-num-files 50 \
  --file-extensions .html,.md \
  --fields id | jq -r .id)

# 2-3. 状態確認
qaip api crawls.retrieve -i "$crawl_id" --fields id,status
```

特定 URL 群を直接落とすなら `crawls.create_url_list`（再帰クロールではなくリストダウンロード）。

---

## 3. ローカルファイルをアップロード

```bash
qaip api local-file-groups.create \
  --name "spec-2025q2" \
  --file ./docs/spec.pdf \
  --file ./docs/faq.md \
  --dry-run
# last_modified は自動で fstat から埋まる

qaip api local-file-groups.create \
  --name "spec-2025q2" \
  --file ./docs/spec.pdf \
  --file ./docs/faq.md \
  --fields id,name
```

`local-file-groups` には update 系メソッドが実装されておらず、CLI からは `create` / `retrieve` / `list` / `delete` しか呼べない（`qaip schema local-file-groups` で確認可能）。既存グループに追加したい場合は、**同じ name で再度作るのか、別グループに分けるのか**を先に設計する。

---

## 4. タグで取り込み範囲を整える

list 系レスポンスは `{<resource>, pagination}` の dict なので、要素内を覗きたい場合は `--fields <resource>` で絞ったうえで `jq` する。

```bash
# タグ付け対象の source-group を決める
qaip api source-groups.list --limit 20 --fields source_groups \
  | jq '.source_groups[] | {id, name}'

# 既存タグ一覧
qaip api tags.list --fields tags | jq '.tags[] | {id, name}'

# 紐付け（create は重複エラーを握らない。dry-run で想定 body を確認）
# sg / tag は実際の UUID に置換する。<uuid> を裸で書くとシェルが `<` を
# 入力リダイレクトと解釈して構文エラーになるので、必ずダブルクォートで囲むか
# source-groups.list / tags.list から動的に拾う。
sg="00000000-0000-0000-0000-000000000000"   # ← 実際の source_group_id
tag="00000000-0000-0000-0000-000000000000"  # ← 実際の tag_id
# 動的に拾うなら:
# sg=$(qaip api source-groups.list --limit 1 --fields source_groups | jq -r '.source_groups[0].id')
# tag=$(qaip api tags.list --fields tags | jq -r '.tags[0].id')

qaip api tag-source-groups.create \
  --source-group-id "$sg" --tag-id "$tag" --dry-run

# `--json` でも書ける
# qaip api tag-source-groups.create \
#   --json "$(jq -n --arg sg "$sg" --arg tag "$tag" '{source_group_id:$sg, tag_id:$tag}')" --dry-run
```

外すときは `tag-source-groups.delete` に **同じ引数**（`--source-group-id` / `--tag-id`、または同形の `--json`）。削除系は一度 dry-run を通し、ユーザー確認を取ってから本実行する。

---

## 5. 検索して文脈を拾う

`search.create` のレスポンスは `{created, results}` で、top-level に `total` や `has_more` は**無い**。件数が欲しい場合は `jq '.results | length'` を使う。

```bash
qaip api search.create -q "ベクター検索の実装" --limit 5 \
  --fields results

# タグでフィルタ（カンマ区切りタグ名）
qaip api search.create -q "設定" --tags docs,internal --limit 10 \
  --fields results
```

より凝ったフィルタ（`date_from`, `source_types`, `metadata` 等）は `--json` 経由。ただし body の型には癖があるので注意:

- `date_from` / `date_to` は **Unix epoch 秒 (int)**。ISO 文字列 (`"2025-01-01"`) を渡すと 422。
- `source_types` は enum 配列。値は `"crawl" / "local_file" / "google_drive" / "github" / "notion"` の 5 値（`src/qaip/types/shared/source_type.py`）。
- `metadata` は free-form dict ではなく **`MetadataFilterGroup`** の形: `{filters:[{key, operator, type, val?, min?, max?}], groups:[MetadataFilterGroup], logic}`。`operator` は `"eq"/"ne"/"gt"/"gte"/"lt"/"lte"/"between"`、`type` は MetadataType (`"string"/"integer"/"float"/"date"/"datetime"`)。
- `metadata` キー自体は型定義上 "reserved for future use" の注釈付き。ソース単位のメタデータで絞りたい時は `source_metadata` を使う（`src/qaip/types/client_search_params.py`）。

```bash
# UTC の 00:00:00 ちょうどで epoch を計算する。BSD date (-j -f) は FORMAT に
# 含まれない H:M:S を「現在時刻」から埋めてしまうので、日付だけでなく時刻も
# 明示する必要がある。また TZ なしだとローカル時間で解釈されるので TZ=UTC を前置。
date_from_epoch=$(TZ=UTC date -j -f "%Y-%m-%d %H:%M:%S" "2025-01-01 00:00:00" +%s 2>/dev/null \
  || date -u -d "2025-01-01" +%s)   # macOS BSD / GNU date 両対応

cat <<EOF > /tmp/search.json
{
  "query": "OAuth の失敗事例",
  "limit": 10,
  "source_types": ["crawl", "github"],
  "date_from": ${date_from_epoch},
  "source_metadata": {
    "logic": "AND",
    "filters": [
      {"key": "team", "operator": "eq", "type": "string", "val": "platform"}
    ]
  }
}
EOF
qaip api search.create --json @/tmp/search.json --fields results
rm /tmp/search.json
```

---

## 6. completion（RAG）

```bash
cat <<'EOF' > /tmp/msg.json
[
  {"role":"system","content":"You answer from indexed internal docs."},
  {"role":"user","content":"認証の仕組みを教えて"}
]
EOF

qaip api completion.create \
  --messages "$(cat /tmp/msg.json)" \
  --tags docs --citation \
  --fields choices

rm /tmp/msg.json
```

レスポンスは `{choices:[{message, finish_reason, index, citations?}], created}` の形で、**`citations` は `choices[].citations` の下にある**（top-level には無い）。引用だけ欲しい時は:

```bash
qaip api completion.create --messages "$(cat /tmp/msg.json)" --tags docs --citation \
  | jq '.choices[0].citations'
```

`--citation` は bool フラグで、付けると `citation: true` を body に入れる。**未指定時はキー自体が body に入らない**（= server 側デフォルトに従う）ので、明示的に `false` を送りたい場合だけ `--json '{"citation":false}'` を使う。

---

## 7. 構造化抽出（extract）

`extract.create` は **必須フィールドが `schema`**（JSON Schema）。named フラグ `--schema` / `--prompt` / `--tags` が実装されているので、単純なケースはそれだけで済む。レスポンスは `{created, result}` で **`result`** が抽出結果の object（`data` ではない）。

```bash
# 最小構成
qaip api extract.create \
  --schema '{"type":"object","properties":{"features":{"type":"array","items":{"type":"string"}}},"required":["features"]}' \
  --prompt "リリースノートから新機能名だけを抜く" \
  --tags docs \
  --fields result
```

入れ子の大きい schema や `limit` / `source_types` / `date_from` 等のフィルタを重ねたい場合は `--json @file` に倒す。

```bash
cat <<'EOF' > /tmp/extract.json
{
  "schema": {
    "type": "object",
    "properties": {
      "features": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["features"]
  },
  "prompt": "リリースノートから新機能名だけを抜く",
  "limit": 20,
  "source_types": ["github"]
}
EOF
qaip api extract.create --json @/tmp/extract.json --dry-run
qaip api extract.create --json @/tmp/extract.json --fields result
rm /tmp/extract.json
```

---

## 8. メタデータの一括更新

`sources.batch_set_metadata` / `source-groups.batch_set_metadata` は named フラグ無し、`--json` 必須。body の形は実装型 (`src/qaip/types/source_batch_set_metadata_params.py` など) に合わせる必要があり、2 点の制約がある:

- `sources.batch_set_metadata` の各 item は `source_group_id` と `source_id` の **両方が必須**（データベース制約）。
- `metadata` は `{"k":"v"}` のような free-form dict ではなく、**`{"records":[{"key","val","type"}, ...]}`** 形式。`type` は `MetadataType` の 5 値 `"string" / "integer" / "float" / "date" / "datetime"`（`src/qaip/types/shared/metadata_type.py`）のいずれか。`val` に `null` を入れるとそのキーの削除。

```bash
cat <<'EOF' > /tmp/meta.json
{
  "items": [
    {
      "source_group_id": "<sg-uuid-1>",
      "source_id": "<src-uuid-1>",
      "metadata": {
        "records": [
          {"key": "owner", "val": "platform", "type": "string"}
        ]
      }
    },
    {
      "source_group_id": "<sg-uuid-2>",
      "source_id": "<src-uuid-2>",
      "metadata": {
        "records": [
          {"key": "owner", "val": "growth", "type": "string"}
        ]
      }
    }
  ]
}
EOF
qaip api sources.batch_set_metadata --json @/tmp/meta.json --dry-run
qaip api sources.batch_set_metadata --json @/tmp/meta.json
rm /tmp/meta.json
```

1 件だけなら `sources.update_metadata -i <source_id> --json '{"metadata":{"records":[{"key":"owner","val":"platform","type":"string"}]}}'`。特定キーだけ消したい場合は `val: null` を入れた records を投げる。`sources.delete_metadata` は `DELETE /sources/{id}/metadata` で、その source に紐づく metadata をまとめてクリアするヘルパー（個別キーだけ消したい時は上記 `val: null` 方式を使う）。

`source-groups` 側 (`source-groups.batch_set_metadata`) も同じ `{records:[...]}` 形だが、item の識別子は `source_group_id` のみで `source_id` は不要 — 迷ったら `qaip schema source-groups` で `batch_set_metadata` の `required_params` を確認する。

---

## 9. シークレット作成

`secret` 本体は **stdin** 経由。引数や変数展開に直接載せない。`type` の enum は実装上 **`google_drive` / `github` / `notion` の 3 値のみ**（`github_token` のような綴りは 422 になる）。

2 つの罠を同時に避ける必要がある:

1. `jq -Rs . <<<"$VALUE"` は **here-string が末尾に改行を付与する** → JSON 化された文字列の末尾に `\n` が混入し API に改行付き secret が送られる。
2. `jq -n --arg secret "$VALUE"` は **secret を jq プロセスの argv に載せる** → `ps` で他プロセスから見える（argv 漏えい）。

両方を回避する書き方: **non-secret なフィールドだけ `--arg` で渡し、secret は stdin から `input` フィルタで読ませる**。`printf` はシェル組み込みコマンドなので新プロセスが立たず argv 漏えいしない。

### 9-a. 単一行 secret（GitHub PAT / Notion token 等）

対話入力でワンライナ値を受け取るパターン。multi-line な値（Google SA JSON）はこの方法では最初の行までしか取れないので **§9-b** を使うこと。

```bash
# §0 の qaip_read_silent ヘルパを使って secret を対話入力（空文字・Ctrl-C は abort）
qaip_read_silent SECRET 'GitHub token: ' || { unset SECRET; return 1 2>/dev/null || exit 1; }
[ -z "$SECRET" ] && { echo "empty secret; aborting" >&2; unset SECRET; return 1 2>/dev/null || exit 1; }

# dry-run — name/type は argv、secret は stdin (printf は builtin なので argv に載らない)
printf '%s' "$SECRET" \
  | jq -Rn --arg name gh-readonly --arg type github \
      '{name:$name, type:$type, secret:input}' \
  | qaip api secrets.create --json - --dry-run
# => "body.secret": "***" にマスクされていることを確認。平文が出たら中止。
```

本実行は `--dry-run` を外すだけ。終わったら `unset SECRET` でメモリから消す。

```bash
printf '%s' "$SECRET" \
  | jq -Rn --arg name gh-readonly --arg type github \
      '{name:$name, type:$type, secret:input}' \
  | qaip api secrets.create --json - --fields id,name,type
unset SECRET
```

### 9-b. Multi-line secret（Google SA JSON key）

Service account key のような改行を含む JSON をそのまま `secret` に入れる場合、対話 `read -r` は 1 行しか取れず、`jq 'input'` も raw モードでは最初の LF までしか読めない。安全に済ますには、`0600` 権限の一時ファイルに一旦置いて `jq --rawfile` で読み込む（`--rawfile` はファイル内容を文字列として取り込み、引数には **パス**しか渡さないので `ps` から secret 本文は見えない）。

```bash
# 0600 で一時ファイルを用意し、必ず削除する trap を仕込む
umask 077
sa_path=$(mktemp -t qaip-sa.XXXXXX.json)
trap 'shred -u "$sa_path" 2>/dev/null || rm -f "$sa_path"' EXIT INT TERM

# SA key 本文を sa_path に入れる。既にローカルに ~/secure/sa.json がある想定。
# 手元で編集したい時は `vim "$sa_path"` などを使う（ファイルは 0600）。
cp ~/secure/sa.json "$sa_path"

# jq --rawfile はファイル内容を 1 つの文字列として読み取る。trailing LF が
# 付いていれば rtrimstr で落としておくと、secret の末尾に改行が混ざらない。
jq -n --arg name gdrive-ingest --arg type google_drive \
      --rawfile sa_raw "$sa_path" \
      '{name:$name, type:$type, secret: ($sa_raw | rtrimstr("\n"))}' \
  | qaip api secrets.create --json - --dry-run

# 問題無ければ --dry-run を外して同じコマンドで本実行。
# trap により sa_path はシェル終了時に shred / rm で破棄される。
```

### やってはいけない書き方

- `qaip api secrets.create --secret "$SECRET" ...` — argv にシークレットを載せる（`ps` / 履歴に残る）。
- `jq -n --arg secret "$SECRET" '...'` — `--arg VALUE` は jq の argv に値を載せるので `ps` から見える。secret は必ず stdin から `input` で読むか、`--rawfile` でファイル経由にする。
- `printf '... "secret":%s' "$(jq -Rs . <<<"$SECRET")"` — 上記の改行混入バグ。
- シークレットを `/tmp/*.json` に書いた上で消し忘れる — 使うなら `umask 077 && trap 'shred -u /tmp/x.json' EXIT` で強制破棄を仕込む（§9-b の流儀）。

---

## 10. Agent run（同期ストリームと非同期）

```bash
# 10-1. 同期ストリーム（1 イベント = 1 行）
qaip api agent.run \
  --messages '[{"role":"user","content":"状況を要約して"}]'
# | while read -r line; do ...; done で各行を処理
```

### 非同期: create_run → retrieve / events / cancel

`agent.create_run` はミューテーションで、**`--idempotency-key` を指定しないと呼ぶたびに新しい run が発行される**。ネットワーク再試行や失敗時の再送で run が重複しないよう、同じ論理リクエストには同じ `--idempotency-key` を必ず付けること（同じキーで 2 回目以降は新 run を作らず既存 run を返す）。ワンショットのスクリプトでも dry-run を先に通して body を確認する習慣を付ける。

```bash
# 10-2a. idempotency-key と messages を変数化して dry-run / 本実行で使い回す。
# dry-run は API を叩かず body を組み立てるだけなので、キーの「初回扱い」は本実行が担う。
idem=$(uuidgen)
messages='[{"role":"user","content":"重めの仕事"}]'

qaip api agent.create_run --messages "$messages" --idempotency-key "$idem" --dry-run

# 10-2b. 本実行。`$idem` と `$messages` を同じ値で再利用することで body drift を防ぐ。
# 再試行 / クラッシュ後に再実行しても同じ run が返る。
run_id=$(qaip api agent.create_run --messages "$messages" --idempotency-key "$idem" \
  --fields run_id | jq -r .run_id)

# ポーリング or イベント取得
qaip api agent.retrieve_run -i "$run_id" --fields status
# list_run_events の cursor は UUID ではなく整数 event index （--after <int>）
qaip api agent.list_run_events -i "$run_id" --limit 50 --after 0

# キャンセル（破壊的操作なので dry-run を先に通す）
qaip api agent.cancel_run -i "$run_id" --dry-run
qaip api agent.cancel_run -i "$run_id"
```

`--forwarded-props` や追加メタデータは `--json` で AG-UI 仕様に合わせる。

---

## 11. 全件スキャン（cursor ページネーション）

list 系レスポンスは **`{<resource>: [...], pagination: {has_more, limit, next_id, total?}}`** の dict。次ページのカーソルは **`pagination.next_id`**（末尾要素の `id` ではない）。末尾ページでは `pagination.has_more == false` かつ `pagination.next_id == null`。

```bash
after=""
while :; do
  page=$(qaip api sources.list --limit 100 ${after:+--after-id "$after"} \
    --fields sources,pagination)
  echo "$page" | jq -r '.sources[] | [.id, .name] | @tsv'
  # qaip 仕様では「末尾ページ = has_more=false かつ next_id=null」なので、
  # どちらか一方が null/false になった時点で止める。has_more=false と
  # next_id 有効が同時に来る API （他サービス等）には持ち出せない書き方。
  next=$(echo "$page" | jq -r '.pagination.next_id // empty')
  more=$(echo "$page" | jq -r '.pagination.has_more // false')
  { [ -z "$next" ] || [ "$more" != "true" ]; } && break
  after="$next"
done
```

他リソースは top-level のキー名だけ置き換える: `crawls`, `source_groups`, `secrets`, `google_drives`, `githubs`, `notions`, `local_file_groups`（ハイフンは CLI のコマンド側のみで、レスポンス top-level キーはアンダースコア）。

例外:

- `tags.list` は `{tags:[...]}` のみで `pagination` を持たない（全件返す想定）。
- `agent.list_run_events` は `{events, next_index, run}` の別形で、次ページカーソルは `pagination.next_id` ではなく `next_index`（整数 event index）、フラグも `--after <int>` を使う。

初見のエンドポイントはまず `qaip api <resource>.list --limit 1` を 1 回叩いて top-level 形を確認するのが堅実。

---

## デバッグ tips

- 引数名に自信が無い: `qaip schema <resource>` で `required_params` / `optional_params` を表示。
- body が何になっているか見たい: `--dry-run` が事実上のエコーサーバ。
- 通信レイヤまで見たい: `export QAIP_LOG=debug` で httpx のログが出る（`info` でリクエスト概要）。
- 400 が出る: まず UUID 形式 ID か、必須フィールドの欠落か、enum 値の typo を疑う（`extract.create` の `source_types` など）。
