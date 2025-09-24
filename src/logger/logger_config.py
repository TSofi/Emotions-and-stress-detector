import logging
from config.constants import LOGS_DIR
import os

class LoggerConfig:
  def initialize_logger(name, file, level):
    directory = LOGS_DIR
    if not os.path.exists(directory):
      os.mkdir(directory)
    filepath = os.path.join(directory, file)

    handler = logging.FileHandler(filepath, mode='w')
    formatter = logging.Formatter('%(asctime)s: %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger