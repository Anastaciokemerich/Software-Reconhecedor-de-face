

import os
import cv2
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from datetime import datetime
from Teste2 import NomeFi


start_time = datetime.now()

# OBJETO RECONHECEDOR DE CARA

EIGEN = cv2.face.EigenFaceRecognizer_create(10, 5000)

EIGEN2 = EIGEN.read("Recogniser/trainingDataEigan.xml")


face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
Pacote = 'dataSet'                # caminho para as fotos
img = cv2.imread('Imagens/thor22.jpg')
print(img)
def getImageWithID (Pacote):
    PacoteImagem = [os.Pacote.join(Pacote, f) for f in os.listdir(Pacote)]
    Facelista = []
    IDs = []

    for PacoteImagem in PacoteImagem:
        faceImage = Image.open(PacoteImagem).convert('L')  # Abrir imagem e converter para cinza

        print(str((faceImage.size)))
        print('Antes')
        faceImage = faceImage.resize((50,50))         # redimensionar a imagem para que o reconhecedor EIGEN possa ser treinado
        faceNP = np.array(faceImage, 'uint8')           # converter a imagem em matriz Numpy
        print('Depois')
        print(str((faceNP.shape)))
        ID = int(os.Pacote.split(PacoteImagem)[-1].split('.')[1])    # Obter o ID da matriz
        Facelista.append(faceNP)                         # Append a matriz Numpy à lista
        IDs.append(ID)                                  # Append o ID para a lista de IDs

    return np.array(IDs), Facelista                      # Os IDs são convertidos em uma matriz Numpy


IDs, Facelista = getImageWithID(Pacote)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)           # Converta a câmera em cinza
faces = face_cascade.detectMultiScale(gray, 1.3, 4)     # Detecte os rostos e armazene as posições
Info = open("SaveData/EIGEN_TEST_DATA.txt", "w+")
face_numero = 1

for (x, y, w, h) in faces:
    Face = cv2.resize((gray[y: y+h, x: x+w]), (50,50))
    Lev = 1
    eigen_ID = []
    eigen_conf = []
    for _ in range(1):#__________________________________Neurônios
        reco = cv2.face.EigenFaceRecognizer_create(Lev)     # RECONHECIMENTO DE EIGEN FACE
        print('TREINANDO COM  ' + str(Lev) + ' NEURONIO')
        reco.train(Facelista, IDs)                         # O reconhecedor é treinado usando as imagens
        print('RECONHECEDOR DA EIGEN FACE TREINADO')
        ID, conf = EIGEN.predict(faces)
        eigen_ID.append(ID)
        eigen_conf.append(conf)
        Info.write(str(ID) + "," + str(conf) + "\n")
        print ('PARA ' + str(Lev) + ' NEURONIOS A ID: ' + str(ID) + ' COM A CONFIANÇA: ' + str(conf))
        Lev = Lev + 1
    # ---------------------------------------- 1 Grafico -----------------------------------------------------
    fig  = plt.gcf()
    fig .canvas.set_window_title('RESULTADO PARA FACE ' + str(face_numero))
    plt.subplot(2, 1, 1)
    plt.plot(eigen_ID)
    plt.title('ID em Relação ao n'
              'Número de Neurônios', fontsize=10)
    plt.axis([0, Lev, 0, 25])
    plt.ylabel('ID', fontsize=8)
    plt.xlabel('Número de Neurônios', fontsize=8)
    p2 = plt.subplot(2, 1, 2)
    plt.plot(eigen_conf, 'red')
    plt.title('Confiança em Relação ao Número de Neurônios', fontsize=10)
    p2.set_xlim(xmin=0)
    p2.set_xlim(xmax=Lev)
    plt.ylabel('Confiança', fontsize=8)
    plt.xlabel(' Número de Neurônios', fontsize=8)
    plt.tight_layout()

    print (' MOSTRAR RESULTADOS PARA O FACE ' + str(face_numero))
    print(str(face_numero))
    cv2.imshow('FACE' + str(face_numero), Face)
    print(Face)
    plt.show()
    face_numero = face_numero + 1 #Numerode faces reconhecidas na imagem

print(img)
time_elapsed = datetime.now() - start_time

print('Tempo para Analisar a Imagem (hh:mm:ss.ms) {}'.format(time_elapsed))
cv2.waitKey()
Info.close()
cv2.destroyAllWindows()
