# Stainless 競合を原因差分の取り消しで解消する

2026-09-09 レビュー合意を反映。**互換性より将来の保守性を優先し、競合原因の
手書き差分を取り消して、対応する生成内容へ戻す**。SDK の機能定義は公開 OpenAPI と
`stainless.yml`、型名は Stainless の標準生成名に揃える。既存の生成・配布フローを維持する。
サポートへの問い合わせや、独自のパッケージ組み立て基盤を前提にしない。
生成設定の絞り込みは実施済み。今回の削除・改名を含む SDK 候補を実装中で、
候補全体の検証・統合・再発確認は未完了。

## 実施状況（2026-09-09）

- 親1件・preview 9件の競合を base/head SHA と衝突ファイルで確認し、
  [PR 一覧](stainless-conflict-pr-status.tsv)を更新した。候補検証後の処置は未実施。
- qdev #7737 を親 `4cccf6d31` へ追従し、設定を63行の追加に絞った。
  入力 SHA は `079b29c0cf6e090d0e65c403ddf8079330db2d6f`。
  YAML と Stainless config schema の検証は成功。
  [生成ジョブ](https://github.com/qlonolink/qdev/actions/runs/34318634525)は成功表示だが、
  実際には結果の観測が600秒でタイムアウトした。新しい生成結果は未確認。
  head のビルド `bui_0cmttpo0kt002n24s65zh67vb6` と
  base のビルド `bui_0cmttpnynn002m24s6djrg5vif` を公式 API で再確認した。
  [状態・履歴取得ログ](https://github.com/qlonolink/qdev/actions/runs/34321082998)では、
  15:54 JST 時点でも両方の Python / OpenAPI が `not_started`。
  本日10:40 JST以降の既存10ビルドもすべて同じ状態で、今回の2ビルドの診断結果は空。
  昨日の10ビルドは完了しているため、今回の設定だけに限定された開始待ちではない。
  新規ビルドを重複起動せず、同じ ID の状態を追跡している。
- SDK 候補の keywords / snapshots は、SDK resource・型・client・export・API文書・CLI・
  schema・旧機能維持だけのテストから撤去した。API key の旧名 alias も除去し、利用側を
  `APIKeysResource` 等へ揃えた。API key の3型ファイルは親の純生成 `fcaa350` と一致し、
  resource は再送抑止のみを保持する。conversations 等の最新生成物への置換と
  `ConversationScopeParams` の撤去は未実施。
- 撤去差分のコミットは `62af57d`。この候補で `bash scripts/test tests/custom -q` は
  v1/v2 とも **287 passed、skipなし**。
  `bash scripts/test` は v2 **793 passed / 1518 skipped**、v1 **780 passed / 1531 skipped**。
  `bash scripts/lint`（Ruff・Pyright・Mypy・import）も成功。Rye 0.44.0で実行した。
  wheel/sdist のビルドと、wheel単独の環境での `qaip --version`、`qaip schema`、
  API key作成・conversations一覧の `--dry-run`、新名import・廃止moduleの除去を確認した。
  これは撤去差分の検証であり、新設定の純生成物との一致・統合・再発確認の完了ではない。

Stainless は2026-05-18に、SDK生成を含むホスト製品の終了方針を
[発表している](https://www.stainless.com/blog/stainless-is-joining-anthropic/)。
今回の `not_started` との因果関係や、このプロジェクトの停止日は未確認。
本計画の生成フローを継続できるかに関わる前提であり、新規出力が得られない状態では
最新生成物との一致・統合・再発試験の完了を判定できない。

## なぜ前の案を縮小するか

前の計画では「毎回の競合をなくす」という目的を、「すべての生成ファイルから
手書き差分をなくし、既存挙動もすべて維持する」まで広げていた。
そのため、今回の繰り返す競合の原因と確認されていない SSE・CLI 配布まで
同時に作り替える案になった。この全面移行は現段階では必要と判断できない。

配布時の自動補正の試作は [検討記録](stainless-distribution-experiment.md)に残す。
これは単純な取り消し・生成設定への置換で対処できないと判明した場合の保留案とする。

## revert でよい範囲

| 対象 | 優先する処置 | 注意点 |
| --- | --- | --- |
| API keys の手書き resource/type と生成物の重複 | 手書き追加を取り消し、対応する生成実装を採用する | #75 は SDK に加えて CLI と再送抑止も含む。コミット丸ごとの revert は削除範囲が広い |
| API keys の型・resource 名と互換 alias | 標準生成名へ統一し、旧名の alias と旧名維持だけの命名設定を撤去する | 採用生成 SHA で名前・import path を確定し、CLI とテストを追従させる。両綴りの維持を完了条件にしない |
| `_client.py`、resource/type の export、`api.md` への手動追加 | 公開 API に対応する登録は OpenAPI / `stainless.yml` から生成し、手書き差分を除去する。keywords / snapshots の登録は撤去する | conversations 等の維持する機能は、登録を生成へ置き換えて呼び出せることを確認する |
| keywords / snapshots | SDK の resource/type・client 登録・export・関連 CLI・API 文書と、旧機能の維持を要求するテストを整合的に撤去する | 公開 REST 仕様・ルーティングに定義がない。`custom: true` と SDK 専用 schema による維持案は採用しない |
| `tests/api_resources/test_api_keys.py` などの生成所有テスト | 対応する生成 SHA のテストへ戻す。維持する手書き契約が混在していれば先に `tests/custom/` へ移す | 生成テストの skip を動作検証の成功とは数えない |
| SSE、CLI entry point、CLI 配布 | 初回の取り消し対象に含めず保持する | CLI 内の参照・コマンド登録は上記の削除・改名に追従させる |

keywords / snapshots は、確認した qdev `c63536d7` の `app/openapi/qdev_api.yaml` と
`dashboard/backend/main.go` では公開 REST API の対象にない。管理画面用の別方式の API
（Connect サービス）は存在する。本番での SDK 利用状況は未確認であり、今回の撤去は
互換性破壊を許容して SDK の機能を公開 API 仕様に揃える判断に基づく。撤去対象は SDK・CLI
側とし、将来必要になった場合は公開 API の仕様・サーバー実装を揃えた上で生成する。

API key/query 周辺で当面残す手書き差分は、再送抑止と、`_base_client.py` の確定 409・
本文エラー保持とする。旧方式のキー発行・query 作成は自動再送を抑止し、期限付き発行の
一時的な失敗には同じ要求 ID で再試行する。確定した 409 では再試行を止め、復旧用 ID を
保持する。応答本文の読み取りが失敗した場合は元の例外を保持する。対象生成 SHA でも
同じ挙動を確認できるまで削除しない。
既存の生成検証では `max_retries: 0` の設定が Python 出力に反映されなかった。
これらの保護処理は、設定だけで置換できるとは扱わない。

古いコミット全体の逆差分よりも、**現在の差分のうち原因になっている部分を取り消す**
方法を優先する。後続の生成変更・#259 の期限付き API key 発行などを一緒に削らずに済む。
一つの古いコミットを revert すれば、後から同じ場所へ入った修正も全部消えるとは扱わない。

## 利用側の変更と保持する差分

以下は今回の合意に基づく変更一覧。SDK候補の全体検証は最新生成結果の取得後に行う。

| 対象 | 利用側の変更 |
| --- | --- |
| `ApiKeysResource` / `AsyncApiKeysResource` | `APIKeysResource` / `AsyncAPIKeysResource` へ変更する。`WithRawResponse` / `WithStreamingResponse` 付きの同名クラスも `API` の綴りへ揃える |
| `CreatedApiKey` / `ApiKeyCreateParams` / `IssuableApiKeyScope` | `CreatedAPIKey` / `APIKeyCreateParams` / `IssuableAPIKeyScope` へ変更する。ファイルの snake_case import path は維持する |
| `ConversationScopeParams` | 利用する生成メソッドの引数型へ変更する。`principal_id` などの通信上の引数は維持する |
| `client.keywords` | `create` / `retrieve` / `update` / `list` / `delete` と raw・streaming wrapper、関連型を撤去する。対応する公開 REST API がないため代替 SDK メソッドは設けない |
| `client.user_keyword_snapshots` | `create` と raw・streaming wrapper、関連型を撤去する |
| CLI | `keywords.*` / `user-keyword-snapshots.*` をコマンド一覧と `qaip schema` から撤去する。API key の操作名は維持し、内部 import を生成名へ揃える |

固定した `generated=fcaa350` / `next=a0be5ba` の差分から、以下の hunk を選別した。
新しい生成結果の取得後に、同じ処置が適用できるかと保持契約の成功を確認する。

| ファイル・差分 | 処置と理由 | 検証 |
| --- | --- | --- |
| `_client.py`、`resources/__init__.py`、`types/__init__.py`、`api.md` の手動登録 | 新設定から生成した内容へ戻す。keywords / snapshots と API key 旧名の重複登録を除去する | import、CLI schema、requested API coverage |
| `resources/api_keys.py` と API key 型の alias | 生成名へ戻す。legacy `create` の同期・非同期 `max_retries=0` の設定と適用、計4 hunkを保持する | legacy契約・phase5契約 |
| `resources/conversations.py`、`external_queries.py`、`tag_management.py`、`agent.py` と対応型 | 公開仕様に対応する設定から生成する。query作成の同期・非同期の再送抑止は保持する | requested API coverage、CLI |
| `_base_client.py` の409判定・同期/非同期の本文読み取り | 3 hunkを保持する。確定エラーの復旧IDと本文読み取りの元の例外を保護する | phase5契約 |
| `_base_client.py`、`_models.py`、`_types.py`、local file groups の独自 multipart option | 生成設定の `array_format: repeat` へ置換し、独自 option の差分を除去する | multipartの同期・非同期テスト |
| `_streaming.py` の空data除外・文字列型の処理 | 同期・非同期の2 hunkを保持する | SSE契約 |
| `src/qaip/cli/**`、`src/qaip/__main__.py`、`pyproject.toml` の entry point | 独立した CLI と配布を保持し、上表のコマンド撤去・import変更を反映する | CLIテスト、wheelの起動・schema・dry-run |

## 実施手順

適用順は、**候補の検証 → 既存競合の解消と生成設定・SDK 差分の取り込み →
継続 PR の再生成による再発確認**とする。

1. 現在の親と継続 preview の競合箇所を固定 SHA で確認し、手書き変更と対応づける。
   既存の [調査結果](stainless-conflict-investigation.md)と
   [PR 一覧](stainless-conflict-pr-status.tsv)を起点に、実施時点の状態を再確認する。
   参照するのは状態・SHA・競合の根拠であり、旧計画の全面移行条件や TSV の旧処置案は
   引き継がない。各 open PR に「解消」「最新入力で再生成」「置換済みとして close」を
   割り当て、取り消す hunk と残す hunk をファイル・内容・理由付きで記録する。
2. 上記で撤去する SDK メソッド・型名・CLI と、維持する機能・通信挙動を一覧にする。
   keywords / snapshots と旧名の alias は撤去し、残す公開 API は生成設定への置換か
   保護処理の hunk の保持で維持する。削除・改名の一覧と利用側に必要な修正を候補 PR に
   記載し、機能差を差分とテストで確認できる形にする。
3. qdev #7737 の検証結果から、維持する機能に必要な設定だけを利用する。
   旧名維持だけの `custom_casings.api.initialism: false`、keywords / snapshots の
   `custom: true` 登録と SDK 専用 schema は取り除く。設定を変更する場合は最新入力の
   preview を生成し、対応する純生成 SHA を確定する。過去の互換性維持案の生成結果を
   今回の候補の検証結果として流用しない。親の統合が競合で停止していても純生成結果は
   別に確認する。別 preview の内容を現在の親へ無条件に上書きしない。
   設定変更が不要なら、親に対応する既存の生成 SHA を固定する。
4. 確定した生成 SHA を使い、通常の作業ブランチに取り消し候補を作る。候補には
   SDK #278 のテスト移設コミット `dbaca58` を含め、`tests/custom/` を利用可能にする。
   `bash scripts/test tests/custom -q`、`bash scripts/test`、`bash scripts/lint` を実行し、
   API key の再送抑止・期限付き発行・確定 409・本文エラー保持、query、SSE、multipart 等の
   維持する挙動が Pydantic v1/v2 とも skip されず成功することを確認する。
   CLI の起動、`qaip schema` の一覧、変更したコマンドの `--dry-run` も確認し、生成名での
   import が成功し、廃止した名前への未解決参照やコマンド登録が残っていないことを確かめる。
   旧名の alias や keywords / snapshots の維持を要求するテストは削除・更新する。
   同じテストファイルに含まれる再送抑止等の保護処理の検証は残し、import を生成名へ直す。
   CI は同じ候補 SHA の push 実行で lint/test/build が成功したことを確認し、
   PR イベントの skip で代用しない。
5. 候補の検証後、親の既存競合を公式の手順で処置する。#237 を使う場合は最新の
   #216 の base/head に対応することを照合する。これは既存の統合停止を解く処置であり、
   原因差分の除去や後続生成の取り込み完了とは数えない。
   設定変更がある場合は最新 preview に取り消し差分を反映し、必要な競合解消と
   同じ候補の検証後に qdev 設定を統合する。親が対応する生成 SHA を取り込む際の
   競合も処置し、同じ候補の差分と保持契約を再確認する。設定変更がなければ対応する
   親の生成結果へ取り消し候補を統合する。`next` 向け PR だけで既存 conflict PR も
   自動解決するとは仮定しない。
6. 継続する各 qdev PR を最新の親へ追従させ、head/base 両 preview を再生成して
   統合 SHA と各 conflict PR の処置完了を記録する。再発試験には今回衝突した resource
   登録や schema を変える差分を使う。既存の継続 PR で確認できなければ試験用 preview PR
   を作り、マージ・公開せず、結果を記録して閉じる。

完了条件は、対象の親・継続 preview の競合が解消し、原因の重複差分が取り除かれ、
表で決めた削除・改名が生成設定・SDK・CLI・文書・テストに一貫して反映され、
維持する機能と保護処理のテストが成功すること。旧名の alias と keywords / snapshots の
維持は要求しない。全手書き差分の排除や staging の必須チェック設定は、この限定した
修正の完了条件にしない。
対象ファイルの `git diff <採用生成SHA> <候補SHA> -- <対象ファイル>` を確認し、
記録した保持 hunk 以外に原因の重複差分が残っていないことを確認する。全対象 PR の
処置が完了し、最新版の head/base が統合され、同じ競合の open PR が残っていないことを確認する。
残した修正が将来別の生成変更と競合する可能性はあるため、「今後どんな更新でも
競合が絶対に起きない」とは保証しない。実際に再発した箇所を次の改善対象にする。
