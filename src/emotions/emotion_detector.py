import cv2
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import os
import logging 
from config.constants import CLASSES, MODEL_PATH, DEVICE

class EmotionDetector:
  def __init__(self, logger: logging.Logger):
    self.logger = logger
    self.model = self._initialize_model()
    self.transform = self._get_transform()
    self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    self.classes = CLASSES
    self.logger.info("Emotion detector initialized")

  def _initialize_model(self):
    model = models.resnet18(weights="IMAGENET1K_V1")
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 7)
    model = model.to(DEVICE)
    model.eval()
        
    if os.path.exists(MODEL_PATH):
      self.logger.info(f"Loading model from {MODEL_PATH}")
      model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    else:
      self.logger.error(f"Model file not found at {MODEL_PATH}")
      raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
            
    return model

  def _get_transform(self):
    return transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor(), transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])])

  def detect_emotions_on_webcam(self):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
      self.logger.error("Failed to access camera")
      return

    while True:
      ret, frame = cap.read()
      if not ret:
        self.logger.warning("Failed to receive frame from camera")
        break

      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
      self.logger.debug(f"Detected {len(faces)} faces")

      for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        face_pil = Image.fromarray(cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB))
        face_tensor = self.transform(face_pil).unsqueeze(0).to(DEVICE)

        with torch.no_grad():
          output = self.model(face_tensor)
          _, pred = torch.max(output, 1)
          emotion = self.classes[pred.item()]
                
        self.logger.info(f"Detected emotion: {emotion}")
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_x = x
        text_y = y - 10 if y - 10 > 10 else y + 10
        (text_width, text_height) = cv2.getTextSize(emotion, font, 1, 2)[0]
        box_coords = ((text_x, text_y + 2), (text_x + text_width + 2, text_y - text_height - 2))
        cv2.rectangle(frame, box_coords[0], box_coords[1], (255, 105, 180), cv2.FILLED)
        cv2.putText(frame, emotion, (text_x, text_y), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
            
      cv2.imshow('Face Emotion Detection', frame)
      if cv2.waitKey(1) & 0xFF == 27:
        self.logger.info("ESC key pressed")
        break

    cap.release()
    cv2.destroyAllWindows()
    self.logger.info("Camera and windows released")
