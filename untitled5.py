# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y_6pHCLjy7dqhOZ1IPHPB6CbjtcI5nnA
"""

from time import sleep
class Carro(object):

  def __init__(self, cor: str, modelo: str, ano: int):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano

  def abastecer (self,valor_abastecido: int)-> None:
      for valor in range(1, valor_abastecido+1):
        print(f'abastecendo: {valor}')
        sleep(1)

  def dirigir (self, abastecido: int, km_por_litro:float)-> None:
    rodado = abastecido * km_por_litro
    print(f"você dirigiu por {int(rodado)}KM")

  def __str__ (self) -> str:

    return f'Seu carro é um {self.modelo}, da cor {self.cor}, do ano {self.ano}'

carro1 = Carro(cor = 'preta',modelo = 'prisma',ano = 2015)

print(carro1)

carro1.abastecer(5)
carro1.dirigir(50, 3.89)

class Caminhao(Carro):
  def __init__(self, cor: str, modelo: str, ano: int, eixos: int):
    super().__init__(cor = cor, modelo = modelo, ano = ano)
    self.eixos = eixos

# Commented out IPython magic to ensure Python compatibility.
# 
# %%writefile musica.txt
# Roda Viva
# Chico Buarque
# 
# Tem dias que a gente se sente
# Como quem partiu ou morreu
# A gente estancou de repente
# Ou foi o mundo então que cresceu
# A gente quer ter voz ativa
# No nosso destino mandar
# Mas eis que chega a roda viva
# E carrega o destino pra lá
# 
# Roda mundo, roda-gigante
# Roda moinho, roda pião
# 
# O tempo rodou num instante
# Nas voltas do meu coração
# A gente vai contra a corrente
# Até não poder resistir
# Na volta do barco é que sente
# O quanto deixou de cumprir
# Faz tempo que a gente cultiva
# A mais linda roseira que há
# Mas eis que chega a roda viva
# E carrega a roseira pra lá
# 
# Roda mundo, roda-gigante
# Roda moinho, roda pião
# 
# 
#

class ArquivoTxt(object):
  def __init__(self, arquivo: str):
    self.arquivo = arquivo
    self.conteudo = []
  def ler_conteudo(self):
    with open(file= './'+ self.arquivo, mode = 'r', encoding= 'utf8') as fp:
      linha = fp.readline()
      while linha:
        self.conteudo.append(linha)
        linha = fp.readline()

  def extrair_linha (self, indice: int):
   return self.conteudo[indice]

e = ArquivoTxt(arquivo='musica.txt')
e.ler_conteudo()
print(e.conteudo)
e.extrair_linha(6)

lista= ['1', '2 ']
print(lista[1])