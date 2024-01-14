# Discord Shell Executor Bot

この Discord bot は、指定されたシェルコマンドを実行し、その結果を Discord チャンネルに送信します  
discord との通信は[discord.py](https://discordpy.readthedocs.io/ja/latest/index.html#)を使用しています  
主な機能は以下の通りです

```
$hello 疎通確認用
$sh [コマンド] 指定されたシェルコマンドを実行します
$sh [ログ数] 指定された行数のログを表示します 無指定で最新10行
$restart 再起動（ただしメインプロセスが死んでた場合はそもそもコマンド受け取れないのでこのコマンドはあまり意味がない！！）
```

# セットアップ

discord の bot を作成します  
[参考：Bot アカウント作成](https://discordpy.readthedocs.io/ja/latest/discord.html)  
Message Content Intent を有効にしておいてください

env.py を編集する

```py
TOKEN = "your-discord-bot-token"
```

# 実行

```sh
poetry install
poetry shell
python discord_bot
```

もしくは poetry を使用しない場合

```sh
pip install discord.py
python ./discord_bot/main.py
```

# 注意事項

この bot はシェルコマンドを実行する能力を持っています  
セキュリティ上の理由から、信頼できるユーザーのみがこれらのコマンドを使用できるように制限することを強く推奨します  
特に、`$sh`は`subprocess(shell=True)`で実行するので、コマンドインジェクションのリスクがあります

# todo

sudo とか y/n とかの対話機能（現在は main.py を実行した端末が応答を待ち受けます）
