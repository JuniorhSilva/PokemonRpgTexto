from pokemon import *
from pessoa import Pessoa


class Pocao(Pokemon, Pessoa):
    def __init__(self, pokemon=None, jcoin=0):
        self.pokemon = pokemon
        self.preco = 350
        self.jcoin = jcoin

    def funcao_pocao(self):
        pass


class Curar(Pocao):
    def funcao_pocao(self, saldo):
        if saldo > self.preco:
            print('Curando...')
            sleep(1.5)
            curar_pokemon = self.pokemon
            print(f'Preco de cura: {self.preco}')
            novo = saldo - self.preco
            curar_pokemon.vida = curar_pokemon.level * 10
        else:
            print('sem saldo')
        return self.preco
