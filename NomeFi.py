#     -----------  FUNÇÃO PARA LER O ARQUIVO E ADICIONAR OS NOMES E IDs NOS TUPLES

import cv2  # cap video biblioteca
import math  # para Imagem Rotação biblioteca
import time  # Time biblioteca
import os  # biblioteca

now_time = time.clock()

face = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')  # Classificador "frontal-face" Haar Cascade
olhos_cas = cv2.CascadeClassifier('Haar/haarcascade_eye_tree_eyeglasses.xml')  # Classificador "eye" Haar Cascade

WHITE = [255, 255, 255]


def FileRead():
    Info = open("Nomes.txt", "r")  # Abrir o arquivo de texto em modo read
    NOME = []  # A tupla para armazenar nomes
    while (True):  # Leia todas as linhas no arquivo e armazene-as em duas tuplas
        linha = Info.readline()
        if linha == '':
            break
        NOME.append(linha.split(",")[1].rstrip())

    return NOME  # Retorne as duas tuplas


Nomes = FileRead()  # Execute a função acima para obter a tupla de identificação e nomes


#     ------------------- FUNÇÃO PARA ENCONTRAR O NOME  -----------------------------------------------------------

# Verificação do último ID no Nomes.txt
def file_is_empty(path):
    return os.stat(path).st_size == 0


with open('Nomes.txt') as f:
    lines = f.readlines()
    if file_is_empty('Nomes.txt'):
        last_string = 1
    else:
        last_row = lines[-1]
        string_last = last_row
        for s in string_last.split():
            if s.isdigit():
                last_string = int(s)
                print("A base possui: " + str(last_string) + " " + "pessoas")


def ID2Nome(ID, conf):
    if ID >= 1 and ID <= last_string:
        NomeString = "Nome: " + Nomes[ID - 1] + " Confianca: " + (
            str(round(conf)))  # Encontre o nome usando o índice do ID
    else:
        NomeString = " Face Not Recognised "  # Encontre o nome usando o índice do ID

    return NomeString


#     ------------------- ESTA FUNÇÃO LÊ O ARQUIVO E ADICIONA O NOME AO FIM DO ARQUIVO  -----------------


def AddNome():
    Nome = input('Enter Your Nome ')
    Info = open("Nomes.txt", "r+")
    ID = ((sum(1 for line in Info)) + 1)
    Info.write(str(ID) + " " + "," + " " + Nome + "\n")
    print("Nome Stored in " + str(ID))
    Info.close()
    return ID


#     ------------------- DESENHE A CAIXA AO REDOR DA CARA, ID E CONFIANÇA  -------------------------------------


def DispID(x, y, w, h, NOME, Imagem):
    #  --------------------------------- A POSIÇÃO DA CAIXA DE IDENTIFICAÇÃO  ---------------------------------------------

    Nome_y_pos = y - 10
    Nome = x + w / 2 - (len(NOME) * 7 / 2)

    if Nome < 0:
        Nome = 0
    elif (Nome + 10 + (len(NOME) * 7) > Imagem.shape[1]):
        Nome = Nome - (Nome + 10 + (len(NOME) * 7) - (Imagem.shape[1]))
    if Nome_y_pos < 0:
        Nome_y_pos = Nome_y_pos = y + h + 10

    #  ------------------------------------   DESENHO DA CAIXA E ID   --------------------------------------

    draw_box(Imagem, x, y, w, h)

    cv2.rectangle(Imagem, (int(Nome - 10), int(Nome_y_pos - 25)),
                  (int(Nome + 10 + (len(NOME) * 7)), int(Nome_y_pos - 1)), (0, 0, 0), -2)
    cv2.rectangle(Imagem, (int(Nome - 10), int(Nome_y_pos - 25)),
                  (int(Nome + 10 + (len(NOME) * 7)), int(Nome_y_pos - 1)), WHITE,
                  1)  # Desenhe um retângulo preto sobre a moldura do rosto
    cv2.putText(Imagem, NOME, (int(Nome), int(Nome_y_pos - 10)), cv2.FONT_HERSHEY_DUPLEX, .4,
                WHITE)  # Imprimir o nome do ID


def draw_box(Imagem, x, y, w, h):
    cv2.line(Imagem, (x, y), (x + (int(w / 5)), y), WHITE, 2)
    cv2.line(Imagem, (x + ((int(w / 5) * 4)), y), (x + w, y), WHITE, 2)
    cv2.line(Imagem, (x, y), (x, y + (int(h / 5))), WHITE, 2)
    cv2.line(Imagem, (x + w, y), (x + w, y + int((h / 5))), WHITE, 2)
    cv2.line(Imagem, (x, (y + int((h / 5 * 4)))), (x, y + h), WHITE, 2)
    cv2.line(Imagem, (x, (y + h)), (x + int((w / 5)), y + h), WHITE, 2)
    cv2.line(Imagem, (x + (int((w / 5) * 4)), y + h), (x + w, y + h), WHITE, 2)
    cv2.line(Imagem, (x + w, (y + int((h / 5 * 4)))), (x + w, y + h), WHITE, 2)


