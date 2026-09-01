# Changelog

## 0.14.0 (2026-09-01)

Full Changelog: [v0.13.1...v0.14.0](https://github.com/qlonolink/qaip-python/compare/v0.13.1...v0.14.0)

### Features

* agent runにOpenAI providerとBedrockのmodel族分岐を追加 ([53eeb27](https://github.com/qlonolink/qaip-python/commit/53eeb27a9d3370a1de9f5c30915ee0e796b065b1))
* Agent runのOpenTelemetry可観測性を実装 ([20ab013](https://github.com/qlonolink/qaip-python/commit/20ab013c37c10687615a1a4dd7152f46d07967ed))
* agent/runs へ X API の読み取りツールを追加する ([56b19f3](https://github.com/qlonolink/qaip-python/commit/56b19f32bf4755ba1f049208e093b1a84042118b))
* AGENTCORE の redaction 同時実行に dev-api 側の入場ゲートを入れる ([602aa0c](https://github.com/qlonolink/qaip-python/commit/602aa0c11d35cb32f01d3719e89971d7379788b7))
* AgentCore 実行モードで redaction を実行できるようにする ([ccbeb1c](https://github.com/qlonolink/qaip-python/commit/ccbeb1c44c926c332fe68c1166c12073d80fb475))
* Agent会話履歴の一覧・再開機能を実装 ([7727744](https://github.com/qlonolink/qaip-python/commit/7727744d754061e92e9e1616963349a59b8ce895))
* Agent実行を永続ストリーミング化し性能を改善 ([67dbe19](https://github.com/qlonolink/qaip-python/commit/67dbe19983043b74470a551e954d847b1da13e46))
* APIキー認可を細粒度scopeへ移行 ([c194880](https://github.com/qlonolink/qaip-python/commit/c1948804a397fe386232e25b8e6f414e8841e6c5))
* Chartmetric Agent toolsを実装 ([567cced](https://github.com/qlonolink/qaip-python/commit/567ccedbb92f5b0016b7bfb76fd70d080832f09d))
* completion のストリーミング応答に SSE (ag-ui イベント) を追加 ([4bedf00](https://github.com/qlonolink/qaip-python/commit/4bedf00cedd41127c1f831da3ef5edf8bcf2a13d))
* Grok X調査とAgent初回表示高速化基盤を実装 ([557ade1](https://github.com/qlonolink/qaip-python/commit/557ade1b1452bc8b932510afa901a98d8658407d))
* クロール raw API の高速取得と source 一覧取得を実装 ([180512b](https://github.com/qlonolink/qaip-python/commit/180512b0a12a8324b44475da0203f1d30f5fb738))
* クロール時のcanonical重複チェック無効化に対応 ([c619e0b](https://github.com/qlonolink/qaip-python/commit/c619e0b4544a2cb67fb62b91e6c0e1100f06acb7))
* テナント別Redactionポリシー管理を実装 ([fca1c12](https://github.com/qlonolink/qaip-python/commit/fca1c1227ee121d485b56f807c155b999fab002d))
* 外部provider境界のredactionを強化 ([b7a0c0d](https://github.com/qlonolink/qaip-python/commit/b7a0c0d5e5f2d3af3346e100c42debb9294675c6))
* 検索APIにsource_group_idフィルタを追加 ([a8bd963](https://github.com/qlonolink/qaip-python/commit/a8bd9639dc5332addd7dd2728d11eb93fbd3d11a))


### Chores

* **internal:** version bump ([804e99f](https://github.com/qlonolink/qaip-python/commit/804e99f35d4c5006b4e11cbe917cef2043bf8c87))

## 0.13.1 (2026-08-28)

Full Changelog: [v0.13.0...v0.13.1](https://github.com/qlonolink/qaip-python/compare/v0.13.0...v0.13.1)

## 0.13.0 (2026-08-24)

Full Changelog: [v0.12.0...v0.13.0](https://github.com/qlonolink/qaip-python/compare/v0.12.0...v0.13.0)

### Features

* テナント別Redactionポリシー管理を実装 ([d67202b](https://github.com/qlonolink/qaip-python/commit/d67202b9844915de99cf1c0f55d27db6de6a9c16))

## 0.12.0 (2026-07-29)

Full Changelog: [v0.11.0...v0.12.0](https://github.com/qlonolink/qaip-python/compare/v0.11.0...v0.12.0)

### Features

* **api:** metadata_filter を /completions・/agent/run・/extract にも公開する ([d0c0d3d](https://github.com/qlonolink/qaip-python/commit/d0c0d3d83150218882e3ae6b09da7af0c125c5ab))
* 外部LLM送信前のRedactionとリリースゲートを実装 ([f2eed0f](https://github.com/qlonolink/qaip-python/commit/f2eed0f0a83e9a6c8816a28c334c155dde12455f))


### Chores

* **internal:** codegen related update ([73ca51c](https://github.com/qlonolink/qaip-python/commit/73ca51c923485ff5f4707b4bbc40246ceb5af179))

## 0.11.0 (2026-07-13)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/qlonolink/qaip-python/compare/v0.10.0...v0.11.0)

### Features

* **app:** エージェント会話のスレッド一覧 (/agent/threads) ([7a0af5d](https://github.com/qlonolink/qaip-python/commit/7a0af5d0962e6776a636f4fd893143335989f46b))
* **app:** 会話履歴機能 (/completions サーバ側保存・分岐対応) ([d29d263](https://github.com/qlonolink/qaip-python/commit/d29d263fa7d764a67997de635b21260e86bbcd32))

## 0.10.0 (2026-07-06)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/qlonolink/qaip-python/compare/v0.9.0...v0.10.0)

### Features

* [codex] クロール原本ダウンロードAPIを実装 ([8d437a2](https://github.com/qlonolink/qaip-python/commit/8d437a27a54b14040b8e6fedcb993040e373bcbd))

## 0.9.0 (2026-07-03)

Full Changelog: [v0.8.2...v0.9.0](https://github.com/qlonolink/qaip-python/compare/v0.8.2...v0.9.0)

### Features

* **app:** Gemini grounding を completion / agent で feature flag + API パラメータ制御 ([d67cf3b](https://github.com/qlonolink/qaip-python/commit/d67cf3b3ba5d524695dc0335d07c400e9969d7e8))


### Bug Fixes

* **types:** avoid type-checker errors on params with additional properties ([cec2c33](https://github.com/qlonolink/qaip-python/commit/cec2c3325cc9fad4641174476b53622a6e1040ae))

## 0.8.2 (2026-06-22)

Full Changelog: [v0.8.1...v0.8.2](https://github.com/qlonolink/qaip-python/compare/v0.8.1...v0.8.2)

## 0.8.1 (2026-06-19)

Full Changelog: [v0.8.0...v0.8.1](https://github.com/qlonolink/qaip-python/compare/v0.8.0...v0.8.1)

## 0.8.0 (2026-06-19)

Full Changelog: [v0.7.1...v0.8.0](https://github.com/qlonolink/qaip-python/compare/v0.7.1...v0.8.0)

### Features

* **app:** /completions と /agent/run で参照する chunk 数の上限を指定可能にする ([3651c69](https://github.com/qlonolink/qaip-python/commit/3651c69152b9734cf0bd608667a344a85202b7ee))
* **app:** vectordb.retrieve に use_postfilter を追加し API でも指定可能にする ([#5465](https://github.com/qlonolink/qaip-python/issues/5465)) ([9937b0e](https://github.com/qlonolink/qaip-python/commit/9937b0e342d8d3e41b488e41040cfda514537761))
* **authz:** metadata_columns API + 直接 metadata_filter (row-level authz 再設計) ([a90cb49](https://github.com/qlonolink/qaip-python/commit/a90cb49a3e5bdb52e574c5166f1aa929f207a83e))
* **internal/types:** support eagerly validating pydantic iterators ([990e392](https://github.com/qlonolink/qaip-python/commit/990e3921e7a6affffb64ee85d78d7cbf3834145e))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([badf4be](https://github.com/qlonolink/qaip-python/commit/badf4bef6c0e8577be592be819bd23ea249714ec))

## 0.7.1 (2026-05-01)

Full Changelog: [v0.7.0...v0.7.1](https://github.com/qlonolink/qaip-python/compare/v0.7.0...v0.7.1)

## 0.7.0 (2026-05-01)

Full Changelog: [v0.6.1...v0.7.0](https://github.com/qlonolink/qaip-python/compare/v0.6.1...v0.7.0)

### Features

* agent/run Vertex AI (Gemini) 対応 ([ad6a73a](https://github.com/qlonolink/qaip-python/commit/ad6a73a8a06b1ce882911b275e87636ccce6604c))
* REST APIを呼び出すCLIを実装 ([#1](https://github.com/qlonolink/qaip-python/issues/1)) ([0806eb8](https://github.com/qlonolink/qaip-python/commit/0806eb859640d2f1260589dcaad2b7a04ab86bdc))
* support setting headers via env ([e1d2753](https://github.com/qlonolink/qaip-python/commit/e1d27538853dac86a2c4e84cb0b4a0d0397bd419))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([b93bd67](https://github.com/qlonolink/qaip-python/commit/b93bd672dd2e61a02cab4c9e8d839711732b040c))
* ensure file data are only sent as 1 parameter ([4134636](https://github.com/qlonolink/qaip-python/commit/41346366a3bdee4aeffb3b25a296b5d1f022fdc0))
* use correct field name format for multipart file arrays ([f0e6727](https://github.com/qlonolink/qaip-python/commit/f0e6727d6270234127ec1a8493bb60af180bea3b))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([9b5c3c7](https://github.com/qlonolink/qaip-python/commit/9b5c3c72fab91305f312fd43cd8465e37e2e23c7))


### Chores

* **internal:** more robust bootstrap script ([206ce24](https://github.com/qlonolink/qaip-python/commit/206ce24edeff21560021c55680d1d567f008f59e))
* **internal:** reformat pyproject.toml ([50fbf80](https://github.com/qlonolink/qaip-python/commit/50fbf8063788d79a178c124cc1ff763987d7838e))

## 0.6.1 (2026-04-03)

Full Changelog: [v0.6.0...v0.6.1](https://github.com/qlonolink/qaip-python/compare/v0.6.0...v0.6.1)

### Bug Fixes

* /contents/{id} で UUID形式でないIDに400を返す ([2a35e53](https://github.com/qlonolink/qaip-python/commit/2a35e536b923ce43457131b461459f7001288f68))

## 0.6.0 (2026-04-02)

Full Changelog: [v0.5.1...v0.6.0](https://github.com/qlonolink/qaip-python/compare/v0.5.1...v0.6.0)

### Features

* stainless.ymlにOpenAPIスペックの全リソース・モデルを追加 ([bb33a95](https://github.com/qlonolink/qaip-python/commit/bb33a95bb6305fcdae0c672a3cccd849a51ff2b4))

## 0.5.1 (2026-04-02)

Full Changelog: [v0.5.0...v0.5.1](https://github.com/qlonolink/qaip-python/compare/v0.5.0...v0.5.1)

## 0.5.0 (2026-04-02)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/qlonolink/qaip-python/compare/v0.4.0...v0.5.0)

### Features

* search/extract/completion APIにchunk_metadataフィルタを追加 ([af80fac](https://github.com/qlonolink/qaip-python/commit/af80fac909b5ddf9c8bb58a708146e9b1a032ca0))

## 0.4.0 (2026-04-01)

Full Changelog: [v0.3.1...v0.4.0](https://github.com/qlonolink/qaip-python/compare/v0.3.1...v0.4.0)

### Features

* `tag_filter_mode` パラメータを追加し、タグのAND/OR検索を選択可能に ([d03f9f5](https://github.com/qlonolink/qaip-python/commit/d03f9f570b2984b37b0fdf528a833367e5fd6c46))
* Add Data Source Tagging API ([3d34747](https://github.com/qlonolink/qaip-python/commit/3d3474732be68754be467e8f773b8be77901c268))
* Add datetime metadata type support across all components ([563faa9](https://github.com/qlonolink/qaip-python/commit/563faa94d314b1f903164bc5607a68d5e890edfe))
* Add JSONL support ([ee35d64](https://github.com/qlonolink/qaip-python/commit/ee35d6423f5d16742a7f3ef552a3ad437879acf6))
* completionsのapiのcitationsの型をsearchでのレスポンスに合わせる ([8bfac4d](https://github.com/qlonolink/qaip-python/commit/8bfac4dce065ef83ba8925612de9fe15d414b89e))
* **internal:** implement indices array format for query and form serialization ([08d5663](https://github.com/qlonolink/qaip-python/commit/08d56631deacb1b58f7b13672612147a66388cd7))
* ToolCallEventをagentに追加 ([8fedc79](https://github.com/qlonolink/qaip-python/commit/8fedc792bd446432a1deb234a7b6499b75f83118))
* メタデータフィルタリング機能を実装 ([9c4ced4](https://github.com/qlonolink/qaip-python/commit/9c4ced45ef62695947f154a0f40b9bbcedd6161a))
* メタデータ機能: source_metadatas を使ったメタデータフィルタリング機能の追加 ([098f7dd](https://github.com/qlonolink/qaip-python/commit/098f7dd49b8b6468dc4d4597fcff278479c91da4))
* 動画対応 ([518d595](https://github.com/qlonolink/qaip-python/commit/518d595293f42079d414acf27b21eddf4e6c46b8))
* 抽出に追加プロンプトと関連情報を追加 ([8b67351](https://github.com/qlonolink/qaip-python/commit/8b67351ef486dee79a40ee70692e4913d1a15b2e))
* 画像取り込み対応 ([d1c16b5](https://github.com/qlonolink/qaip-python/commit/d1c16b5f29760a37bc30eab04d5299d189210747))
* 音声・動画・画像ファイルのクレジット計測コードを追加 ([ec64282](https://github.com/qlonolink/qaip-python/commit/ec64282a422b1b3eb61737666a9835c3c997caa4))
* 音声対応 ([f1799ff](https://github.com/qlonolink/qaip-python/commit/f1799ff3250eaa57e5b6c8cba10b496989bac6ee))


### Bug Fixes

* compat with Python 3.14 ([4937711](https://github.com/qlonolink/qaip-python/commit/49377119cb706e912e31cdc1a86aefb356380946))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([810e090](https://github.com/qlonolink/qaip-python/commit/810e090fabb8fd846ef8738071fffabf4dd2f592))
* ensure streams are always closed ([1967c03](https://github.com/qlonolink/qaip-python/commit/1967c035dac16cbf2c3e8af571f083387426ed07))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([28d4993](https://github.com/qlonolink/qaip-python/commit/28d49939d008a0c0e378c336d14ea4e9919dc750))
* use async_to_httpx_files in patch method ([4167338](https://github.com/qlonolink/qaip-python/commit/41673381736ff50417f97bddf308f69479b4b948))


### Chores

* add Python 3.14 classifier and testing ([dda25ea](https://github.com/qlonolink/qaip-python/commit/dda25ead17c5453cf1c456000355fa5f7b45e75e))
* **ci:** skip uploading artifacts on stainless-internal branches ([c4ea1e7](https://github.com/qlonolink/qaip-python/commit/c4ea1e7f44e014b55e121fb5c76b8e2fbe7cb083))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([018f8e5](https://github.com/qlonolink/qaip-python/commit/018f8e5e5e075d702420252c9f91f4a922cc7d84))
* **docs:** use environment variables for authentication in code snippets ([6ed6feb](https://github.com/qlonolink/qaip-python/commit/6ed6feb90f388b82d14ceafad8c35745abac1046))
* **internal:** add `--fix` argument to lint script ([3a5c382](https://github.com/qlonolink/qaip-python/commit/3a5c382c5063021991d2482106055b375a441505))
* **internal:** add missing files argument to base client ([9ad0273](https://github.com/qlonolink/qaip-python/commit/9ad0273556f0d925f32ef2674351a41aaea3034d))
* **internal:** codegen related update ([fe1139d](https://github.com/qlonolink/qaip-python/commit/fe1139d51336737906d9518cceb3b2856e97915c))
* **internal:** codegen related update ([977f85c](https://github.com/qlonolink/qaip-python/commit/977f85c9f331e7c8e0dbf631157aeb0b5e05d57a))
* **internal:** codegen related update ([7945faf](https://github.com/qlonolink/qaip-python/commit/7945fafe5f12bcce32d91bc58172f7eaf7278f5f))
* **internal:** codegen related update ([9ac2644](https://github.com/qlonolink/qaip-python/commit/9ac26448812e1dc902194addded3904b0fe10b7e))
* **internal:** codegen related update ([3d423f1](https://github.com/qlonolink/qaip-python/commit/3d423f105f3e1637ed234c13ab3f1e60f1331bc8))
* **internal:** codegen related update ([a2251c2](https://github.com/qlonolink/qaip-python/commit/a2251c275d1fe78388d031595537db2489342305))
* **internal:** codegen related update ([ba1e23e](https://github.com/qlonolink/qaip-python/commit/ba1e23ea9baea1152fc1ac08a423b83b1324e495))
* **internal:** codegen related update ([3fc4541](https://github.com/qlonolink/qaip-python/commit/3fc45415ded41a7fc83bae50f9effe8c7b786990))
* **internal:** codegen related update ([8d92965](https://github.com/qlonolink/qaip-python/commit/8d929655c251d0b2d82ecfbb05bc44f7277f3235))
* **internal:** codegen related update ([9bd5380](https://github.com/qlonolink/qaip-python/commit/9bd5380007a40573a1e90491307bb51051b0bd0e))
* **internal:** grammar fix (it's -&gt; its) ([c8b869e](https://github.com/qlonolink/qaip-python/commit/c8b869ee4399a123ef732bab6e880e4b782dab48))
* **package:** drop Python 3.8 support ([3ccaf84](https://github.com/qlonolink/qaip-python/commit/3ccaf848a9e6d84a4f7c502d932a0a1f5a99bec2))
* speedup initial import ([6299faa](https://github.com/qlonolink/qaip-python/commit/6299faa3a93c12f12e53aab8a0cab2e209ceeb93))
* update lockfile ([a430f51](https://github.com/qlonolink/qaip-python/commit/a430f51f8da21b08341dbbfbc5afc86117f63bdc))

## 0.3.1 (2025-10-31)

Full Changelog: [v0.3.0...v0.3.1](https://github.com/qlonolink/qaip-python/compare/v0.3.0...v0.3.1)

### Bug Fixes

* **client:** close streams without requiring full consumption ([20eb525](https://github.com/qlonolink/qaip-python/commit/20eb525aa186bc0bd1c12d9fd48ca477ecf846ef))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([291cb64](https://github.com/qlonolink/qaip-python/commit/291cb64e32b4798ef98194dc90fd05100777a1ff))

## 0.3.0 (2025-10-23)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/qlonolink/qaip-python/compare/v0.2.0...v0.3.0)

### Features

* stainless に /tags を追加 ([eb689aa](https://github.com/qlonolink/qaip-python/commit/eb689aa7c219222aefb89baacc0bcdeae9b10ce0))

## 0.2.0 (2025-10-22)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/qlonolink/qaip-python/compare/v0.1.0...v0.2.0)

### Features

* API のレスポンスの ID を削除 ([532767b](https://github.com/qlonolink/qaip-python/commit/532767b6da7972c95b3341eb8c74433f151c8cf7))
* StainlessによるPyPI自動公開を有効化 ([24ef918](https://github.com/qlonolink/qaip-python/commit/24ef918357585d800c8b68234a8c1f8572f73f73))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([909d5a8](https://github.com/qlonolink/qaip-python/commit/909d5a88674ab296581ae3ea892322c241e38cb6))
* **internal:** detect missing future annotations with ruff ([604af60](https://github.com/qlonolink/qaip-python/commit/604af603823ab09c30f4d9cbf89172c987664d95))

## 0.1.0 (2025-09-25)

Full Changelog: [v0.0.2...v0.1.0](https://github.com/qlonolink/qaip-python/compare/v0.0.2...v0.1.0)

### Features

* devapiの処理に対する無料プランクレジット超過時の対応を追加 ([ba10f24](https://github.com/qlonolink/qaip-python/commit/ba10f24facb31aef87202367c950b13fb731397f))
* stainless.ymlを更新 ([fe86270](https://github.com/qlonolink/qaip-python/commit/fe862705d99e666ccb19f0cddfa4fe05c57827a1))

## 0.0.2 (2025-09-22)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/qlonolink/qaip-python/compare/v0.0.1...v0.0.2)

### Chores

* **config:** update docs/contact and set production base URL to https://developer.qaip.com/v1 ([1e427fd](https://github.com/qlonolink/qaip-python/commit/1e427fd9e884a9dfee86a6341a0ebe845dfb4468))
* do not install brew dependencies in ./scripts/bootstrap by default ([d2da491](https://github.com/qlonolink/qaip-python/commit/d2da4912ea2d07dbce045f79365b2228f93fd77d))
* update SDK settings ([c91cf5a](https://github.com/qlonolink/qaip-python/commit/c91cf5a6d4a15b592d2abd54e1b6f43d87181e88))
