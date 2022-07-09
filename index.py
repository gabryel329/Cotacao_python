from tkinter import *
import requests
import json
import datetime

def pegar_cotacao():
    
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")#pega a informacao
    cotacoes = cotacoes.json()#converter o formato json em python

    cotacao_euro = cotacoes['EURBRL']['bid']#filtrando apenas campo do valor euro
    cotacao_bit = cotacoes['BTCBRL']['bid']#filtrando apenas campo do valor bitcoin
    cotacao_dolar = cotacoes['USDBRL']['bid']#filtrando apenas campo do valor dolar

    agora = datetime.datetime.now()#pegando a hora atual
    strt=str(agora)#convertendo e pegando apenas data e hora

    texto = f'''
    Euro: {cotacao_euro} 
        Bitcoin: {cotacao_bit} 
    Dolar: {cotacao_dolar}

    Data/Hora: {strt[0:19]}'''

    texto_cotacao["text"] = texto

janela = Tk()
janela.title("Cotacao") #colocando texto na janela
janela.geometry("225x250")#editando o tamanho da janela

texto_orientacao = Label(janela, text="Clique no botao para exibir a cotacao")#inserindo texto na pagina
texto_orientacao.grid(column=1, row=1, padx=10, pady=10)

botao = Button(janela, text="Buscar cotacao do Dolar/Euro/BTC", command=pegar_cotacao)#botao direcionado com command para pega a cotacao
botao.grid(column=1, row=3, padx=10, pady=10)

texto_cotacao = Label(janela, text="")#aqui sera exibido o resultado
texto_cotacao.grid(column=1, row=5, padx=10, pady=10)

janela.mainloop()
