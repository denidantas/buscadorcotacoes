import requests
from PySimpleGUI import Window, Input, Button, Checkbox, Text


class telapython:
    def __init__(self):
        layout = [
            [Checkbox('Dolar', key='Dolar'), Checkbox('Euro', key='Euro'), Checkbox('BitCoins', key='BTC')],
            [Text('Endereco do Arquivo', size=(20, 0)), Input(size=(20, 0), key='Endereco do Arquivo')],
            [Text('Local de descricao da moeda', size=(30, 0)), Input(size=(10, 0), key='loc desc moeda')],
            [Text('Local da Cotacao', size=(30, 0)), Input(size=(15, 0), key='cotacao')],
            [Text('Local em Reais', size=(35, 0)), Input(size=(15, 0), key='reais')],
            [Text('Loc Moeda Original', size=(35, 0)), Input(size=(15, 0), key='original')],
            [Button('Confirmar Dados')]
        ]
        self.janela = Window("Atualizador de Cotações").layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.read()
            cot_dol = self.values['Dólar']
            cot_eu = self.values['Euro']
            cot_btc = self.values['BTC']
            local_arq = self.values['Endereco do Arquivo']
            desc_moeda = self.values['loc desc moeda']
            loc_cot = self.values['cotacao']
            loc_val_reais = self.values['reais']
            loc_val_original = self.values['original']
            print(f'Aceita dólar: {cot_dol}')
            print(f'aceita  euro: {cot_eu}')
            print(f'aceita btc: {cot_btc}')
            print(f'Informe o local da planilha: {local_arq}')
            print(f'Informe a coluna de descrição da moeda: {desc_moeda}')
            print(f'Informe coluna dos valores da cotação: {loc_cot}')
            print(f'Informe coluna do valor de compras em R$: {loc_val_reais}')
            print(f'Informe a coluna do valor de compra original: {loc_val_original}')
    
    def pegar_cotacoes(cot):
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
        requisicao_dic = requisicao.json()

        if cot == 1:
            mo_e_da = "Dólar"
            return requisicao_dic["USDBRL"]["bid"]

        if cot == 2:
            mo_e_da = "Euro"
            return requisicao_dic["EURBRL"]["bid"]

        if cot == 3:
            mo_e_da = "BitC"
            return requisicao_dic["BTCBRL"]["bid"]


tela = telapython()
tela.Iniciar()

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

tabela.loc[tabela[coluna] == mo_e_da, col2] = float(cotacao)
tabela[col3] = tabela[col2] * tabela[col4]
print(tabela)
