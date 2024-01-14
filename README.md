# Discord Shell Executor Bot

この Discord bot は、指定されたシェルコマンドを実行し、その結果を Discord チャンネルに送信します  
主な機能は以下の通りです

```
$hello 疎通確認用
$sh [コマンド] 指定されたシェルコマンドを実行します
$restart 再起動（ただしメインプロセスが死んでた場合はそもそもコマンド受け取れないのでこのコマンドはあまり意味がない！！）
```

# セットアップ

```sh
pip install discord.py
```

env.py を編集する

```py
TOKEN = 'your-discord-bot-token'
```

# 実行

```sh
python main.py
```

# 注意事項

この bot はシェルコマンドを実行する能力を持っています  
セキュリティ上の理由から、信頼できるユーザーのみがこれらのコマンドを使用できるように制限することを強く推奨します  
特に、`$sh`は`subprocess(shell=True)`で実行するので、コマンドインジェクションのリスクがあります
