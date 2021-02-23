from random import random, randint
from time import sleep

class Pokemon:
    def __init__(self, nome=None, level=None):
        self.nome = nome
        if level is None:
            level = randint(1, 100)
        self.level = level
        self.atk = level * 2
        self.vida = level * 10

    def __str__(self):
        return f'{self.nome} lvl.{self.level}'

    def atacar(self, pokemon_atk):
        if self.vida > 0:
            total_atk = int(self.atk * (random() * 1.5))
            sleep(1.0)
            pokemon_atk.vida -= total_atk
            print(f'{pokemon_atk} perdeu {total_atk}pts de vida')
            if pokemon_atk.vida <= 0:
                pokemon_atk.vida = 0
                self.vida = 0
                print(f'{pokemon_atk} foi derrotado')
                return pokemon_atk.vida
            else:
                return pokemon_atk.vida


class PokemonEletrico(Pokemon):
    def atacar(self, pokemon_atk):
        print(f'{self} lancou uma raio em {pokemon_atk}')
        return super().atacar(pokemon_atk)


class PokemonFogo(Pokemon):
    def atacar(self, pokemon_atk):
        print(f'{self} lancou uma bola de fogo em {pokemon_atk}')
        return super().atacar(pokemon_atk)


class PokemonAgua(Pokemon):
    def atacar(self, pokemon_atk):
        print(f"{self} lancou um jato d'gua em {pokemon_atk}")
        return super().atacar(pokemon_atk)
