import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/daily/USD-BRL/30")
lista_cotacao = cotacoes.json()
lista_cotacao_dolar = [float(item['bid']) for item in lista_cotacao]
print(lista_cotacao_dolar)
