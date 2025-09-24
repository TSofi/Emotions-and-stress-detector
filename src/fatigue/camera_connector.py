import cv2
import time
from config.constants import MAX_ATTEMPTS, WAIT_DELTA
import logging

class CameraConnector:
  def __init__(self, logger: logging.Logger, source = 0):
    self.logger = logger
    self.video_capture = cv2.VideoCapture(source)
    attempts = 0
    while not self.video_capture.isOpened() and attempts < MAX_ATTEMPTS:
      self.logger.warning(f'Attempt #{attempts} to open camera failed')
      time.sleep(WAIT_DELTA)
      attempts += 1
    self.logger.info(f'Camera was initialized with source {source}')

  def read_shot(self):
    connection_marker, frame = self.video_capture.read()
    if not connection_marker:
      self.logger.error('Could not get a shot')
      return None
    
    self.logger.info(f'Got frame of shape: {frame.shape}')
    return frame
  
  def close_session(self):
    self.video_capture.release()
    cv2.destroyAllWindows()
    self.logger.info('Camera session was closed')
  
