import cv2
from fatigue.camera_connector import CameraConnector
from fatigue.landmarks_detector import LandmarksDetector
from fatigue.eyes import Eye
from fatigue.mouth import Mouth
from fatigue.analizer import Analyzer
import logging

class Manager:
  def __init__(self, connector: CameraConnector, detector: LandmarksDetector, eye: Eye, mouth: Mouth, logger: logging.Logger):
    self.connector = connector
    self.detector = detector
    self.eye_metrics = eye
    self.mouth_metrics = mouth
    self.logger = logger
    self.fatigue_analyzer = Analyzer(self.eye_metrics, self.mouth_metrics, self.logger)
    self.logger.info("Manager initialized")

  def draw_landmarks(self):
    while True:
      frame = self.connector.read_shot()
      if frame is None:
        self.logger.error("No frame received")
        self.close()
        break

      landmarks = self.detector.detect_landmarks(frame)
      if landmarks:
        self.fatigue_analyzer.update(landmarks)

      self.fatigue_analyzer.get_fatigue_score()

      cv2.imshow('Fatigue Detector', frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        self.logger.info("Q pressed")
        break

  def close(self):
    if self.connector:
      self.connector.close_session()
