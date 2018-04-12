import requests
from bs4 import BeautifulSoup as bs


class GetInfoVagas():
    """
    Classe para processar os dados html e retornar as informações das vagas
    """

    def __init__(self, link):
        self.link = link
        self.pg_conteudo = self.get_pg_vaga()
        self.nome = self.get_nome()
        self.nome_empresa = self.get_nome_empresa()
        self.desc_vaga = self.get_descricao_vaga()

    def get_pg_vaga(self):
        """
        método para pegar o conteudo da página referente a uma vaga
        """
        print(self.link)
        pg_vaga = requests.get(self.link)
        conteudo_pg = bs(pg_vaga.content, 'html.parser')
        return conteudo_pg


    def get_nome(self):
        """
        método para pegar o nome da vaga publicada
        """
        soup = self.pg_conteudo
        div_nome = soup.find_all('div', class_='advisor-card header-advisor advisor-basic')
        nome_vaga = div_nome[0].find('h1').get_text()
        return nome_vaga


    def get_nome_empresa(self):
        """
        método para retornar o nome da empresa que publicou a vaga
        """
        soup = self.pg_conteudo
        div_nome = soup.find_all('div', class_='advisor-card header-advisor advisor-basic')
        nome_empresa = div_nome[0].find('div', class_='divName jsCompanyName').find('h1').get_text()
        return nome_empresa


    def get_descricao_vaga(self):
        """
        método para coletar a descrição da vaga
        """
        soup = self.pg_conteudo
        div_desc = soup.find('div', class_='advisor-vacancy-detail').find_all('ol')
        conteudo = str(div_desc).split('</ol>')
        descricao_processada = self.limpa_descricao(conteudo)
        return descricao_processada


    def limpa_descricao(self, conteudo):
        """
        método para limpar o conteúdo da descrição do método
        get_descricao_vaga
        """
        info = conteudo[0]
        exigencias = conteudo[1]

        #limpando a info
        linhas = str(info).split('</li>')
        linhas_sem_li = [text.replace('<li>', '') for text in linhas]
        process = ''
        process = process.join(linhas_sem_li)
        pos_maior = process.find('>')
        info = process[pos_maior+1:]

        #limpando as exigencias
        linhas = exigencias.split('\n')

        #-- Removendo comentário do conteudo e também a abertura de tag ol
        linhas = [text for text in linhas if '<!--' not in text and text != linhas[0]]
        sem_li = ''
        for linha in linhas:
            pos_maior = linha.find('>')
            sem_li += (linha[pos_maior+1:-5])

        descricao = {
            'info': info,
            'exigencias': sem_li,
        }

        return descricao
