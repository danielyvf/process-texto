import bs4 as bs 
import urllib.request 
import re 
import nltk 
import spacy
import numpy as np 
import random 
import string 

nltk.download('punkt')

dados = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial') 
dados = dados.read('utf-8')
dados_html = bs.BeautifulSoup(dados, 'lxml') 
paragrafos = dados_html.find_all('p') 
paragrafos[0].text
conteudo = ''

for p in paragrafos: 
    conteudo += p.text
    conteudo = conteudo.lower()

    lista_sentencas = nltk.sent_tokenize(conteudo)

    pln = spacy.load('pt_core_news_sm')

    stop_words = spacy.lang.pt.stop_words.STOP_WORDS
    string.punctuation



def preprocessamento(texto):

    texto = re.sub(r"https?://[A-Za-z0-9./]+", ' ', texto) 
    texto = re.sub(r" +", ' ', texto)
    documento = pln(texto)
    lista = [token.lemma_ for token in documento if token.text not in stop_words and token.text not in string.punctuation]

    lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])
    
    return lista 

url = 'https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial'
with urllib.request.urlopen(url) as response:
    dados = response.read().decode('utf-8')

lista_sentencas = re.split(r'(?<=[.!?]) +', dados)  
texto = lista_sentencas[0]  

resultado = preprocessamento(texto)








