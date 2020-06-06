# -------------------------- FACE DITECTION USING HAAR CASCADES ---------------------------
# ---------------------------- BY LAHIRU DINALANKARA AKA SPIKE ----------------------------

import cv2                  # Importing the opencv
from Teste2 import NomeFi

#  importar as cascatas Haar para a diteção facial

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')

img = cv2.imread('imagens/groupangle.jpg')

while True:
   # ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                    # Converte a camera para grayScale

    # ---------------------------------- FACE DETECÇÂO------------------------------------

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)             # Detectar os rostos e guardar as posições

    for (x, y, w, h) in faces:                                      # Frames  LOCALIZAÇÃO X, Y LARGURA, ALTURA
        gray_face = cv2.resize((gray[y: y+h, x: x+w]), (50, 50))  # Face é isolada e recortada
        eyes = eye_cascade.detectMultiScale(gray_face)
        for (ex, ey, ew, eh) in eyes:
            NomeFi.draw_box(gray, x, y, w, h)

    cv2.imshow('Face Detection Using Haar-Cascades ', gray)         # Mostra video
    if cv2.waitKey(1) & 0xFF == ord('q'):                           # Sair  Q
        break

cv2.destroyAllWindows()
