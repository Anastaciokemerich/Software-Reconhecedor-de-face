
import cv2                  # Importing the opencv
import numpy as np          # Import Numarical Python
from Teste2 import NomeFi

WHITE = [255, 255, 255]

#   importar as cascatas Haar para a diteção facial

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')

ID = NomeFi.AddNome()
Count = 0
cap = cv2.VideoCapture(0)                                                                           # Camera

while Count < 50:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                                    # Converte a camera para grayScale
    if   110>=  np.average(gray) < 110 :                                                                      # Teste do brilho da imagem
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)                                         # Detectar os rostos e guardar as posições
        for (x, y, w, h) in faces:                                                                  # Frames  LOCALIZAÇÃO X, Y LARGURA, ALTURA
            FaceImage = gray[y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5)]    # Face é isolada e recortada
            print(FaceImage)
            Img = (NomeFi.DetectEyes(FaceImage))
            cv2.putText(gray, "FACE DETECTADA", (x+int((w/2)), y-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)
            if Img is not None:
                frame = Img                                                                         # mostra faces recortadas
            else:
                frame = gray[y: y+h, x: x+w]
            cv2.imwrite("dataSet/User." + str(ID) + "." + str(Count) + ".jpg", frame)
            cv2.waitKey(500)
            cv2.imshow("FOTOGRAFIAS CAPTURADAS", frame)                                                     # Mostra a captura
            Count = Count + 1
    cv2.imshow('Faces de Captura do Sistema de Reconhecimento Facial', gray)                                # Mostra o video
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
print ('A CAPTURA DO ROSTO PARA O ASSUNTO ESTÁ COMPLETA')
cap.release()
cv2.destroyAllWindows()
