#!/bin/fish

# リポジトリのディレクトリへ移動
cd /home/nag/ghq/github.com/ngmtine/discord_bot

# poetry環境をアクティブにする
source (poetry env info --path)/bin/activate.fish

# botを実行
python ./discord_bot/main.py
