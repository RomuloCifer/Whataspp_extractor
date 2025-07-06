# ===================== IMPORTS =====================
import pyautogui
import pytesseract
import time
from PIL import Image
import json
import os
from utils import salvar_contatos, carregar_contatos, adicionar_contato

# ===================== CONFIGURAÇÕES =====================
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

POS_CONTATOS = [
    (300, 348),
    (300, 424),
    (300, 501),
    (300, 577),
    (300, 650),
    (300, 726),
    (300, 801),
    (300, 881),
    (300, 957),
    (300, 1017),
]

POS_ABRIR_PERFIL = (797, 153)
AREA_NOME_NUMERO = (1400, 180, 1900, 600)

ARQUIVO_JSON = "contatos.json"

# ===================== FUNÇÕES =====================
def rolar_contatos():
    print("Rolando contatos...")
    pyautogui.moveTo(300, 424)
    time.sleep(1)
    pyautogui.scroll(-910)
    time.sleep(1)

# ===================== EXECUÇÃO =====================
contatos = carregar_contatos()

print("Você tem 5 segundos para posicionar o WhatsApp Web certinho...")
time.sleep(5)

ultimo_telefone = None
tentativas_finais = 0
contador = 1
falhas_extracao = 0
max_falhas_extracao = 5

contatos_processados = 0  # Novo contador global

while tentativas_finais < 2 and falhas_extracao < max_falhas_extracao and contatos_processados < 25:
    telefone_ultimo_da_rodada = None

    for i, pos in enumerate(POS_CONTATOS, 1):
        print(f"\n📌 Capturando contato {i}...")

        pyautogui.click(pos)
        time.sleep(1.5)

        pyautogui.click(POS_ABRIR_PERFIL)
        time.sleep(1.5)

        imagem = pyautogui.screenshot()
        recorte = imagem.crop(AREA_NOME_NUMERO)

        texto = pytesseract.image_to_string(recorte).strip()
        linhas = texto.splitlines()

        nome = ""
        telefone = ""

        for idx, linha in enumerate(linhas):
            if "+55" in linha:
                telefone = linha.strip()
                for j in range(idx - 1, -1, -1):
                    nome_candidato = linhas[j].strip()
                    if nome_candidato:
                        nome = nome_candidato
                        break
                break

        if nome and telefone:
            falhas_extracao = 0
            telefone_ultimo_da_rodada = telefone
            adicionar_contato(contatos, {"nome": nome, "telefone": telefone})
        else:
            falhas_extracao += 1
            recorte.save(f"contato_{i}{contador}.png")
            print(f"⚠️ Não foi possível extrair nome/telefone. Falhas seguidas: {falhas_extracao}/{max_falhas_extracao}")

            if falhas_extracao >= max_falhas_extracao:
                print("❌ Número máximo de falhas de extração seguidas atingido. Encerrando o programa.")
                break


        pyautogui.press('esc')
        time.sleep(1)
        contador += 1
        contatos_processados += 1

        # Parar imediatamente se atingir o limite de 25 contatos
        if contatos_processados >= 25:
            print(f"✅ Limite de {contatos_processados} contatos atingido. Encerrando o programa.")
            break

    # Verificar repetição após capturar todos os visíveis
    if telefone_ultimo_da_rodada == ultimo_telefone:
        tentativas_finais += 1
        print(f"⚠️ Último contato repetido ({tentativas_finais}/2)")
    else:
        tentativas_finais = 0
        ultimo_telefone = telefone_ultimo_da_rodada

    rolar_contatos()

    if falhas_extracao >= max_falhas_extracao:
        break

# ===================== SALVAR =====================
if contatos:
    salvar_contatos(contatos)
else:
    print("\n⚠️ Nenhum contato foi salvo.")