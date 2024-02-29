import random
import time
from PIL import ImageGrab
from pywinauto.application import Application
from pynput import keyboard

import corrigeImagem


def coords_relativas(janela, posicoes):
    coord_absolutas_janela = (janela.rectangle().left, janela.rectangle().top)

    # Calcula as coordenadas relativas
    coord_relativas = (
        posicoes[0] - coord_absolutas_janela[0],
        posicoes[1] - coord_absolutas_janela[1]
    )

    return coord_relativas
def verificar_Mineracao(coordenadas):
    # Obtenha a cor do pixel na janela
    time.sleep(1)
    #janela.click_input(coords=(coordenadas[0], coordenadas[1]))
    imagem = ImageGrab.grab(bbox=(coordenadas[0] - 1, coordenadas[1] - 1, coordenadas[0] + 1, coordenadas[1] + 1))
    cor_obtida = imagem.getpixel((1, 1))

    # Define a cor RGB desejada
    cor_desejada = (20, 70, 134)
    margem = 25
    # Verifique se a cor obtida está dentro do intervalo
    if (abs(cor_obtida[0] - cor_desejada[0]) <= margem and
        abs(cor_obtida[1] - cor_desejada[1]) <= margem and
        abs(cor_obtida[2] - cor_desejada[2]) <= margem):
        return True
    else:
        return False
def realizar_acoes_na_janela(janela, coord_relativas):
    # Envie a tecla F10 para a janela
    janela.type_keys("{F10}")

    # Aguarde um momento (2 segundos)
    time.sleep(1)
    posicaoMiner = (429, 654)

    # Realize dois cliques nas coordenadas especificadas dentro da janela
    janela.click_input(coords=coord_relativas)
    janela.click_input(coords=coord_relativas)
    time.sleep(40)
    janela.click_input(coords=coords_relativas(janela, posicaoMiner))


def printarTempo():
    coordenadas2 = [(713,508),(742,524)]
    # Determina os limites da região retangular
    x_inicial, y_inicial = coordenadas2[0]
    x_final, y_final = coordenadas2[1]

    # Captura a região retangular
    imagem2 = ImageGrab.grab(bbox=(x_inicial, y_inicial, x_final, y_final))

    # Salva a imagem em um arquivo
    imagem2.save('captura.png')

# Defina o título da janela do aplicativo que deseja automatizar
titulo_alvo = "Mir4G[0]"

# Crie uma instância do aplicativo usando o título da janela
app = Application(backend="win32").connect(title=titulo_alvo)

# Obtenha a janela alvo
janela = app.window(title=titulo_alvo)

janela.set_focus()

# Coordenadas absolutas (X, Y) da janela
coord_absolutas_janela = (janela.rectangle().left, janela.rectangle().top)

# Coordenadas (X, Y) desejadas (coordenadas absolutas)
coordMinerX = 682
coordMinerY = 445

# Calcula as coordenadas relativas
coord_relativas = (
    coordMinerX - coord_absolutas_janela[0],
    coordMinerY - coord_absolutas_janela[1]
)

# Coordenadas (X, Y) desejadas
coord_x = 568
coord_y = 447
coordenadas = [(581, 292), (590, 445), (568, 447), (603, 391), (637, 280), (559, 237), (513, 234), (509, 528), (535, 570), (509, 576), (581, 292)]

ultimo_sorteio = -1

while True:
    sorteio = random.randint(0, 10)
    if sorteio != ultimo_sorteio:
        ultimo_sorteio = sorteio
        break

# Flag para controlar o loop
executando = True


def on_key_release(key):
    global executando
    if key == keyboard.Key.esc:  # Você pode definir a tecla que deseja usar para parar o loop
        executando = False


# Crie um ouvinte de teclado
listener = keyboard.Listener(on_release=on_key_release)
listener.start()

while executando:
    while(True):
        sorteio = random.randint(0, 10)
        if sorteio != ultimo_sorteio:
            ultimo_sorteio = sorteio
            break

    realizar_acoes_na_janela(janela, coordenadas[sorteio])
    while(True):
        testeMiner = verificar_Mineracao(coord_relativas)
        if not testeMiner:
            print("Vou procurar outra pedra")
            break
        if testeMiner:
            print("minerando")
            printarTempo()
            tempoDeMineracao = corrigeImagem.teste()
            print(f"irei procurar outra pedra em {tempoDeMineracao+10} segundos")
            time.sleep(tempoDeMineracao+10)
            break

