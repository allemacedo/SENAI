import requests
from datetime import datetime

print("📈 Consulta de Cotações - Bolsa de Valores Brasileira (B3)")
print("-" * 65)

ticker = input("Digite o código da ação (ex: PETR4, VALE3, ITUB4): ").upper()

url = f"https://brapi.dev/api/quote/{ticker}"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()

    if "results" in dados and len(dados["results"]) > 0:
        info = dados["results"][0]

        preco = info.get("regularMarketPrice", "N/A")
        nome = info.get("longName", ticker)
        moeda = info.get("currency", "BRL")
        hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print("\n📊 Resultado da Consulta:")
        print("-" * 65)
        print(f"Ação: {nome} ({ticker})")
        print(f"Cotação Atual: R$ {preco:.2f}" if preco != "N/A" else "Cotação não disponível.")
        print(f"Moeda: {moeda}")
        print(f"Consulta realizada em: {hora}")
        print("-" * 65)
    else:
        print("⚠️ Nenhum resultado encontrado para esse código de ação.")
else:
    print("Erro ao conectar à API. Verifique sua conexão com a internet ou tente novamente mais tarde.")