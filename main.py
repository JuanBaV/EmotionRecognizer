import cv2
import json
import dataBase
import time
from deepface import DeepFace
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import numpy as np
from PIL import Image
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


intervalo_tiempo = 2
tiempo_anterior = time.time()
video = cv2.VideoCapture(0)
video.set(3,640)
video.set(4,480)
imgBackground=cv2.imread('Resources/Background.png')


diccionario_img = {
    "fear": "Images/miedo.png",
    "neutral": "Images/neutral.png",
    "sad": "Images/triste.png",
    "angry": "Images/enojado.png",
    "disgust": "Images/disgustado.png",
    "happy": "Images/feliz.png",
    "surprise": "Images/sorprendido.png",
}


emotion = None


while True:
    success, frame = video.read()
    imagen = None

    if emotion in diccionario_img:
        imagen = cv2.imread(diccionario_img[emotion])
    else:
        imagen = cv2.imread("Images/sinCara.png")       
    
    imgBackground[162:162+480, 55:55+640] = frame
    imgBackground[160:160+353, 870:870+400] = imagen

    cv2.imshow("background",imgBackground)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for x, y, w, h in face:
        img = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)

    try:
        tiempo_actual = time.time()
        
        if tiempo_actual - tiempo_anterior >= intervalo_tiempo:
            analisis = DeepFace.analyze(frame, actions=['emotion'])

            emotion=analisis[0]['dominant_emotion']
            
            print(emotion)

            dataBase.updateData(emotion)

            tiempo_anterior = tiempo_actual
    except:
            print("rostro no detectado")
            emotion = None

    key = cv2.waitKey(1)

    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows()


