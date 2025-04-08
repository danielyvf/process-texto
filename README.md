# Projeto de Processamento de Texto com BeautifulSoup, NLTK e spaCy

Este projeto realiza a extração e o processamento de dados de uma página da Wikipédia sobre "Inteligência Artificial". O código utiliza as bibliotecas BeautifulSoup para fazer scraping da página, NLTK para tokenização de sentenças e spaCy para o pré-processamento do texto (como remoção de stop words e lematização).


## Funcionalidades

- Extração de texto da Wikipédia: O código faz uma requisição HTTP para a página da Wikipédia sobre "Inteligência Artificial" e extrai o conteúdo textual dos parágrafos.

- Pré-processamento do texto: O texto extraído é processado com a remoção de URLs, espaços extras, e com a tokenização em sentenças.

- Uso de NLP (Processamento de Linguagem Natural):

- Tokenização de sentenças com o NLTK.

- Lematização e remoção de stop words com o spaCy.


## Requisitos

- Este projeto usa as seguintes bibliotecas externas:

- BeautifulSoup (para scraping de páginas web).

- NLTK (para tokenização e manipulação de texto).

- spaCy (para processamento de linguagem natural).

- urllib (para fazer requisições HTTP).
