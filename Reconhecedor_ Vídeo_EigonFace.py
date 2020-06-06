
import cv2
from Teste2 import NomeFi

#------------------------  importe as Haar Cascade para obter a detecção de rosto e olho_______________________________________

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml') # Classificador "frontal-face" Haar Cascade
eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml') # Classificador "eye" Haar Cascade

recognise = cv2.face.EigenFaceRecognizer_create(15,4000)  # cria EIGEN FACE RECOGNISER
recognise.read("Recogniser/trainingDataEigan.xml")        # Carregar os dados do treinamento



EIGEN = cv2.face.EigenFaceRecognizer_create(10, 5000)



# Carregue os dados de treinamento do treinador para reconhecer os rostos

EIGEN.read("Recogniser/trainingDataEigan.xml")


# -------------------------     START O VIDEO  ------------------------------------------
cap = cv2.VideoCapture(0)                                                       # Camera object
#cap = cv2.VideoCapture('Videos_Treino/Alexandre_Garcia.mp4')                     # Video object
ID = 0
face_numero = 1
while True:
    ret, img = cap.read()                                                       # Leia o objeto da câmera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converta a câmera em gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)                         # Detecte os rostos e armazene as posições
    for (x, y, w, h) in faces:                                                  # Quadros LOCALIZAÇÃO X, LARGURA Y, ALTURA

# ------------ CONFIRMANDO QUE OS OLHOS ESTÃO DENTRO DO ROSTO MELHOR RECONHECIMENTO DE ROSTO É GANHADO ------------------

        gray_face = cv2.resize((gray[y: y+h, x: x+w]), (50, 50))              # O rosto é isolado e cortado
        eyes = eye_cascade.detectMultiScale(gray_face)
        for (ex, ey, ew, eh) in eyes:
            ID, conf = LBPH.predict(gray_face)  # Determine the ID of the photo
            NOME = NomeFi.ID2Nome(ID, conf)
            NomeFi.DispID(x, y, w, h, NOME, gray)
            print(NOME)
            cv2.imshow('FACE' + str(face_numero), gray_face)
            face_numero = face_numero + 1
            print(' MOSTRAR RESULTADOS PARA O FACE ' + str(face_numero))
    cv2.imshow('Sistema de reconhecimento de rosto EigenFace', gray)           # Mostrar o vídeo
    if cv2.waitKey(1) & 0xFF == ord('q'):                                       # Sair Q
        break
cap.release()
cv2.destroyAllWindows()


