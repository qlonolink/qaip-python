# Stainless Python 生成器の制約調査（問い合わせ案の記録）

**2026-09-08 方針変更: この問い合わせは送信しない。** サポートに依存せず、
[原因差分の取り消しを優先する計画](stainless-self-managed-plan.md)で進める。
以下は当時の生成器の制約と再現結果を残すための記録。

手書き変更による継続的な生成 PR の競合をなくすため、既存 SDK の機能を設定へ
移しています。以下の点が、Python 生成領域の手書き patch を除去する妨げに
なっています。対応する設定か、生成器側の修正方法を確認したいです。

## 対象と再現結果

- Project: `qlonolink/qaip`、Python package: `qaip`。
- 設定 PR: https://github.com/qlonolink/qdev/pull/7737 （draft）。
- 初回入力 SHA: `aa7c6872d3fec0561ff292e7f010d0e799c4f7ae`。
- 初回 Python 生成 SHA: `dc63c9997f8244449be9f0d064a8bc5cb55cdcb5`。
- 成功した生成 job: https://github.com/qlonolink/qdev/actions/runs/34204140599
- head build: `bui_0cmtsekqz0000m26s69v4ahxn6`。
- 最新入力 SHA: `70404e5a219363c3b911821079701c21f0ee7f5c`、Python 生成 SHA:
  `591dd064625ada7fc670587a15e6200fe68566fe`。
- 最新生成にも同じ問題が残り、公開 wheel で成功する 75 契約ケースのうち
  再送抑止・SSE の 10 ケースが失敗しました。残り 65 件は成功しています。
- 手書き patch を持つ現在の SDK では以下のテストが成功し、上記純生成版では
  API key 再送抑止 2 件と SSE 4 件が失敗しました。multipart 2 件は生成設定で
  再現できました。ネットワークは HTTP モックで、実際のキー発行は行っていません。

## 1. method 単位の max_retries: 0

公式 config schema が受理する次の指定が、Python の同期・非同期 method の
request options に反映されません。

```yaml
resources:
  api_keys:
    methods:
      create:
        type: http
        endpoint: post /api-keys
        default_request_options:
          max_retries: 0
```

生成された method の `make_request_options(...)` に `max_retries` がなく、
HTTP モックが最初の応答に 500 と `x-should-retry: true` を返すと、2 回目の
POST が発生します。既存の SDK は method の `options["max_retries"] = 0` で
1 回だけ送信します。同じ問題を非冪等な `POST /query` でも確認しました。

全 method の retry を無効化すると、既存の読み取り API の挙動が変わるため、
対象 method だけの指定を生成できる必要があります。

## 2. SSE の空フレームと文字列型

次の SSE で、直前の `id` を保持した comment frame に対して `json.loads("")`
が呼ばれて失敗します。comment / keepalive を無視して有効なイベントを処理
する既存挙動を、同期・非同期の両方で維持したいです。

```text
id: 1
data: {"type":"RUN_STARTED"}

: keepalive

id: 2
data: {"type":"RUN_FINISHED"}

```

また、生成された `Stream[str]` / `AsyncStream[str]` が `sse.json()` の dict を
文字列型として処理し、strict response validation で失敗します。既存 SDK は
文字列 stream では `sse.data` をそのまま返します。これは通常の
`client.agent.stream_events(...)` からも再現します。

現在の回帰テスト: `tests/custom/test_sse_compat.py`。

## 3. API key の確定 409 と応答本文エラー

未公開の統合済み変更（SDK next `a0be5ba3cc960d449fe9d9022059a91816f8d180`）では、
有効期限付き API key 発行で `credential_already_created` 等の確定した 409 を
再試行せず、復旧に使う ID と元の例外を保持します。一般的な 409 の retry は
維持しています。応答本文の読み取りが失敗した場合にも例外を置き換えない
処理があります。

この差分を基盤の `_base_client.py` に残さず接続できる拡張点、または同等の
生成器対応があるか確認したいです。サーバーの `x-should-retry: false` だけで
本文エラーの保持も同等になるとは扱っていません。

回帰テスト: `tests/custom/sdk/test_api_key_phase5_contract.py`。

## 4. Python パッケージの独自 CLI entry point

現在の SDK は独立した `src/qaip/cli/**` と、`pyproject.toml` の次の設定で
`qaip` コマンドを提供しています。

```toml
[project.scripts]
qaip = "qaip.cli:main"
```

この entry point を生成設定で定義する方法、または生成と独自パッケージ設定の
所有範囲を分離する対応方法を確認したいです。`keep_files` の「ファイル削除を
防ぐ」という説明を、生成ファイルを上書きしない保証とは解釈していません。

## 5. staging の必須チェックを設定する権限

`stainless-sdks/qaip-python` の現在の権限は `maintain: true` / `admin: false`。
`GET /repos/stainless-sdks/qaip-python/rulesets` は、利用プランによる機能制限の
403 を返しました。手書き差分の再導入を拒否する境界チェックを必須化するため、
staging の管理者が設定できる強制方法を確認したいです。Stainless の正規の生成・
ミラー・release の取り込みは維持する必要があります。

## 既に生成できた項目

resource/method/model 定義、`custom_casings.api.initialism: false`、multipart
repeat、`custom: true` による独自 resource の client / wrapper 登録、SDK 専用
schema からの公開型生成、`x-stainless-override-schema` による query の 202 応答
の union 化は、実際の Python 出力で確認できています。

上記の未解決点を確認してから、既存の競合解消と手書き差分の cleanup を進めます。
