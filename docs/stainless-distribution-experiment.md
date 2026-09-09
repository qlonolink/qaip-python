# 配布時に SDK を補正する案の検討記録

2026-09-08。ユーザーの「サポートはないので自力で解決する」という指示に基づく
方針変更。これは実証を伴う移行案であり、本番の生成・配布フローはまだ変更していない。
以前の調査書にある問い合わせ、生成器の修正待ち、staging 管理者への依頼は前提から外す。

**現在は保留案。** [原因差分の取り消しを優先する計画](stainless-self-managed-plan.md)に置き換えた。
以下の「採用」は当時の判断を記録したもので、配布フロー変更は進めない。

## 他の案との比較

| 案 | 判断 |
| --- | --- |
| 差分を小さな独立 wrapper / subclass に寄せる | 配布フローを変えずに済む有力な縮小策。ただし既存の `from qaip import Qaip` や型の import を維持する接続、明示的に渡される Stream 型、CLI の登録が必要。生成ファイルへの接続差分が残れば、競合をゼロにする構造にはならない |
| 共通の conflict 解消を rerere / bot で再利用する | 当面の負担軽減にはなる。生成内容の変化ごとの意味確認が必要で、手書き差分の再適用という原因は残る |
| 純生成入力から配布 SDK を自社で組み立てる | 採用案。公開 import を変えず、補正済みファイルを Stainless に戻さずに済む。配布・開発用の組み立て CI を自社で保守する必要がある |

