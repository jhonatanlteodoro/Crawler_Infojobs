import requests
from bs4 import BeautifulSoup as bs


class GetLinksVagas():
    """
    Classe para pegar os links das vagas
    o link pode ser alterado na chamada. Neste exemplo usei só dois filtros do
    info jobs mas poderiamos entrar lá e selecionar os necessários e copiar o
    link.
    """

    def __init__(self):
        self.link = "https://www.infojobs.com.br/empregos.aspx?Palabra=programador&Provincia=64"
        self.list_links_vagas = self.get_links_vagas()

    def get_texts_vagas(self):
        """
        Método para buscar as vagas, retornando uma lista com todas as vagas
        que foram encontradas(sem processar o texto)
        """
        #pagina inicial tem parametros pré definidos
        page_inicial = requests.get(self.link)
        soup = bs(page_inicial.content, 'html.parser')
        text_list_vagas = soup.find_all('div', class_='vaga')
        return text_list_vagas


    def get_links_vagas(self):
        """
        Método para limpar os dados coletados de cada vaga para retirarmos apenas
        o link de cada vaga
        """
        text_vagas = self.get_texts_vagas()
        #limpando conteúdo para pegar o link de cada vaga
        link_vagas = [link.find('a').get('href') for link in text_vagas]
        return link_vagas
