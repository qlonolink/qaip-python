# Stainless 生成 PR の競合調査

2026-09-08の原因調査と当時の案の記録。最新の合意・実施状況・完了条件は
[原因差分の取り消しを優先する計画](stainless-self-managed-plan.md)を参照する。

## 最新方針: 競合の原因差分だけを取り消す

ユーザーからの簡素化の指摘を受け、[原因差分の取り消しを優先する計画](stainless-self-managed-plan.md)
へ変更した。既存の配布フローを維持し、不要な手書き差分は取り消し、必要な登録は
生成設定への置換を優先する。全面的な自社組み立ては保留とし、以下の全差分移行の
完了条件を今回の限定修正へ一律に要求しない。keywords / snapshots と API key 旧名の
撤去候補は実装・ローカル検証済み。新設定の生成物との照合、統合、再発確認は未完了。

## 前案の記録: サポートを使わず自社で組み立てる

ユーザーの指示により問い合わせを前提から外した。
当時の案は [配布時補正の検討記録](stainless-distribution-experiment.md) を参照する。
生成後の隔離コピーへ互換補正を機械適用した試作で、従来失敗していた 10 ケースを含む
公開契約 75 件と #259 の先行契約 27 件、計 102 件が Pydantic v1 / v2 とも成功した。
CLI を含む wheel の隔離インストールも確認した。本番フロー・既存 PR は未変更。

以下は原因調査と以前の移行案の記録である。「外部対応が必要な残件」、upstream 待ち、
純生成物だけで全互換性を満たす条件、staging 管理者による強制を前提とした手順は、
最新計画では前提にしない。必要な保護処理は手書き差分として残す。

## 実施状況（2026-09-08）

