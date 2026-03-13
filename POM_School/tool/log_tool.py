import logging
import os,sys
from datetime import datetime


# 全局变量：标记是否已初始化根logger
LOGGER_INITIALIZED = False

def get_logger(name:str = __name__):

    """
    获取按模块命名的logger，避免全局冲突
    :param name: 建议传__name__（当前模块名），如base.base_page
    :return: 配置好的logger对象
    """

    global LOGGER_INITIALIZED

    # 获取项目根目录（utils的上上级目录）
    project_dir = os.path.dirname(os.path.dirname(__file__))
    log_dir = os.path.join(project_dir, 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir,exist_ok=True)

    # 日志文件名（按时间戳，只创建一次）
    log_file_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_file_path = os.path.join(log_dir,log_file_name)

    # 获取按模块命名的logger（关键：避免全局根logger冲突）
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not LOGGER_INITIALIZED:
        # 屏蔽第三方库的DEBUG日志
        logging.getLogger('selenium').setLevel(logging.WARNING)
        logging.getLogger('urllib3').setLevel(logging.WARNING)
        logging.getLogger("werkzeug").setLevel(logging.WARNING)

        # 设置格式，其中levelname后的8s代表占8位，用于对齐
        formatter = logging.Formatter("%(asctime)s %(name)20s %(levelname)8s %(lineno)s %(message)s",
                                      datefmt='%Y-%m-%d %H:%M:%S',
                                      )

        # 创建consoleHandler并设置格式、等级
        consoleHandler = logging.StreamHandler(sys.stdout) # 标准输出流
        consoleHandler.setLevel(logging.INFO)
        consoleHandler.setFormatter(formatter)

        # 创建fileHandler并设置格式、等级
        fileHandler = logging.FileHandler(
            filename=log_file_path,
            mode='a',
            encoding='utf-8',
        )
        fileHandler.setLevel(logging.DEBUG)
        fileHandler.setFormatter(formatter)

        # 添加到根logger（全局生效）
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        root_logger.addHandler(consoleHandler)
        root_logger.addHandler(fileHandler)

        # 标记已初始化，避免重复添加
        LOGGER_INITIALIZED = True

    return logger

# logger = get_logger()
# test_dir = os.path.dirname(os.path.dirname(__file__))
# logger.info(test_dir)
