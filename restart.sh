#!/bin/bash

# 環境変数取得
repository_path=$(python -c "from env import REPOSITORY_PATH; print(REPOSITORY_PATH)")

# リポジトリのディレクトリへ移動
cd "$repository_path"

# poetry環境をアクティブにする
source $(poetry env info --path)/bin/activate

# botを実行
python ./discord_bot/main.py
