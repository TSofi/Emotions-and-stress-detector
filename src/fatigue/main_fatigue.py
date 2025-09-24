from fatigue.landmarks_detector import LandmarksDetector
from fatigue.camera_connector import CameraConnector
from fatigue.manager import Manager
from fatigue.eyes import Eye
from fatigue.mouth import Mouth
from config.constants import LEFT_EYE, RIGHT_EYE, MOUTH
import logging

def main_fatigue(logger: logging.Logger):
  connector = CameraConnector(logger)
  detector = LandmarksDetector()
  eye = Eye(LEFT_EYE, RIGHT_EYE, logger)
  mouth = Mouth(MOUTH, logger)
  manager = Manager(connector, detector, eye, mouth, logger)

  manager.draw_landmarks()
  manager.close()
