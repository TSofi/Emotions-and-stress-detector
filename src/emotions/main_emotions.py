import logging
from emotions.emotion_detector import EmotionDetector

def main_emotions(logger: logging.Logger):
  try:
    logger.info("Starting emotion detection from webcam")
    detector = EmotionDetector(logger)
    detector.detect_emotions_on_webcam()

  except FileNotFoundError as e:
    logger.error(f"Error: Model file not found. {e}")
  except Exception as e:
    logger.critical(f"An unhandled error occurred: {e}", exc_info=True)
