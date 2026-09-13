# qaip CLI

`qaip api` でAPIを呼び出し、`qaip schema` で操作と引数を確認できます。
CLIは `qaip-cli`、Python SDKは `qaip` として個別に配布します。

```sh
uv tool install qaip-cli
qaip --version
qaip schema local-file-groups
```

旧SDKに同梱されたCLIを `uv tool install qaip` で入れていた場合は、
`uv tool uninstall qaip` を実行してから `qaip-cli` をインストールしてください。
アプリケーション側でSDKを利用する場合は、引き続き `pip install qaip` を使います。

認証情報は `QAIP_API_KEY`、接続先は `QAIP_BASE_URL` で指定できます。
`schema` と `--dry-run` は認証情報なしで実行できます。

## チャンク削除

```sh
qaip api local-file-groups.start_chunk_deletion \
  --id "$GROUP_ID" --text-contains '削除対象の文字列' --dry-run
qaip api local-file-groups.start_chunk_deletion \
  --id "$GROUP_ID" --text-contains '削除対象の文字列' --yes
qaip api local-file-groups.retrieve_chunk_deletion \
  --id "$GROUP_ID" --chunk-deletion-id "$JOB_ID"
```

`--text-contains` を繰り返すと、いずれかの文字列を含むチャンクを削除します。
文字列内のカンマもそのまま扱います。空文字列は受け付けません。

## 一括削除

```sh
qaip api local-file-groups.start_bulk_deletion \
  --source-group-id "$GROUP_ID_1" --source-group-id "$GROUP_ID_2" --dry-run
qaip api local-file-groups.start_bulk_deletion \
  --source-group-id "$GROUP_ID_1" --source-group-id "$GROUP_ID_2" --yes
qaip api local-file-groups.retrieve_bulk_deletion --bulk-deletion-id "$JOB_ID"
```

開始応答の `accepted_count` は受付件数です。削除完了はジョブの `status`、
`deleted_count`、`remaining_source_group_ids` で確認してください。
全件が拒否された場合はジョブIDが返らず、ジョブも作成されません。
`remaining_truncated` が `true` の場合は、応答の `remaining_cursor` を
`retrieve_bulk_deletion --after` に渡して残りを取得できます。

開始操作は結果を返して終了し、自動でポーリングや再試行を行いません。
通信エラー時は実際の削除状況を確認してから再実行してください。

開始操作は `--json @request.json` または `--json -` にも対応し、JSON側の値を
個別フラグより優先します。本文はチャンク削除なら `text_contains`、
一括削除なら `source_group_ids` だけを受け付けます。

## 開発

このディレクトリのコードはPython SDKの生成物から独立しています。
SDKの `src/qaip` を変更せず、CLIとテストをここで管理します。
対応SDKをインストールしてから `pytest tests` で検証します。
