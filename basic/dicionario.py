### IMPORTANDO BIBLIOTECLAS ###

from teste_importacao.classes import *
import os

### TIPOS DE DADOS ###

nome = "erick" # string
idade = 17 # int
dinheiro = 52.9 # float
cnh = False # boolean
not cnh # negando
bolso = ["chave", "celular", "carteira"] # lista / array
pessoa_erick = {"nome":"erick", "idade":"17", "dinheiro":"52,9"} # dicionario
carteira = {"dinheiro", "moedas", "cartao_credito"} # set (nao permite elementos repetidos)

### CONDICIONAIS / LAÇOS DE REPETIÇÃO ###

if idade >= 18:
    print()

elif idade == 17:
    print()

else:
    print()

mensagem = 'isso' if cnh == True else 'aquilo' # if em uma linha


contador = 0
while contador < 5:
    print(contador)
    contador += 1

# break usado para parar o codigo

for coisa in bolso:
    print(coisa)


comando = ""

match comando:
    case "entrar":
        print("Entrando")
    case "sair":
        print("Saindo")
    case _:
        print("Comando inválido")
    

### FUNÇÕES E CLASSES ###

class Pessoa():
    def __init__(self):
        self.nome = ""
        self.idade = 0

minha_pessoa = Pessoa()
minha_pessoa.nome = "erick"
minha_pessoa.idade = 17

print(f"meu nome é {minha_pessoa.nome}, e minha idade é {minha_pessoa.idade}")

class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria

    def __str__(self): #nao precisa chamar pois é o return da função
        return f"Restaurante: {self.nome} Categoria: {self.categoria}"

resultado = Restaurante("Sushi House", "Japonesa")
print(resultado)


dir() #exibe os metodos de uma classe
vars() # dicionario dos atributos e metodos