`keep_files` に生成ファイルを列挙して上書きを止める案は採らない。
[公式説明](https://www.stainless.com/docs/sdks/configure/custom-code/)では、生成対象ファイルを
変更対象から除外する仕組みは提供されていない。

## 採用する構成

Stainless の生成結果と、利用者へ配布する SDK の組み立てを分ける。
生成設定で表現できる部分は qdev #7737 の設定へ移し、残りの補正は自社 CI が
毎回、固定した純生成 SHA のコピーへ機械的に適用する。

```text
OpenAPI + stainless.yml
          ↓ Stainless
固定した純生成 SHA ── 読み取り ──┐
                               ↓
qdev の互換処理・CLI・テスト → 隔離ディレクトリで SDK を組み立て
                               ↓
                         契約テスト・wheel/sdist 検証
                               ↓
                         同じ検証済み成果物を配布
```

**補正済みの生成ファイルを Stainless 管理のブランチへコミットしない。**
production の `main` / `next` に置くだけでも、Stainless のミラー処理で手書き差分に
戻る。したがって単なる「生成直後に patch して push」では解決にならない。
この制約は [Stainless の custom code とミラーの説明](https://www.stainless.com/docs/sdks/configure/custom-code/)
に基づく。本案の組み立て処理自体は、こちらで実装・保守する。

互換処理・CLI・手書きテストの管理先は、自社管理の qdev 内の専用ディレクトリ
`sdk/python/` を第一候補とする。生成側の pytest / 型検査が、補正前の SDK に対して
補正後の契約を要求しないよう、手書き契約テストも組み立て側で実行する。
現在の SDK #278 はテスト分離の第一段階であり、この新しい構成の導入 PR ではない。

keywords / snapshots の独立 resource は、`custom: true` の生成登録と組み合わせる。
純生成 SDK の通常 CI が import できるよう、生成器が所有しないこの 2 ファイルは
SDK 側にも残せる。組み立てで使う版との一致を manifest で検査する。
将来このパスを生成器が所有し始めた場合は、所有範囲検査で止めて移行する。

## 以前の未解決点への対処

| 項目 | 自社側での対応 | 今回の実証 |
| --- | --- | --- |
| API key / query 作成の再送抑止 | 同期・非同期の対象 `create` の request options にだけ `max_retries=0` を付加。全 API の再試行は無効化しない | 既存の再送抑止テスト成功 |
| SSE の空フレーム・文字列 | 生成されたイベントループの対象処理だけを構文で特定し、空フレームの無視と `str` の生データ処理を追加 | 通常の client と Stream / AsyncStream のテスト成功 |
| API key の確定 409 / 本文エラー | #259 の判定と同期・非同期の本文読み取り処理を、生成後の基盤へ限定的に挿入 | 復旧 ID、一般 409 の再試行、元の ReadTimeout を含む先行契約 27 件成功 |
| 公開名と #259 の大文字名 | 現在存在する import path に、同一オブジェクトを指す互換 alias を追加 | 既存の alias identity テスト成功 |
| CLI entry point | 組み立て先へ独立 CLI を配置し、配布用 `pyproject.toml` に `[project.scripts]` を追加 | wheel 隔離インストール後の CLI 起動・schema・dry-run 成功 |
| staging の必須チェック権限 | 自社管理の qdev / production の検証・配布経路で純生成との差分と互換性を必須確認する | 設計段階。staging の直接 push を技術的に禁止したとは扱わない |

サーバー側の仕様変更や、新しい REST API の公開には依存しない。
設定で生成できた resource/model、命名、multipart repeat はその設定を継続する。

## 組み立て処理の条件

- 毎回、新しいディレクトリに固定 SHA を展開する。前回の補正済み tree に重ねない。
- クラス・メソッド・HTTP method/path・対象構文・一致件数を検査する。対象がない、
  複数ある、生成器が同じ機能を実装済みなど、想定と違う場合は非ゼロ終了する。
  曖昧なテキスト置換や、自動的な ours/theirs 採用で通さない。
- 既存 runtime ファイル全体を古いコピーで置き換えない。生成器の他の修正を保持する。
  本実装では整形・コメントを保持する構文変換を使い、補正の実装・理由・契約テストを
  対応づけて管理する。今回の試作は AST の再出力であり、製品用ではない。
- 入力 OpenAPI/config hash、qdev SHA、生成 SHA、補正コード SHA、出力ファイル hash、
  パッケージ版を manifest に記録する。可変の preview ref だけで入力を指定しない。
- ビルドと配布を分ける。失敗時は配布せず、成功した同じ wheel/sdist を配布する。
  検証後に別のブランチや依存で再ビルドしない。
- `pyproject.toml`、`_version.py`、wheel metadata、release tag の版を一致させる。
  sdist にも組み立て済みソースを含め、sdist からの wheel 再ビルドを検証する。

これにより既知の手書き差分を原因とする Git 競合を除去する設計になる。
将来の生成器の大きな変更まで無保守で吸収する保証ではない。その場合は全 preview で
同じ競合を人手解消する代わりに、共通の変換を一度修正して再検証する。

## 移行手順

1. qdev に独立した組み立て処理、互換コード、CLI、契約テストを用意する。
   SDK #278 のテストも欠落・重複なく移す。SDK の純生成 CI と、配布 SDK の契約 CI
   を別々に合格させる。OpenAPI preview 完了後の生成 SHA を入力とし、補正だけの変更でも
   同じ検査を実行する。認証情報の取得・追加、配布の変更はまだ実施していない。
2. 公開 wheel と候補を比較し、既存の全契約、型検査、全テスト、CLI、wheel/sdist を
   検証する。今までの Git URL インストール・editable install・ソース直接実行の利用も
   確認し、同じ組み立てを使う開発コマンドと導線を用意する。Git checkout の素の生成物が
   配布物と同じ挙動だとは説明しない。Git からの互換インストールが必須なら、Stainless
   のミラー対象外の配布用ソースを用意するまで切り替えない。
3. 自社管理の配布経路を用意する。現在の `.github/workflows/publish-pypi.yml` は
   `bin/publish-pypi` でソースを直接 build/publish するので、そのまま使わない。
   production 側で旧 publisher を無効化し、新しい自社管理 workflow に一本化する。
   qdev の PR 検証ジョブには配布権限を与えず、release 対応の固定入力と合格済み成果物を
   配布ジョブへ渡す。二重公開、未補正 SDK の公開、staging からの公開を防ぐ。
   自動版付け・release 作成を継続する場合も、全公開経路がこのジョブを通ることを検証する。
4. 組み立て候補が合格してから qdev 設定を統合し、対応する純生成 SHA に生成領域を
   一度戻す。既存の #216 / #237 と継続 preview は調査書の SHA 照合・公式解消手順を
   用いて処置する。`generated` / 通常の `codegen/**` / `integrated/**` は直接編集しない。
   この移行で本番ブランチのマージや配布切り替えはまだ行っていない。
5. 継続中の qdev PR を親へ追従させて再生成する。さらに resource 登録・schema を実際に
   変更した preview で、親・各 preview の統合が手動解消なしに進むことを確認する。
6. 所有範囲一覧を更新し、生成領域への手書き差分がないことを自社 CI で検査する。
   staging に必須チェックを設定できなくても配布を止められる構成にする。ただし staging
   への直接変更を完全に防ぐ権限がないことは残るため、技術的な全経路強制と混同しない。

既存の競合を一度解消する作業は必要。問い合わせへの回答待ちは不要になる。

## 今回実証した範囲

- 入力生成 SHA: `591dd064625ada7fc670587a15e6200fe68566fe`。
- 互換実装の基準 SHA: `a0be5ba3cc960d449fe9d9022059a91816f8d180`。
- 再送抑止・SSE を含む公開契約 75 ケースと #259 の先行契約 27 ケースの
  **計 102 件が Pydantic v1 / v2 とも成功**。純生成候補で失敗していた 10 件も含む。
- 配布用に組み立てた wheel を別の仮想環境へインストールし、ソース checkout 外で
  `qaip --version`、`qaip schema`、`qaip api sources.list --dry-run`、互換 alias の import
  を確認。実 API は呼んでおらず、PyPI への公開もしていない。
- 独立して二度組み立て、308 ファイルの出力 hash が一致した。
- 生成所有 13 ファイルに補正を適用し、独立した CLI/resource 30 ファイルを加えた。
  これらの補正済み生成ファイルは隔離ディレクトリにのみ存在する。

試作スクリプトと当時の互換性テストは、保留案のローカル調査に用いた。
今回の配布・CIへの導入対象には含めない。keywords / snapshots を撤去する最新の
判断と検証結果は [現在の計画](stainless-self-managed-plan.md) に記録する。

ログは今回の一時作業ディレクトリ
`/private/tmp/qaip-stainless-migration-7ulafpdq/` の `self-managed-v1.txt`、
`self-managed-v2.txt`、`self-managed-candidate/proof-manifest.json` にある。
全 suite・全型の比較、sdist 再ビルド、負の変換 fixture、本番 CI、配布経路の切り替え、
新しい生成差分による競合再発試験は未実施。恒久対策全体の完了とは扱わない。
