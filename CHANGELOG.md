# Changelog

## 0.6.2 (2026-04-11)

Full Changelog: [v0.6.1...v0.6.2](https://github.com/qlonolink/qaip-python/compare/v0.6.1...v0.6.2)

### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([b93bd67](https://github.com/qlonolink/qaip-python/commit/b93bd672dd2e61a02cab4c9e8d839711732b040c))
* ensure file data are only sent as 1 parameter ([4134636](https://github.com/qlonolink/qaip-python/commit/41346366a3bdee4aeffb3b25a296b5d1f022fdc0))

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
