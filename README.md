
# Web scraping

Projeto desenvolvido na disciplina de Tópicos avançados de Banco de dados.

Através deste scrapping conseguimos obter informações das melhores marcas de acordo com o ranking : "www.rankingthebrands.com"
guardando os dados num objeto JSON.




## Instalação

Para executar o crawler é necessário o pacote venv (Virtual enviroment)

```bash
  cd my-project
  pip install virtualenv
```
Após a instalação basta ativar dentro do projeto:

```bash
  cd my-project
  .\venv\Scripts\activate.bat
```
## Execução

Para rodar o scrapping, execute o seguinte comando:

```bash
  scrapy runspider myspider.py
```

