import pyautogui
import time
import webbrowser

url_sigmine = 'https://dados.gov.br/dados/conjuntos-dados/sistema-de-informacoes-geograficas-da-mineracao-sigmine'
tempo_carregamento_pagina = 8  
tempo_download = 120  

print("Abrindo navegador e acessando SIGMINE...")
webbrowser.open(url_sigmine)
time.sleep(tempo_carregamento_pagina)

print("Procurando botão 'Acessar o recurso'...")

pyautogui.moveTo(800, 500) 
pyautogui.click()
time.sleep(tempo_carregamento_pagina)

print("Procurando link de download...")

pyautogui.moveTo(850, 600)
pyautogui.click()

print(f"Aguardando {tempo_download} segundos para o download ser concluído...")
time.sleep(tempo_download)

print("Download concluído! Processo finalizado!")
