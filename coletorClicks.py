import time

import pyautogui
import csv

# Nome do arquivo onde as coordenadas dos cliques serão salvas
nome_arquivo = 'coordenadas_cliques.csv'

# Abre o arquivo para escrita
with open(nome_arquivo, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Escreve um cabeçalho no arquivo CSV
    writer.writerow(['X', 'Y'])

    # Loop para capturar as coordenadas dos cliques
    while True:
        time.sleep(1)

        # Obtém as coordenadas atuais do mouse
        x, y = pyautogui.position()
        print(f'Coordenadas: X={x}, Y={y}')

        # Escreve as coordenadas no arquivo CSV
        writer.writerow([x, y])

        # Aguarda um curto período de tempo antes de verificar novamente (você pode ajustar conforme necessário)
        pyautogui.PAUSE = 1
