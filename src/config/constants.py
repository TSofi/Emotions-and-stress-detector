from pathlib import Path
import torch

MAX_ATTEMPTS = 5
WAIT_DELTA = 1

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
MOUTH = [78, 81, 13, 311, 308, 402, 14, 17, 312, 318, 324, 308, 13, 14, 17, 18, 312, 317, 318, 402] 

BASE_DIR = Path(__file__).resolve().parent.parent.parent
REPORTS_DIR = BASE_DIR/'reports'
LOGS_DIR = REPORTS_DIR/'logs'
MODEL_DIR = BASE_DIR/'model'
LOG_FILE_FATIGUE = 'fatigue.log'
LOG_FILE_EMOTIONS = 'emotions.log'
MAIN_LOGGER = 'Detector'

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MODEL_PATH = MODEL_DIR/'emotion_model.pth'
CLASSES = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']