import requests

# teste 2

cot = dolar = euro = btc = 0
mod = ""
cot = int(input("Informe: 1 - Cotação Dólar   2 - Cotação Euro   3 - cotação BitC: "))


def pegar_cotacoes(cot):
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    if cot == 1:
        mod = "Dólar"
        return requisicao_dic["USDBRL"]["bid"]

    if cot == 2:
        mod = "Euro"
        return requisicao_dic["EURBRL"]["bid"]

    if cot == 3:
        mod = "BitC"
        return requisicao_dic["BTCBRL"]["bid"]


cotacao = pegar_cotacoes(cot)
import pandas as pd

dados = input("Informe o endereço da tabela Excel que deseja atualizar valores: ")
tabela = pd.read_excel(dados)
pd.set_option('Display.max_columns', None)
print(tabela)
coluna = input("Informe nome da coluna dos valores da moeda a ser alterada: ")
col2 = input("Informe o nome dacoluna que contém os valores da moeda desejada:")
col3 = input("Informe a coluna do valor de compra em Reais: ")
col4 = input("informa a coluna que contém o valor na moeda original: ")
# tabela.loc[tabela[(coluna)] == "Dólar","Cotação"] = float(cotacao)
# tabela["Preço Base Reais"] = tabela["Cotação"] * tabela["Preço Base Original"]
# tabela["Preço Final"] = tabela["Preço Base Reais"] * tabela["Ajuste"]

tabela.loc[tabela[coluna] == "Dólar", col2] = float(cotacao)
tabela[col3] = tabela[col2] * tabela[col4]
print(tabela)