# ---------------     SEGUNDA CAIXA DE IDENTIFICAÇÃO     ----------------------
def DispID2(x, y, w, h, NOME, Imagem):
    #  --------------------------------- A POSIÇÃO DA CAIXA DE IDENTIFICAÇÃO  -------------------------------------------------

    Nome_y_pos = y - 40
    Nome = x + w / 2 - (len(NOME) * 7 / 2)

    if Nome < 0:
        Nome = 0
    elif (Nome + 10 + (len(NOME) * 7) > Imagem.shape[1]):
        Nome = Nome - (Nome + 10 + (len(NOME) * 7) - (Imagem.shape[1]))
    if Nome_y_pos < 0:
        Nome_y_pos = Nome_y_pos = y + h + 10

    #  ------------------------------------    O DESENHO DA CAIXA E ID   --------------------------------------
        cv2.rectangle(Imagem, (int(Nome - 10), int(Nome_y_pos - 25)),
                  (int(Nome + 10 + (len(NOME) * 7)), int(Nome_y_pos - 1)), (0, 0, 0), -2)
    cv2.rectangle(Imagem, (int(Nome - 10), int(Nome_y_pos - 25)),
                  (int(Nome + 10 + (len(NOME) * 7)), int(Nome_y_pos - 1)), WHITE,
                  1)  # Desenhe um retângulo preto sobre a moldura do rosto
    cv2.putText(Imagem, NOME, (int(Nome), int(Nome_y_pos - 10)), cv2.FONT_HERSHEY_DUPLEX, .4,
                WHITE)  # Imprimir o nome do ID


# ---------------     TERCEIRA CAIXA DE IDENTIFICAÇÃO      ----------------------
def DispID3(x, y, w, h, NOME, Imagem):
    #  ---------------------------------     # A POSIÇÃO DA CAIXA DE IDENTIFICAÇÃO -------------------------------------------------

    Nome_y_pos = y - 70
    Nome = x + w / 2 - (len(NOME) * 7 / 2)

    if Nome < 0:
        Nome = 0
    elif (Nome + 10 + (len(NOME) * 7) > Imagem.shape[1]):
        Nome = Nome - (Nome + 10 + (len(NOME) * 7) - (Imagem.shape[1]))
    if Nome_y_pos < 0:
        Nome_y_pos = Nome_y_pos = y + h + 10

    #  ------------------------------------    O DESENHO DA CAIXA E ID   --------------------------------------
    cv2.rectangle(Imagem, (int(Nome - 10), int(Nome_y_pos - 25)),
                  (int(Nome + 10 + (len(NOME) * 7)), int(Nome_y_pos - 1)), (0, 0, 0), -2)
    cv2.rectangle(Imagem, (int(Nome - 10), int(Nome_y_pos - 25)),
                  (int(Nome + 10 + (len(NOME) * 7)), int(Nome_y_pos - 1)), WHITE,
                  1)  # Desenhe um retângulo preto sobre a moldura do rosto
    cv2.putText(Imagem, NOME, (int(Nome), int(Nome_y_pos - 10)), cv2.FONT_HERSHEY_DUPLEX, .4,
                WHITE)  # Imprimir o nome do ID


def DrawBox(Imagem, x, y, w, h):# retângulo
    cv2.rectangle(Imagem, (x, y), (x + w, y + h), (255, 255, 255), 1)  # Desenhe um retângulo ao redor da face



# ----------------------------- ESTA FUNÇÃO TEM EM CASCATA ESPECÍFICA, CASCAÇA FACIAL E UMA IMAGEM
# # ------------------------- RETORNA UM ROSTO CORTADO E SE POSSÍVEL endireita a inclinação da cabeça


def Detectaolho(Imagem):
    Coordenada = 0
    linha, col = Imagem.shape
    olhos = olhos_cas.detectMultiScale(Imagem)  # detecta os olhos
    for (sx, sy, sw, sh) in olhos:
        if olhos.shape[0] == 2:  # A Imagem deve ter 2 olhos
            if olhos[1][0] > olhos[0][0]:
                DY = ((olhos[1][1] + olhos[1][3] / 2) - (
                            olhos[0][1] + olhos[0][3] / 2))  # Diferença de altura entre os olhos
                DX = ((olhos[1][0] + olhos[1][2] / 2) - olhos[0][0] + (
                            olhos[0][2] / 2))  # Diferença de largura entre os olhos
            else:
                DY = (-(olhos[1][1] + olhos[1][3] / 2) + (
                            olhos[0][1] + olhos[0][3] / 2))  # Diferença de altura entre os olhos
                DX = (-(olhos[1][0] + olhos[1][2] / 2) + olhos[0][0] + (
                            olhos[0][2] / 2))  # Diferença de largura entre os olhos

            if (DX != 0.0) and (DY != 0.0):  # Certifique-se de que a alteração ocorra apenas se houver um ângulo
                Coordenada = math.degrees(math.atan(round(float(DY) / float(DX), 2)))  # Encontre o ângulo
                print("Coordenada  " + str(Coordenada))

                M = cv2.getRotationMatrix2D((col / 2, linha / 2), Coordenada, 1)  # Encontre a matriz de rotação
                Imagem = cv2.warpAffine(Imagem, M, (col, linha))
                # cv2.imshow('GIRADA', Imagem)                 # se tiver um angulo na foto gira

                Face2 = face.detectMultiScale(Imagem, 1.3, 5)  # Isso detecta um rosto na imagem
                for (FaceX, FaceY, FaceWidth, FaceHeight) in Face2:
                    CortaFace = Imagem[FaceY: FaceY + FaceHeight, FaceX: FaceX + FaceWidth]
                    return CortaFace


def tell_time_passed():
    print('TEMPO PASSOU ' + str(round(((time.clock() - now_time) / 60), 2)) + ' MINS')
