import math
import logging

class Eye:
  def __init__(self, left_eye_indices, right_eye_indices, logger: logging.Logger, threshold=0.25):
    self.left_eye_indices = left_eye_indices
    self.right_eye_indices = right_eye_indices
    self.threshold = threshold
    self.logger = logger
    self.logger.info("EyeMetrics initialized")

  def euclidean_distance(self, point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.hypot(x2 - x1, y2 - y1)

  def calculate_ear(self, landmarks):
    def eye_aspect_ratio(eye_points):
      A = self.euclidean_distance(eye_points[1], eye_points[5])
      B = self.euclidean_distance(eye_points[2], eye_points[4])
      C = self.euclidean_distance(eye_points[0], eye_points[3])
      ear = (A + B) / (2.0 * C)
      return ear

    left_eye = [(landmarks.landmark[i].x, landmarks.landmark[i].y) for i in self.left_eye_indices]
    right_eye = [(landmarks.landmark[i].x, landmarks.landmark[i].y) for i in self.right_eye_indices]

    left_ear = eye_aspect_ratio(left_eye)
    right_ear = eye_aspect_ratio(right_eye)
    ear_avg = (left_ear + right_ear) / 2.0

    self.logger.info(f"Left EAR: {left_ear:.2f}, Right EAR: {right_ear:.2f}, Avg EAR: {ear_avg:.2f}")
    return ear_avg

  def is_eye_closed(self, ear):
    closed = ear < self.threshold
    self.logger.info(f"Eye closed: {closed} (EAR={ear:.2f}, Threshold={self.threshold})")
    return closed
