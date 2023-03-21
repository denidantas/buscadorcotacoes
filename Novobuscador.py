#import requests
import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Checkbox('Dolar', key='Dolar'), sg.Checkbox('Euro', key='Euro'), sg.Checkbox('BitCoins', key='BTC')],
            [sg.Text('Endereco do Arquivo', size=(20, 0)), sg.Input(size=(20, 0), key='Endereco do Arquivo')],
            [sg.Text('Local de descricao da moeda', size=(30, 0)), sg.Input(size=(10, 0), key='loc desc moeda')],
            [sg.Text('Local da Cotacao', size=(30, 0)), sg.Input(size=(15, 0), key='cotacao')],
            [sg.Text('Local em Reais', size=(35, 0)), sg.Input(size=(15, 0), key='reais')],
            [sg.Text('Loc Moeda Original', size=(35, 0)), sg.Input(size=(15, 0), key='original')],
            [sg.Button('Confirmar Dados')]
        ]
        self.janela = sg.Window("Atualizador de Cotações").layout(layout)
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
tela = TelaPython()
tela.Iniciar()