生成定義の移行は qdev の [draft PR #7737](https://github.com/qlonolink/qdev/pull/7737)
で進めている。SDK の作業ブランチは `avoid-conflict`。公開・統合先へのマージは未実施。

| 基準 | SHA / 版 |
| --- | --- |
| 公開 SDK / production main | `v0.14.0` / `a238440b136d908bafb3c6d907951c3ed47e3676` |
| staging・production next / SDK 作業ブランチの基準 | `a0be5ba3cc960d449fe9d9022059a91816f8d180`（#259 を含む） |
| staging generated | `fcaa350ccbfc9630e980de0f478da54f9f35a838` |
| qdev 移行元 | `1349aa12bccefa2c702c4124dc179900733b0832` |
| qdev 初回設定 | `aa7c6872d3fec0561ff292e7f010d0e799c4f7ae` |
| 初回設定の純生成 Python SDK | `dc63c9997f8244449be9f0d064a8bc5cb55cdcb5` |
| 最新 qdev 設定 | `70404e5a219363c3b911821079701c21f0ee7f5c` |
| 最新設定の純生成 Python SDK | `591dd064625ada7fc670587a15e6200fe68566fe` |

[初回 preview job](https://github.com/qlonolink/qdev/actions/runs/34204140599) は成功。
ログの入力は上記 qdev head と一致し、OpenAPI hash は
`4fa285c4c88d00650de2b75da7ce6f87`、config hash は
`019ddec8c5e9c16566c250522b682738`。ジョブ開始直後の preview ref は古い初期
コミットを指していたため、ジョブ完了後に取得した SHA のみを検証対象とする。

初回生成結果の確認:

- conversations、external_queries、tag_management、agent threads の登録・実装が
  生成された。既存の import / 全応答型 / signature の一致は検証途中。
- `custom_casings.api.initialism: false` により公開済み `ApiKeysResource` /
  `CreatedApiKey` の名前を生成できた。#259 の未公開の大文字名との両立は未解決。
- `multipart_settings.array_format: repeat` は基盤側に反映され、通常の同期・非同期
  client を通した既存 multipart テスト 2 件が純生成版で成功した。
- `default_request_options.max_retries: 0` は Python の対象 method に反映されず、
  純生成版の API key 再送抑止テスト 2 件が失敗した。SSE テスト 4 件も失敗した。
  設定の schema 検証・preview job の成功だけでは、これらの patch を除去できない。
- query の `202 PREPARING` 型の欠落は、Stainless 専用 schema override で補正した。
  keywords / snapshots の `custom: true` 登録と独自 SDK 型の生成も確認できた。

SDK 作業ツリーでは、CLI・extract_files・crawl・requested API coverage・API key の
legacy / phase5 契約の手書き専用 6 ファイルを `tests/custom/` へ移設し、元を除去した。
keywords / snapshots の旧 skip テスト 2 ファイルも同ディレクトリへ移設した。
`test_client.py` / `test_streaming.py` の multipart / SSE ケースは独立ファイルへ
切り出し、この 2 ファイルを固定した `generated` の内容へ戻した。旧 retry テストの
コピーは新しい legacy 契約に包含されることを確認して除去した。

移設対象と基盤テストの収集比較では、既存 455 件の欠落・重複はなく、境界チェック
24 件を加えた 479 件が Pydantic v2 / v1 の両環境で成功した。これは現在の SDK を
用いた移設の検証であり、純生成候補の互換性合格ではない。

さらに keywords / snapshots の 6 method × 同期・非同期 × 5 種類のアクセス
（通常、resource/client 経由の raw・streaming）の 60 ケースを追加した。
最新生成版に独立した 2 つの custom resource ファイルのみを加えた候補で、
これらと multipart の計 62 件が Pydantic v1 / v2 の両方で成功した。
公開 PyPI wheel `qaip==0.14.0` を隔離インストールし、公開契約 75 ケースの成功も
確認した。最新候補では同じ 75 ケースのうち 65 件が成功し、再送抑止・SSE の
10 件が失敗する。したがって全置換はまだ実施できない。

公開 wheel の 182 module・539 export を比較し、最新候補で import の欠落はない。
主要 7 resource の同期・非同期計 52 method は、引数名・必須性・positional /
keyword の区分が一致した（keyword-only 引数の並び順は互換性の差と扱わない）。
この比較だけで全応答型・通信挙動の一致を証明したとは扱わない。

SDK 作業ツリーの最終確認は Pydantic v2 が 878 passed / 1638 skipped、v1 が
865 passed / 1651 skipped。Ruff、Pyright、Mypy も成功。Rye が環境にないため、
同じ lockfile の依存と pytest / lint ツールを直接実行した。uv build で作成した
wheel を別の隔離環境へ入れ、ソース参照なしの `qaip --version`、`qaip schema`、
`qaip api sources.list --dry-run`、Python import と主要 client 属性を確認した。
これらは現在の SDK の検証で、生成候補の wheel 合格ではない。

固定した generated / next 間の全 101 差分の所有者・移行先・検証を
[所有範囲一覧](stainless-ownership.tsv) に記録した。README、lockfile、workflow の
差分がない項目も確認対象に含めた。

### 以前、外部対応が必要と判断していた残件（新計画で代替）

[Stainless への確認・修正依頼の下書き](stainless-generator-compatibility.md) に、
再送抑止、SSE、#259 の 409 / 例外保持、CLI entry point の生成方法をまとめた。
送信は未実施。公開名を生成できても #259 の未公開大文字 alias の互換性は別問題で、
先行契約を黙って削除しない。

境界 CI は既存の未追跡候補のままで、運用 fixture・必須化は未完了。
staging の権限は maintain / admin=false、ruleset API はプラン制限の 403。
production は admin 権限があり main の ruleset は有効だが、next の branch
protection は未設定だった。staging を含む強制は管理側への確認が必要。
親・既存 preview の競合解消、qdev / SDK のマージ、差分を加えた再生成試験も未実施。

## 原因と発生時期

SDK の生成領域へ手追加したコードが、Stainless の新しい生成結果と衝突している。
Stainless は親ブランチの手書き変更を各 preview に引き継ぐため、対象機能と無関係な
preview でも同じ競合が発生する。

最初の競合 PR は [#10](https://github.com/stainless-sdks/qaip-python/pull/10)
（2026-08-03 16:33 JST）。その base/head を取得して `git merge-tree` で再現した。
競合は `src/qaip/_client.py` の次の import 追加同士だった。

- 手書き側: `UserKeywordSnapshotsResource` / `AsyncUserKeywordSnapshotsResource`
- 生成側: `RedactionPoliciesResource` / `AsyncRedactionPoliciesResource`

前者は [#5](https://github.com/stainless-sdks/qaip-python/pull/5)
（2026-06-23 JST マージ、コミット `9051253`）で導入された。
コミット本文にも「Stainless 生成スタイル準拠の手動パッチ」とある。
したがって、少なくとも最初の競合は生成器の変更を仮定せず説明できる。

## 現在の競合

### 2026-09-08 19:25 JST の処置一覧

[競合 PR の状態・SHA・処置一覧](stainless-conflict-pr-status.tsv) に、現時点の
open PR と以前の調査対象の計 18 件を記録した。これは読み取りで確認した状態と
今後の処置であり、この作業から close / merge は実行していない。

- bulk-delete の qdev #7458 は OPEN。旧 #257 / #258、#262 / #263 は CLOSED で、
  現在の対応は #272 / #273。親の移行後に最新入力で再生成する。
- issue 6332 の qdev #7465 も OPEN。旧 #207 / #208 は CLOSED で、現在は
  #269 / #271。古い機能だから不要と判断せず、継続対象として再生成する。
- issue 7643 の qdev #7731 は 2026-09-08 15:46 JST に MERGED。
  head 側 #256 は CLOSED、base 側 #255 は OPEN。親へ最新の生成結果が統合された
  ことを確認してから、残る base preview を不要として閉じる対象にする。
- issue 7415 の qdev #7470 は OPEN、#244 / #245 が引き続き競合している。
- 今回の qdev #7737 の最新 preview は #274 / #275 で競合している。純生成 job の
  成功を、手書き変更を含む統合 preview の成功と取り違えない。

親 #216 と解消候補 #237 の base はともに
`0c9e8162ddf8678959ebeefac9c099878962fb25`。#237 の head
`17f0ded7a78d43eabc5645f84f835ddf97cae2fb` は #216 の生成 head
`91ee0ff2c8faf2abd5a6aa5067d0353b29313639` を祖先に持つ。
base と #237 head を一時 object directory で `git merge-tree --write-tree` にかけ、
競合なく merge でき、結果の tree `bf6a8040b5cd0a09078b746ed944be8e9503b847` が
固定した next `a0be5ba` と同一であることを確認した。したがってこの固定された
#216 の解消には #237 を利用する方針とする。最新 generated や今回の設定変更を
すべて含む候補ではないため、全体の移行・互換性の条件とは分けて扱う。
実行前には base/head が進んでいないことを再確認する。

### 調査開始時点の競合

API keys の SDK は [#75](https://github.com/stainless-sdks/qaip-python/pull/75)
で手追加され、後の生成更新で同じファイルが生成された。
`resources/api_keys.py` と関連型には add/add 競合がある。

次の 7 PR は、調査開始時点で同じ API keys 関連 9 ファイルに競合していた。

- 親: [#216](https://github.com/stainless-sdks/qaip-python/pull/216)
- bulk-delete: [#257](https://github.com/stainless-sdks/qaip-python/pull/257)、[#258](https://github.com/stainless-sdks/qaip-python/pull/258)
- issue 7643: [#255](https://github.com/stainless-sdks/qaip-python/pull/255)、[#256](https://github.com/stainless-sdks/qaip-python/pull/256)
- issue 7415: [#244](https://github.com/stainless-sdks/qaip-python/pull/244)、[#245](https://github.com/stainless-sdks/qaip-python/pull/245)

共通の競合ファイル:

```text
api.md
src/qaip/_client.py
src/qaip/resources/__init__.py
src/qaip/resources/api_keys.py
src/qaip/types/__init__.py
src/qaip/types/api_key_create_params.py
src/qaip/types/created_api_key.py
src/qaip/types/issuable_api_key_scope.py
tests/api_resources/test_api_keys.py
```

調査中に [#259](https://github.com/stainless-sdks/qaip-python/pull/259) が `next` に
反映された（`a0be5ba`）。再 fetch 後も #216 の競合ブランチには上記のうちテストを除く
8 ファイルの競合が残っていた。通常の `next` 向け PR のマージと、Stainless の
競合 PR の解消確認は別に必要となる。以後の更新状況は実施直前に再確認する。

既存の解消用 [#237](https://github.com/stainless-sdks/qaip-python/pull/237) も対象に含める。
2026-09-08 の再確認では OPEN / MERGEABLE で、取得済み head のファイル内容は
#259 後の `next` と一致していた。ただしマージ可能であることだけで採用せず、
現在の #216 の base/head に対応する解消かを検証する。#237 を使うか、最新の
競合ブランチから解消を作り直すかを先に決め、二重に解消変更を投入しない。

[#207](https://github.com/stainless-sdks/qaip-python/pull/207) と
[#208](https://github.com/stainless-sdks/qaip-python/pull/208) は別の古い生成更新で、
Agent、redaction policies、stream event params など 8 ファイルに競合していた。
API keys の解消だけですべての preview が直るわけではない。

## 恒久対策

### 0. 基準と移行対象を固定する

実装担当は SDK staging / production と qdev を fetch し、ローカル `main` は
作成・使用せず、リモート参照から作業ブランチを作る。次を移行 PR に記録する。

- 互換基準となる公開 tag・wheel と、それに対応する SDK commit。
- staging の `next` / `generated`、production の公開・開発ブランチの SHA。
- qdev の基準 SHA、OpenAPI 入力、`stainless.yml`、対応する preview の生成 SHA。
- #259 など公開前の変更のうち、維持する API・通信挙動。公開済み契約と区別する。

qdev の [#7628](https://github.com/qlonolink/qdev/pull/7628) は 2026-09-07 に
`main` へマージ済みである。古いローカル `origin/main` や未統合時の
`bff-phase5-public-api` を前提に再実装しない。実施時点のリモートで再確認する。

純生成と統合版の全ファイル差分を取り、`ファイル → 所有者 → 独自変更の理由 →
移行先 → 合格させるテスト` の一覧を作る。resource/type だけでなく
`_models.py`、`_types.py`、テスト、`pyproject.toml`、README、CHANGELOG、lockfile、
workflow も含める。リリース由来の差分と、生成コードへの手書き差分を区別する。
`pyproject.toml` の CLI entry point もインストール後の互換性の対象とする。

移行中は対象生成領域への新たな手書き変更を凍結する。緊急修正や生成更新で基準が
進んだ場合は SHA と一覧を更新し、影響する互換テストと生成比較をやり直す。
凍結と最終 CI の適用範囲は staging / production 双方の取り込み経路を対象とする。

### 1. qdev で SDK 定義を生成できるようにする

qdev の OpenAPI と `stainless.yml` を変更し、公開済み SDK の次の機能を生成対象にする。
SDK 側だけで生成コードへ機能を追加する運用を止める。

投入元は `.github/workflows/update_mintlify_api_references.yml` にある
`app/openapi/qdev_api.yaml` と `stainless.yml` である。直下の `openapi.yaml` は
この workflow の入力ではない。API keys の契約は
`app/openapi/fragments/public_api_keys.yaml` を編集し、bundle 内の対応する
生成領域を手編集しない。fragment 変更後は qdev で以下を実行する。

```bash
mise run app:bundle:openapi
mise run app:check:openapi-bundle
mise run app:generate:openapi
```

それ以外の API は、基準 SHA の bundle の path/schema と `stainless.yml` の
定義を照合する。既存契約がある conversations、agent threads、query、tags は
不足する SDK 設定を追加し、契約自体の変更が必要な場合だけ所有元を編集する。

| 手書き差分 | 移行先と確認事項 |
| --- | --- |
| conversations、external_queries、tag_management、agent threads | OpenAPI の path / schema と Stainless の resource / method / model 定義。同期・非同期、raw・streaming wrapper も保持する |
| keywords、user_keyword_snapshots | 公開 API として OpenAPI に定義するか、生成対象外の拡張へ分離する。既存の SDK 呼び出しを先に削除しない |
| API keys の既存名 | 公開済み `ApiKeysResource` / `CreatedApiKey` / `IssuableApiKeyScope` と生成側の `APIKeysResource` / `CreatedAPIKey` / `IssuableAPIKeyScope` の扱いを決める。必要な互換 alias は独立ファイルへ置けるか検証する |
| API key 発行・external query 作成の再試行抑止 | メソッドの request option 設定へ移し、実際の生成出力と HTTP モックで再試行しないことを確認する |
| local-file-groups の multipart 配列 | encoding の指定と生成器の対応を確認する。既存の repeat 送信が壊れないことを検証する |
| SSE の空フレーム・文字列処理 | Stainless 生成ランタイムでの対応、または独立した stream 拡張を検証する |
| #259 の API key 409 / 本文読み取り処理 | 最新版に追加された挙動も移行対象に含める。重複発行防止、復旧用 ID と元の例外の保持を回帰検証する |

特定の設定だけですべて表現可能とは確認できていない。
生成器に依存する部分は preview の実出力で確認し、表現できないランタイム修正は
Stainless への修正依頼か独立した拡張が必要となる。

次の判断・実証を cleanup の開始条件とする。未解決の項目は移行完了と扱わない。

- **keywords / snapshots**: 公開 OpenAPI に path がなく、確認できるのは Dashboard
  の Connect サービスである。OpenAPI の追記だけで REST API が動くとは扱わない。
  qdev の API 担当が公開の要否を決める。公開するなら handler・routing・認証認可・
  dev 実環境テストを含む別の変更として定義する。公開しないなら既存の
  `Qaip.keywords` 等を維持できる拡張を実証するか、互換破壊を承認した廃止計画が
  必要となる。この文書は新規公開や既存 API 廃止を承認するものではない。
- **公開型名**: model のキー名を指定するだけでは頭字語の変換まで制御できない。
  `custom_casings` 等の設定を候補として、既存 import path と client 属性を保つ
  実際の出力を確認する。独立した alias ファイルを置くだけで既存 export まで
  保てるとは仮定しない。設定の影響が他の公開名へ及ばないことも検証する。
- **通信挙動**: 各項目について、使用する設定・拡張の接続方法・取り込み済みの
  upstream 修正のいずれかを記録し、通常の `Qaip` / `AsyncQaip` と生成 resource
  経由で既存挙動を再現する。APIキーの確定409に `x-should-retry: false` を返す
  サーバー側対応も候補だが、本文読み取りエラーの保持まで同等とは仮定しない。
  サーバー変更に依存する場合は先に対象環境へ反映・検証してから SDK patch を外す。
  実現手段が未確認のランタイム patch は、その項目の cleanup を止める条件となる。

型名設定の候補は [Stainless の設定リファレンス](https://www.stainless.com/docs/reference/config/#custom_casings)
に基づく。設定が存在することと、この SDK で互換な出力が得られることは区別する。

### 2. 対応する生成結果で、蓄積した手書き差分を一度除去する

生成定義の追加だけでは、親ブランチに残った手書き差分は消えない。
新しい preview の生成結果と既存 SDK を比較して、対応済みの手書き実装を除去する。
`_client.py` の登録、resource/type の export、`api.md` も対象となる。

手書きテストを `tests/custom/` に移し、生成された API テストと分離する。
同名コピーを残すだけで移設完了とせず、元の手書き専用ファイルを除去し、生成テストへ
混在した hunk は切り出して生成版へ戻す。収集されるテストの重複・欠落も確認する。
生成側を一括採用すると、まだ生成されていない API や再試行抑止を失うため、
公開 API と通信挙動の互換テストを通した単位で移行する。

統合の順序は以下とする。実装担当が各 SHA・検証結果を記録し、レビュー担当が
生成比較と互換性の合格を確認して次段階へ進める。

1. 既存の各競合 PR の base/head SHA、対応する qdev PR、生成機能、最新の生成結果に
   包含済みかを一覧にする。処置を「現 PR で解消」「最新入力で再生成」
   「置換済みとして閉じる」に分ける。#207 / #208 を古いまま一律にマージしない。
2. qdev の移行 PR を作り、**最新 head SHA に対応する** preview job と生成 SHA の
   完了を確認する。統合 preview が競合で停止していても、純生成の
   `codegen/preview/<qdev-branch>` は別に取得して比較できる。
3. その生成 SHA と維持する手書きコードから、通常の作業ブランチに候補を組み立て、
   互換テストを実行する。競合解消が必要なら対応する `--merge-conflict` PR の
   所定手順で反映する。通常の `codegen/**` / `integrated/**` は直接編集しない。
4. 最新 qdev head の preview と候補が合格してから qdev PR をマージする。
   workflow は最後の preview を merge するため、古い preview の成功で代用しない。
5. 親の生成更新を確認し、必要な親の競合解消と SDK cleanup を反映する。
   `next` 向け境界チェックが使う `generated` に候補が到達する前に、preview の
   内容へ復帰する人 PR を `next` に出さない。#237 を利用する場合も手順1の最新
   base/head と照合する。反映後に親の再生成と互換テストを確認する。
6. 継続する各 qdev PR を最新の親へ追従させ、PR の更新による preview workflow で
   再生成する。head/base 両 preview の生成 SHA と統合結果を確認する。
   不要になった preview / conflict PR は一覧の処置に従って閉じる。

個々の preview の競合解消のみを恒久対策としない。

### 3. 手書き差分の再導入を CI で防ぐ

作業ツリーには境界チェックの未追跡ファイルが既に存在している。
境界チェックを整備して必須化する。既存の競合解消・生成移行は別途必要。
2026-09-08 の調査では境界チェックの単体テスト 24 件が成功したが、以下の運用まで
検証した結果ではない。

- 人による生成領域の変更は、生成定義へ移すか独立した手書きファイルへ移す。
- 生成結果への復帰は、その preview に対応する生成 commit と比較する。
- Stainless Bot とリリース処理を妨げない条件を確認する。
- CLI ブランチの命名統一は補助的な運用であり、既存の競合を除去する機能ではない。
- `docs/stainless-development.md` の「分離済み」は現ブランチの状態と一致しない。
  現在も `api.md` と `tests/api_resources/` などに手書き差分が残っている。

導入前に同文書を「移行中」という実態に合わせ、型名は実出力で検証することと、
`--merge-conflict` ブランチには公式の解消手順を適用することを明記する。

全ファイルの所有範囲に合わせてチェックを拡張し、生成比較には検証済みの SHA を使う。
人の通常 PR、cleanup、Stainless の生成・競合解消 PR、リリース PR の許可・拒否を
fixture で検証する。Bot の commit author と PR 作成者は区別し、Bot 全体への
無条件な除外は設けない。ブランチ名だけを変更しても許可されないことを確認する。

管理担当が対象ブランチの ruleset / branch protection にチェックを必須登録し、
人による直接 push と bypass で抜けられないことを確認する。Stainless に必要な
取り込み経路は維持し、merge queue を使う場合はそのイベントでも検査する。
workflow ファイルを置いただけで強制が完了したとは扱わない。

### 4. 検証と完了条件

1. 公開基準版と移行候補をそれぞれ隔離環境へインストールし、既存 import path、
   client 属性、method signature、HTTP method/path/query/body/header、応答型、
   同期・非同期と raw・streaming wrapper を同じ契約テストで検証する。
   #259 の先行契約は別ケースとして検証し、公開版に存在しない API を要求しない。
2. 移設後の `tests/custom/` には、既存 `tests/test_api_key_legacy_contract.py`、
   `tests/test_api_key_phase5_contract.py`、`tests/api_resources/test_requested_api_coverage.py`、
   CLI、crawl raw、multipart、SSE の手書きテストを保持する。契約不足のケースは
   cleanup 前に追加する。SDK ルートで `bash scripts/test tests/custom -q` を実行し、
   Pydantic v1 / v2 の両環境で必須ケースが skip されず成功することを確認する。
   さらに `bash scripts/test` と `bash scripts/lint` を通す。生成テストの skip は
   互換性の成功件数へ数えない。
3. `rye build` の wheel をソース参照のない隔離環境へインストールし、`qaip --version`、
   `qaip schema`、代表的な `--dry-run` と Python import を検証する。新しいサーバー
   契約へ依存する項目は、承認された dev 環境でも該当契約を確認する。
4. 固定した生成 SHA と統合 SHA の全差分を所有範囲一覧と照合する。生成器が所有する
   内容は生成出力と一致させる。リリース由来の差分は対応するリリース処理で説明し、
   独立した手書き領域の変更は一覧と一致することを確認する。生成領域の手書き patch
   が残る項目は未完了とし、単に理由を記録して完了扱いにしない。
5. 親と継続する preview の最新版が競合せず統合され、一覧の競合 PR が処置済みで
   あることを確認する。さらに試験用 qdev PR で、今回衝突した resource 登録や
   schema を実際に変える preview を生成し、新しい生成差分でも手動解消なしに
   統合されることを確認する。同一入力の再実行だけを再発防止の証拠にしない。
6. 手書き変更の再導入を拒否する必須チェックが有効で、生成・解消・リリースの
   正規フローは成功する。以上の証拠を移行 PR に残して完了とする。

## 参照

Stainless の [custom code の公式説明](https://www.stainless.com/docs/sdks/configure/custom-code/)
では、手書き差分を生成結果へ三者マージし、親の差分を preview に引き継ぐこと、
競合 PR が開いている間は統合更新が停止することが説明されている。
同じ説明で、設定で表現できる変更を設定へ移すことと、独立したファイルでの拡張を推奨している。

`generated`、`codegen/**`、`integrated/**` の通常の作業ブランチを直接編集しない。
競合解消は、公式説明と各競合 PR 本文にある `--merge-conflict` ブランチ向けの
手順に従う。
