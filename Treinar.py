import os
import cv2
import numpy as np
from PIL import Image
import time

# -------------------------TREINADOR PARA TODOS OS ALGORITMOS NO RECONHECIMENTO FACIAL ----------------------------------------- -

import os                                               # import  OS para Pacote
import cv2                                              # import o OpenCV biblioteca
import numpy as np                                      # import Numpy biblioteca
from PIL import Image                                   # import Imagen biblioteca
import timeit
from datetime import datetime
start_time = datetime.now() # inicia o contador de tempo

EigenFace = cv2.face.EigenFaceRecognizer_create(15)      # criando EIGEN FACE RECOGNISER

path = 'dataSet'                                        #caminho para as fotos

def pegaIDimagem (path):
    imagepacote = [os.path.join(path, f) for f in os.listdir(path)]
    Facelista = []
    IDs = []
    for imagePath in imagepacote:
        faceImage = Image.open(imagePath).convert('L')              # Abrir imagem e converter para cinza
        faceImage = faceImage.resize((50,50))                      # redimensionar a imagem para que o reconhecedor EIGEN possa ser treinado
        faceNP = np.array(faceImage, 'uint8')                         # converter a imagem em matriz Numpy
        ID = int(os.path.split(imagePath)[-1].split('.')[1])        # Recriei novamente o ID da matriz
        Facelista.append(faceNP)                                      # Append matriz Numpy à lista
        IDs.append(ID)                                               # Append o ID para a lista de IDs
        cv2.imshow('@&@', faceNP)              # Mostrar as imagens na lista
        cv2.waitKey(1)
    return np.array(IDs), Facelista                                  # Os IDs são convertidos em uma matriz Numpy
IDs, Facelista = pegaIDimagem(path)

# ------------------------------------  TREINANDO O RECONHECEDOR ----------------------------------------
print('TREINANDO......')
EigenFace.train(Facelista, IDs)                                          #O reconhecedor é treinado usando as imagens
print('EIGEN FACE COMPLETO TREINANDO...')
EigenFace.save('Recogniser/trainingDataEigan.xml')
print('ARQUIVO SALVADO..')
print ('TODO ARQUIVO XML SALVADO...')
cv2.destroyAllWindows()
time_elapsed = datetime.now() - start_time
print('Tempo para Analisar a Imagem e treinar (hh:mm:ss.ms) {}'.format(time_elapsed)) #finaliza e mostra o tempo