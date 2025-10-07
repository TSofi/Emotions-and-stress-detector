Face Emotion and Fatigue Detection Prototype

This project is a prototype system for real-time facial emotion recognition and fatigue analysis using computer vision. It combines a deep learning model for emotion classification with facial landmark tracking for fatigue-related cues.

Features

Emotion Recognition:

Trained a ResNet18 model on the FER-2013 dataset (RGB images, batch size 64, Adam optimizer, CrossEntropy loss).
Trained for 20 epochs, achieving ~65% test accuracy.
Integrated with the main detection script for real-time emotion recognition.
Note: Some emotions, such as "Disgust", are less accurately recognized due to dataset limitations.
Model and original code available on https://github.com/TSofi
In this project, the model is used in a simplified and integrated form.

Fatigue Detection via Facial Landmarks:

Used Mediapipe for real-time detection of 468 facial landmarks.
Focused on eye and mouth movements, which are indicators of fatigue or discomfort:
Eyes: blink frequency, eyelid aperture (EAR), gaze dynamics.
Mouth: yawning, muscle tension (MAR).
Prototype tested with live webcam input.


Notes
This is a first working prototype; improvements in emotion recognition and fatigue metrics are planned.
The code can be extended to combine both components seamlessly in one unified application.

Authors
Sofiia Tretiak – Model training; full code and model hosted on GitHub
Vitaliya Rabchynskaya – Mediapipe-based fatigue detection, real-time facial landmark tracking.
