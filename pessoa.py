from pokemon import *
from random import choice, random, randint

NOMES = ['Eric', 'Aurora', 'Pedro', 'Chris', 'Felipe', 'Jane', 'Bernado', 'Oliver',
         'Lucifer', 'Abel', 'Jesus', 'Flavia', 'Rebeca', 'Jaqueline', 'Gary']

POKEMONS = [
    PokemonFogo('Charmander'), PokemonFogo(
        'Charizard'), PokemonFogo('Magmar'), PokemonFogo('Flareon'),
    PokemonFogo('Combusken'), PokemonEletrico('Pikachu'), PokemonEletrico(
        'Ampharos'), PokemonEletrico('Manectric'),
    PokemonEletrico('Elekid'), PokemonEletrico(
        'Jolteon'), PokemonAgua('Squirtle'), PokemonAgua('Blastoise'),
    PokemonAgua('Psyduck'), PokemonAgua('Golduck'), PokemonAgua('Slowpoke')
]


class Pessoa():
    def __init__(self, nome=None, pokemons=None, jcoin=1000):
        if pokemons is None:
            pokemons = []
        self.nome = nome
        self.jcoin = jcoin
        self.pokemons = pokemons

    def __str__(self):
        return f'{self.nome}'

    def mostrar_pokemons(self):
        print(f'Pokemons de {self}: ')
        if self.pokemons:
            for i, pokemon in enumerate(self.pokemons):
                print(f'{i+1}- {pokemon} hp.{pokemon.vida}')
        else:
            print(f'{self} não tem pokemon')

    def escolher_pokemon(self):
        if self.pokemons:
            escolha = choice(self.pokemons)
            print(f'{self} escolheu {escolha}')
            return escolha
        else:
            print(f'{self} não tem pokemons')

    def ganhar_jcoin(self, jcoin):
        self.jcoin += jcoin
        print(f'Voce ganhou: {jcoin}')
        self.mostrar_jcoin()
        return self.jcoin

    def perder_jcoin(self, jcoin):
        self.jcoin -= jcoin
        print(f'NPC pegou um total de: {jcoin} Jcoins')
        if self.jcoin < 0:
            print(f'Conta nao pode ficar negativa')
            self.jcoin = 0
        self.mostrar_jcoin()
        return self.jcoin

    def mostrar_jcoin(self):
        print(f'Total de Jcoin: {self.jcoin}')

    def batalha_contra_inimigos(self, inimigo):
        if self.jcoin > 500:
            print(f'Inimigo: {inimigo}')
            inimigo.mostrar_pokemons()
            while True:
                pergunta = input(f'Batalhar com {inimigo}? [s/n]: ')
                if pergunta == 's':
                    pokemon_inimigo = inimigo.escolher_pokemon()
                    pokemon_escolhido = self.escolher_pokemon()
                    if pokemon_escolhido.vida > 0:
                        print(f'{inimigo} escolheu {pokemon_inimigo}')
                        if pokemon_escolhido and pokemon_inimigo:
                            while True:
                                vitoria_player = pokemon_escolhido.atacar(
                                    pokemon_inimigo)
                                if vitoria_player == 0:
                                    self.ganhar_jcoin(
                                        pokemon_inimigo.level * 10)
                                    break
                                vitoria_inimigo = pokemon_inimigo.atacar(
                                    pokemon_escolhido)
                                if vitoria_inimigo == 0:
                                    self.perder_jcoin(
                                        pokemon_inimigo.level * 4)
                                    break
                    else:
                        print('Cure seu Pokemon!')
                    break
                elif pergunta == 'n':
                    print(f'{self} correu da batalha')
                    break
                else:
                    print('Comando invalido')
                    continue
        else:
            ('Jcoins insuficientes')


class Player(Pessoa):
    def escolher_pokemon(self):
        self.mostrar_pokemons()
        while True:
            escolhido = input('Escolha um pokemon: ')
            try:
                escolhido = int(escolhido)
                if escolhido > 0:
                    escolhido -= 1
                    pokemon_escolhido = self.pokemons[escolhido]
                    print(
                        f'{self} escolheu {pokemon_escolhido}')
                    break
                else:
                    print('Pokemon nao existe')
            except IndexError:
                print('Pokemon nao existe')
                continue
            except ValueError:
                print('Pokemon nao existe')
                continue
        return pokemon_escolhido

    def capturar_pokemon(self, pokemon):
        print('Capturando...')
        sleep(1.5)
        rng_capturar = random()
        if self.pokemons:
            if pokemon.level < 50:
                rng_capturar += 0.3
            if rng_capturar > 0.7:
                self.pokemons.append(pokemon)
                print(f'{self} capturou {pokemon}')
            else:
                print(f'{pokemon} fugiu!')
        else:
            self.pokemons.append(pokemon)
            print(f'Voce capturou {pokemon}')

    def explorar(self):
        print('Explorando...')
        sleep(2.5)
        rng = random()
        if rng > 0.4:
            pokemon_selvagem = choice(POKEMONS)
            print(f'Voce encontrou um {pokemon_selvagem}')
            while True:
                print(f'1- Capturar\n2- Batalhar\n3- Fugir ')
                pergunta = input('Escolha sua Opcao: ')
                if pergunta == '1':
                    self.capturar_pokemon(pokemon_selvagem)
                    break
                elif pergunta == '2':
                    self.batalha_pokemon_selvagem(pokemon_selvagem)
                    break
                elif pergunta == '3':
                    print('Fugindo...')
                    break
                else:
                    print('comando invalido')
        else:
            print('Nada encontrado')

    def batalha_pokemon_selvagem(self, pokemon):
        pokemon_escolhido = self.escolher_pokemon()
        if pokemon_escolhido and pokemon:
            while True:
                vitoria_player = pokemon_escolhido.atacar(pokemon)
                if vitoria_player == 0:
                    self.capturar_pokemon(pokemon)
                    return True
                vitoria_pokemon = pokemon.atacar(pokemon_escolhido)
                if vitoria_pokemon == 0:
                    return True

    def vender_pokemon(self):
        pokemon_escolhido = self.escolher_pokemon()
        index_pokemon = self.pokemons.index(pokemon_escolhido)
        self.pokemons.pop(index_pokemon)
        self.ganhar_jcoin(pokemon_escolhido.level * 7)


class Inimigo(Pessoa):
    def __init__(self, nome_i=None, pokemons=None):
        if nome_i is None:
            nome_i = choice(NOMES)
        if pokemons is None:
            pokemons = []
        if not pokemons:
            for qtd_pokemon in range(randint(1, 6)):
                pokemons.append(choice(POKEMONS))
        super().__init__(nome_i, pokemons)
