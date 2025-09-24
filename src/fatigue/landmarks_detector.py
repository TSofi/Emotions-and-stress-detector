import mediapipe as mp
import cv2

class LandmarksDetector:
  def __init__(self):
    self.model = mp.solutions.face_mesh
    self.face_mesh = self.model.FaceMesh(refine_landmarks=True)
    self.picture = mp.solutions.drawing_utils
    self.drawing_specture = self.picture.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1)

  def detect_landmarks(self, frame):
    shot_in_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    list_of_faces_and_landmarks = self.face_mesh.process(shot_in_rgb)
    if list_of_faces_and_landmarks.multi_face_landmarks:
      return list_of_faces_and_landmarks.multi_face_landmarks[0]
    
    return None
  
  def draw_landmarks(self, frame, landmarks):
    for landmark in landmarks:
      self.picture.draw_landmarks(image=frame, landmark_list=landmark, connections=self.mp_face_mesh.FACEMESH_TESSELATION, landmark_drawing_spec=self.drawing_spec, connection_drawing_spec=self.drawing_spec)