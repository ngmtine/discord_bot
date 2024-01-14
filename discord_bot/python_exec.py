import io
import os
from contextlib import redirect_stdout

from util.log import log
from util.split_message import split_message


# python実行
async def python_exec(message):
    command_text = message.content[len("$py ") :]
    responses = []
    original_dir = os.getcwd()
    output_dir = os.path.join(original_dir, "output")

    try:
        # ディレクトリ作成
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            log(f"Created directory: {output_dir}", level="info")

        # 実行
        output = io.StringIO()
        with redirect_stdout(output):
            exec(command_text)

        # 実行結果を取得
        result = output.getvalue()

        # 整形
        if result:
            resultstr = split_message(f"PYTHON RESULT:\n{result}")
            responses.extend(f"```{i}```" for i in resultstr)
            log(f"STDOUT: {result}", level="info")

    # 実行時エラー
    except Exception as e:
        errorstrs = split_message(f"PYTHON EXECUTE ERROR:\n{str(e)}")
        responses.extend(f"```fix\n{i}```" for i in errorstrs)
        log(f"Execution error: {e}", level="error")

    # discordにメッセージ送信
    for res in responses:
        await message.channel.send(res)
    log("Message sent to Discord", level="info")
