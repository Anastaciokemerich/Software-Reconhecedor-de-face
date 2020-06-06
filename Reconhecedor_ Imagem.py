# ------------------------------ FACE RECOGNISER FOR ALL THE ALGORITHMS  ---------------------------------


import cv2  # opencv
import numpy as np  # Import numpy
from Teste2 import NomeFi
# --- importe as cascatas de Haar para obter a detecção de rosto e olho

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')
spec_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye_tree_eyeglasses.xml')

# OBJETO RECONHECEDOR DE FACE

EIGEN = cv2.face.EigenFaceRecognizer_create(10, 5000)


# Carregue os dados de treinamento do treinador para reconhecer os rostos
EIGEN.read("Recogniser/trainingDataEigan.xml")


# ------------------------------------  entrada da images  -----------------------------------------------------

img = cv2.imread('imagens/Zamberlan.JPG')  # ------->>> O ENDEREÇO ​​À FOTOGRAFIA

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Converta a câmera em cinza
faces = face_cascade.detectMultiScale(gray, 1.3, 4)  # Detecte os rostos e armazene as posições
#print(faces) #matriz da face
face_numero = 1
for (x, y, w, h) in faces:  # Frames  LOCALIZAÇÃO X, LARGURA Y, ALTURA

    #Face = cv2.resize((gray[y: y + h, x: x + w]), (20,10))  # O rosto está isolado e cortado

    ID, conf = EIGEN.predict(faces)  # RECONHECIMENTO  com EIGEN
    print(ID)
    NOME = NomeFi.ID2Nome(ID, conf)
    NomeFi.DispID(x, y, w, h, NOME, gray)
    print(ID)
    print(NOME)
    print(str(face_numero))
    cv2.imshow('Sistema de reconhecimento facial', gray)  # DISPLAY
    cv2.imshow('FACE' + str(face_numero), Face) #recorta as faces
    face_numero = face_numero +1
    print(' MOSTRAR RESULTADOS PARA O FACE ' + str(face_numero))

cv2.waitKey(0)
cv2.destroyAllWindows()

