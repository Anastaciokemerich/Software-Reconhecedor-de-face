# Software-Reconhecedor-de-face

ABAIXO SEGUE O PASSO A PASSO PARA EXECUTAR


Primeiramente, é importante dizer que você deve possuir algum interpretador python instalado em sua máquina. Sugiro utilizar o Anaconda Python. Ele tem disponível para Windows, Mac e Linux.

Após instalar o Anaconda em sua máquina, deve instalar também o pacote pillow e opencv..

OpenCV: https://www.scivision.co/install-opencv-python-windows 
pillow: https://wp.stolaf.edu/it/installing-pil-pillow-cimage-on-windows-and-mac/

Também é necessário que possua uma webcam em sua máquina.

1-Executar o arquivo Captura_imagem_Gira.py

Ao executar o código, abrirá uma tela com a imagem em tempo real da sua webcam. Em seguida, 50 fotos serão tiradas do seu rosto. Posicione o rosto o mais próximo do centro do quadrado que aparecerá na imagem. Após executar este arquivo, as 50 fotos que foram tiradas do seu rosto, ficarão armazenadas na pasta dataet e o seu nome e ID serão inseridos no arquivo Names.txt.

2- Após isso, execute o arquivo Treinar.py

Ao executar este arquivo, o seu algoritmo será treinado para poder identificar as imagens posteriores. Ao fim da execução deste arquivo, arquivos .xml serão adicionados ao diretório Recogniser. Estes arquivos conterão as informações necessárias para que seu algoritmo seja capaz de identificar os rostos.

3- Por fim, Reconhecedor_Video_EigenFace.py, para fazer o reconhecimento da base treinda

É isso!

__________________________________________________________________________________________________________________________________


Detectar_Video.py: Este diretorio detecta rostos usando cascatas Haar. Funciona para com múltiplas faces.

Captura_imagem_Gira.py: Ao executar este diretorio irá captar 50 imagens de uma pessoa infractora da câmara. Vai garantir que as fotos não são escuras e também fará com que o rosto fique direito girando se estiver enclinado.

NomeFi.py: Este diretorio contém todas as funções.

Treinar.py: Este diretorio irá treinar o algoritmos de reconhecimento utilizando as imagens da pasta DataSet.

Reconhecedor_ Imagem.py: Esta aplicação irá detectar e reconhecer rostos a partir de imagens. Podem ser seleccionadas imagens difrentes.

Reconhecedor_Video_EigenFace.py: Este diretorio é o diretorio que irá reconhecer rostos a partir da alimentação da câmara utilizando o algoritmo Eigen face.

Coler_dados_Neuroneos_EiganFace.py: Este diretorio é a aplicação de teste. Ele irá receber uma imagem e o conjunto de dados será carregado. Um laço irá correr quantas veses quiser
cada vez, aumentando o número de componentes. De cada vez, será treinado um reconhecimento facial Eigen e
previsto na imagem de entrada. Após o loop for completado, a identificação e a confiança serão mostradas.

------------------PASTAS -----------
dataSet --> Contém as imagens que serão usadas para treinar o reconhecedor.
Haar --> Contém as cascatas Haar do OpenCV utilizadas nas aplicações
Reconhecedor --> Contém os ficheiros XML guardados pelos reconciliadores
SaveData --> Contém os dados guardados pelas aplicações de teste
