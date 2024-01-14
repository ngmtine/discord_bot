import os
import subprocess

from util.is_command_available import is_command_available
from util.log import log
from util.split_message import split_message


# js実行
async def javascript_exec(message):
    command_text = message.content[len("$js ") :]
    responses = []
    original_dir = os.getcwd()
    output_dir = os.path.join(original_dir, "output")
    jsfile_apspath = os.path.join(output_dir, "temp.js")

    try:
        # node実行可能か確認
        is_node_available = is_command_available("node")
        if not is_node_available:
            raise RuntimeError("Node.js is not available on this system.")

        # jsコードを一時ファイルに保存
        with open(jsfile_apspath, "w") as file:
            file.write(command_text)

        # 実行
        process = subprocess.run(["node", jsfile_apspath], shell=False, text=True, capture_output=True, cwd=output_dir)
        stdout = process.stdout.strip()
        stderr = process.stderr.strip()

        # 出力を整形
        if stdout:
            stdouts = split_message(f"STDOUT:\n{stdout}")
            responses.extend(f"```{i}```" for i in stdouts)
            log(f"STDOUT: {stdout}", level="info")
        if stderr:
            stderrs = split_message(f"STDERR:\n{stderr}")
            responses.extend(f"```fix\n{i}```" for i in stderrs)
            log(f"STDERR: {stderr}", level="error")

        # レスポンス空の場合
        if not responses or all(res.isspace() for res in responses):
            responses.extend(["```Execution completed successfully, but the result is empty```"])

    # node使用不可エラー
    except RuntimeError as e:
        errorstrs = split_message(f"JAVASCRIPT EXECUTE ERROR:\n{str(e)}")
        responses.extend(f"```fix\n{i}```" for i in errorstrs)
        log(f"Execution error: {e}", level="error")

    # 実行時エラー
    except Exception as e:
        errorstrs = split_message(f"JAVASCRIPT EXECUTE ERROR:\n{str(e)}")
        responses.extend(f"```fix\n{i}```" for i in errorstrs)
        log(f"Execution error: {e}", level="error")

    # discordにメッセージ送信
    for res in responses:
        await message.channel.send(res)
    log("Message sent to Discord", level="info")

    # 後始末
    os.remove(jsfile_apspath)
