import requests
from PySimpleGUI import Window, Input, Button, Checkbox, Text

mo_e_da=''

class TelaPython:
    def Iniciar(self, self1):
        pass

class telapython:
    def __init__(self):
        layout = [
            [Checkbox('Dólar', key='Dolar'), Checkbox('Euro', key='Euro'), Checkbox('BitCoins', key='BTC')],
            [Text('Endereco do Arquivo', size=(20, 0)), Input(size=(20, 0), key='Endereco do Arquivo')],
            [Text('Local de descricao da moeda', size=(20, 0)), Input(size=(10, 0), key='loc desc moeda')],
            [Text('Local da Cotacao', size=(20, 0)), Input(size=(15, 0), key='cotacao')],
            [Text('Local em Reais', size=(20, 0)), Input(size=(15, 0), key='reais')],
            [Text('Loc Moeda Original', size=(20, 0)), Input(size=(15, 0), key='original')],
            [Button('Confirmar Dados')]
        ]
        self.janela = Window("Atualizador de Cotações").layout(layout)
   
    @staticmethod   
    def pegar_cotacoes(cot):
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
        requisicao_dic = requisicao.json()

        global mo_e_da

        if cot == 1:            
            mo_e_da = "Dólar"
            return requisicao_dic["USDBRL"]["bid"]

        if cot == 2:            
            mo_e_da = "Euro"
            return requisicao_dic["EURBRL"]["bid"]

        if cot == 3:           
            mo_e_da = "BitC"
            return requisicao_dic["BTCBRL"]["bid"]



    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.read()
            cot_dol = self.values['Dolar']
            if cot_dol == True:
                cot=1
                cotacao=tela.pegar_cotacoes(cot)   

            cot_eu = self.values['Euro']
            if cot_eu == True:
                cot=2
                cotacao=tela.pegar_cotacoes(cot)   
           
            cot_btc = self.values['BTC']
            if cot_btc == True:
                cot=3
                cotacao=tela.pegar_cotacoes(cot)   
           
            dados = self.values['Endereco do Arquivo']
            desc_moeda = self.values['loc desc moeda']
            loc_cot = self.values['cotacao']
            loc_val_reais = self.values['reais']
            loc_val_original = self.values['original']
            print(f'Aceita dólar: {cot_dol}')
            print(f'aceita  euro: {cot_eu}')
            print(f'aceita btc: {cot_btc}')
            print(f'Informe o local da planilha: {dados}')
            print(f'Informe a coluna de descrição da moeda: {desc_moeda}')
            print(f'Informe coluna dos valores da cotação: {loc_cot}')
            print(f'Informe coluna do valor de compras em R$: {loc_val_reais}')
            print(f'Informe a coluna do valor de compra original: {loc_val_original}')  

            import pandas as pd

            tabela = pd.read_excel(dados)
            pd.set_option('Display.max_columns', None)
            print(tabela)

            tabela.loc[tabela[desc_moeda] == mo_e_da, loc_cot] = float(cotacao)
            tabela[loc_val_reais] = tabela[loc_cot] * tabela[loc_val_original]
            print(tabela)



tela = telapython()
tela.Iniciar()