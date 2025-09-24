import math
import logging

class Mouth:
  def __init__(self, mouth_indices, logger: logging.Logger, threshold=0.7):
    self.mouth_indices = mouth_indices
    self.threshold = threshold
    self.logger = logger
    self.logger.info("MouthMetrics initialized")

  def _euclidean_distance(self, point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.hypot(x2 - x1, y2 - y1)

  def calculate_mar(self, landmarks):
    def mouth_aspect_ratio(mouth_points):
      A = self._euclidean_distance(mouth_points[13], mouth_points[19])
      B = self._euclidean_distance(mouth_points[14], mouth_points[18])
      C = self._euclidean_distance(mouth_points[12], mouth_points[16])
      mar = (A + B) / (2.0 * C)
      return mar

    mouth = [(landmarks.landmark[i].x, landmarks.landmark[i].y) for i in self.mouth_indices]
    mar = mouth_aspect_ratio(mouth)
    self.logger.info(f"MAR: {mar:.2f}")
    return mar

  def is_yawning(self, mar):
    yawning = mar > self.threshold
    self.logger.info(f"Yawning: {yawning} (MAR={mar:.2f}, Threshold={self.threshold})")
    return yawning
