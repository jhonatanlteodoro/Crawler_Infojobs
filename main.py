from get_links_vagas import GetLinksVagas as glv
from get_info_vagas import GetInfoVagas as giv


links = glv()
#Como exemplo vamos passar 3 links
vagas = []
for vaga in range(3):
    vagas.append(giv(links.list_links_vagas[vaga]))

print(vagas[0].nome)
print(vagas[0].nome_empresa)
print(vagas[0].desc_vaga)

print(vagas[1].nome)
print(vagas[1].nome_empresa)
print(vagas[1].desc_vaga)

print(vagas[2].nome)
print(vagas[2].nome_empresa)
print(vagas[2].desc_vaga)

"""
Este exemplo ainda possuí uma listagem limpa e muito menos exata de cada conteúdo
raspado, isso pois foi feito sem usar regex e só com o bs4 e o python fica díficil
limpar sem erros o conteúdo raspado
"""
