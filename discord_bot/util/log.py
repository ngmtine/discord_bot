import logging
import os
from logging.handlers import RotatingFileHandler

# ログの設定
repo_dir = os.getcwd()
log_dir = os.path.join(repo_dir, "log")
log_file = "bot.log"

# ディレクトリ作成
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# ログのフォーマット設定
log_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# ログレベルの設定
log_level = logging.INFO

# ロガーの設定
logger = logging.getLogger("discord")
logger.setLevel(log_level)

# ファイルハンドラの設定
file_handler = RotatingFileHandler(filename=os.path.join(log_dir, log_file), maxBytes=5 * 1024 * 1024, backupCount=5)  # 5 MB
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)

# コンソールハンドラの設定（オプション）
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)


def log(message, level=log_level):
    """
    ログ出力

    :param message: メッセージ
    :param level: ログレベル（'debug' | 'info' | 'warning' | 'error' | 'critical'）
    """
    if level == "debug":
        logger.debug(message)
    elif level == "info":
        logger.info(message)
    elif level == "warning":
        logger.warning(message)
    elif level == "error":
        logger.error(message)
    elif level == "critical":
        logger.critical(message)
    else:
        print(f"{log_level}: undefined log_level!!")
        logger.info(message)
