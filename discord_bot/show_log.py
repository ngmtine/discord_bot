import os

from util.split_message import split_message


# ログ表示
async def show_log(message):
    original_dir = os.getcwd()
    log_dir = os.path.join(original_dir, "log")
    log_path = os.path.join(log_dir, "bot.log")

    # デフォルトログ数
    num_lines = 10

    # ログ数の指定あるなら取得
    args = message.content[len("$log ") :].split()
    if args:
        try:
            num_lines = int(args[0])
        except:
            pass

    # ログファイルから最新のエントリを読み込む
    log_entries = read_last_lines_from_log(log_path, num_lines)
    responses = split_message(log_entries)

    # ログ空の場合
    if not responses or all(res.isspace() for res in responses):
        responses.extend(["log file empty"])

    # Discordにログを送信
    for res in responses:
        await message.channel.send(f"```{res}```")


# ログファイル読んで最新n行返す
def read_last_lines_from_log(file_name, num_lines):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return "".join(lines[-num_lines:])
    except FileNotFoundError:
        return "log file not found"
    except Exception as e:
        return str(e)
