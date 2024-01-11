import requests
from bs4 import BeautifulSoup
from datetime import datetime

data_e_dia = datetime.now().strftime("%Y-%m-%d %A")

headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"}
link="https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar"
requisicao = requests.get(link, headers=headers)
print(requisicao)
site = BeautifulSoup(requisicao.text, "html.parser")
cotacao = site.find('input', class_="lWzCpb a61j6")

print(f"Data e dia da execução: {data_e_dia}")
print("1 dolar está valendo R$ " + cotacao["value"])
