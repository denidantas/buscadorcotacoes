import requests
#teste 2

cot = dolar = euro = btc= 0
cot = int(input("Informe: 1 - Cotação Dólar   2 - Cotação Euro   3 - cotação BitCoins: "))
def pegar_cotacoes(cot):
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    if cot == 1:
       cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
       print(cotacao_dolar)
    if cot==2:
       cotacao_euro = requisicao_dic["EURBRL"]["bid"]
       print(cotacao_euro)
    if cot ==3:
       cotacao_btc = requisicao_dic["BTCBRL"]["bid"]
       print(cotacao_btc)

pegar_cotacoes(cot)
cotacao = pegar_cotacoes(cot)
import pandas as pd


dados = input("Informe o endereço da tabela Excel que deseja atualizar valores: ")
tabela = pd.read_excel(dados)
print(tabela)
coluna = input("informe nome da coluna dos valores da moeda a ser alterada: ")

if tabela.loc[(coluna)] == "Dólar" and tabela.loc[(coluna)] == "Cotação":
    tabela["Cotação"] = cotacao
    tabela["Preço de Compra"] = tabela["Cotação"] * tabela["Preço Original"]

print(tabela)