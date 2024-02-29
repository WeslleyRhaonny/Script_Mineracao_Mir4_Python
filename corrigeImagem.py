import cv2
import pytesseract

def teste():
    img = cv2.imread("captura.png")

    resultado = pytesseract.image_to_string(img)

    # Separa os minutos e segundos usando split e converte em inteiros
    minutos, segundos = map(int, resultado.split(":"))

    # Calcula o tempo total em segundos
    tempo_em_segundos = (minutos * 60) + segundos

    return tempo_em_segundos
