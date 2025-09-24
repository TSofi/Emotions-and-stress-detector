import logging

class Analyzer:
  def __init__(self, eye_metrics, mouth_metrics, logger: logging.Logger):
    self.eye_metrics = eye_metrics
    self.mouth_metrics = mouth_metrics
    self.blink_count = 0
    self.yawn_count = 0
    self.blinking = False
    self.yawning = False
    self.logger = logger
    self.logger.info("Analyzer initialized")

  def update(self, landmarks):
    ear = self.eye_metrics.calculate_ear(landmarks)
    mar = self.mouth_metrics.calculate_mar(landmarks)

    if self.eye_metrics.is_eye_closed(ear):
      if not self.blinking:
        self.blinking = True
        self.blink_count += 1
        self.logger.info(f"Total blinks: {self.blink_count}")
      else:
        self.blinking = False

    if self.mouth_metrics.is_yawning(mar):
      if not self.yawning:
        self.yawning = True
        self.yawn_count += 1
        self.logger.info(f"Total yawns: {self.yawn_count}")
      else:
        self.yawning = False

  def get_fatigue_score(self):
    score = self.blink_count + self.yawn_count
    self.logger.info(f"Current fatigue score: {score}")
    return score