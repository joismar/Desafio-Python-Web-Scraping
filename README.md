<h1 align="center">Desafio Python Web Scraping</h1>

<p align="center">
  <img alt="Principal linguagem do projeto" src="https://img.shields.io/github/languages/top/joismar/Desafio-Python-Web-Scraping?color=56BEB8">

  <img alt="Quantidade de linguagens utilizadas" src="https://img.shields.io/github/languages/count/joismar/Desafio-Python-Web-Scraping?color=56BEB8">

  <img alt="Tamanho do repositório" src="https://img.shields.io/github/repo-size/joismar/Desafio-Python-Web-Scraping?color=56BEB8">

  <img alt="Licença" src="https://img.shields.io/github/license/joismar/Desafio-Python-Web-Scraping?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/joismar/Desafio-Python-Web-Scraping?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/joismar/Desafio-Python-Web-Scraping?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/joismar/Desafio-Python-Web-Scraping?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Desafio Python   Web Scraping 🚀 Em construção...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-sobre">Sobre</a> &#xa0; | &#xa0; 
  <a href="#sparkles-funcionalidades">Funcionalidades</a> &#xa0; | &#xa0;
  <a href="#rocket-tecnologias">Tecnologias</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-pré-requesitos">Pré requisitos</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-começando">Começando</a> &#xa0; | &#xa0;
  <a href="#memo-licença">Licença</a> &#xa0; | &#xa0;
  <a href="https://github.com/joismar" target="_blank">Autor</a>
</p>

<br>

## :dart: Sobre ##

O projeto a seguir aborda diferentes formas de realizar Web Scraping.

## :sparkles: Objetivos ##

:heavy_check_mark: Realizar Web Scraping em uma página do Olhar Digital utilizando [Scrapy](https://scrapy.org/);\
:heavy_check_mark: Realizar Web Scraping na primeira página do Airbnb realizando busca por localidade utilizando [Scrapy](https://scrapy.org/);\
:heavy_check_mark: Realizar Web Scraping na primeira página do Airbnb realizando busca por localidade utilizando [Selenium](https://selenium-python.readthedocs.io/) com [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/);\
:heavy_check_mark: Realizar Web Scraping na primeira página de anúncios do Mercado Livre realizando uma busca utilizando o método que julgo mais apropriado.

## :rocket: Tecnologias ##

As seguintes ferramentas foram usadas:

- [Scrapy](https://scrapy.org/)
- [Selenium](https://selenium-python.readthedocs.io/)
- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## :white_check_mark: Pré requisitos ##

Antes de começar :checkered_flag:, você precisa ter o [Git](https://git-scm.com) e o [Python](https://www.python.org/) instalados em sua maquina.

## :checkered_flag: Começando ##
#### Primeiramente...

```bash
# Clone este repositório
$ git clone https://github.com/joismar/Desafio-Python-Web-Scraping

# Entre na pasta
$ cd Desafio-Python-Web-Scraping
```
#### Scrapy
Nessa pasta estão dois scrapers, na pasta spiders pode ser encontrado dois spiders que cumprem os dois primeiros objetivos, abra os arquivos para ver as explicações.
Para rodar siga os passos abaixo...
```bash
# Vá até a pasta
$ cd scrapy

# Instale as dependencias
$ poetry install --no-root
# Ou instale com o seu gerenciador de dependencias preferido

# Execute os spiders com o comando
$ poetry run scrapy crawl NOME_DO_SPIDER

# Caso tenha instalado as dependencias localmente
$ scrapy crawl NOME_DO_SPIDER
```

#### Selenium
Nessa pasta estão dois scrapers que cumprem os objetivos um e dois utilizando Selenium, abra os arquivos para ler as explicações.
Para rodar os Bots siga os passos abaixo...
```bash
# Vá até a pasta
$ cd selenium

# Instale as dependencias
$ poetry install --no-root
# Ou instale com o seu gerenciador de dependencias preferido

# Execute os spiders com o comando
$ poetry run python main_NOME_DO_BOT.py

# Caso tenha instalado as dependencias localmente
$ python main_NOME_DO_BOT.py
```

## :memo: Licença ##

Este projeto está sob licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.


Feito com :heart: por <a href="https://github.com/joismar" target="_blank">Joismar Braga</a>

&#xa0;

<a href="#top">Voltar para o topo</a>
