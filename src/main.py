from fatigue.main_fatigue import main_fatigue
from logger.logger_config import LoggerConfig
from config.constants import MAIN_LOGGER, LOG_FILE_FATIGUE, LOG_FILE_EMOTIONS
from emotions.main_emotions import main_emotions
import logging

if __name__ == '__main__':
  print('Hi, nice to see you in app for dtecting emotions and stress \n\nIf you want to detect your emotions enter 1 \nIf you want to detect signs of stress enter 2 \nIf you want to exit enter whatever')
  choice = input('\nYour choice: ')
  if choice == '1':
    logger_1 = LoggerConfig.initialize_logger(MAIN_LOGGER, LOG_FILE_EMOTIONS, logging.INFO)
    logger_1.info('Detector started')
    main_emotions(logger_1)
  elif choice == '2':
    logger_2 = LoggerConfig.initialize_logger(MAIN_LOGGER, LOG_FILE_FATIGUE, logging.INFO)
    logger_2.info('Detector started')
    main_fatigue(logger_2)

  