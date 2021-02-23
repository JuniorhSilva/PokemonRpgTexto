from pokemon import *
from pessoa import *
from pocao import *
from pickle import dump, load
from time import sleep


def escolher_pokemon_inicial(player_inicial):
    print('Escolha seu POKEMON!!')
    pikachu = PokemonEletrico('Pikachu', 1)
    squirtle = PokemonAgua('Squirtle', 1)
    charmander = PokemonFogo('Charmander', 1)
    print(f'1- {pikachu}\n2- {squirtle}\n3- {charmander}')
    while True:
        pokemon_escolhido = input('Escolha: ')
        if pokemon_escolhido == '1':
            player_inicial.capturar_pokemon(pikachu)
            break
        elif pokemon_escolhido == '2':
            player_inicial.capturar_pokemon(squirtle)
            break
        elif pokemon_escolhido == '3':
            player_inicial.capturar_pokemon(charmander)
            break
        else:
            print('Comando invalido!')


def salvar_jogo(player):
    try:
        with open('database', 'wb') as arquivo:
            dump(player, arquivo)
            return True
    except:
        print('Erro ao salvar')


def carregar_jogo():
    try:
        with open('database', 'rb') as arquivo:
            jogo_salvo = load(arquivo)
            return jogo_salvo
    except:
        print('Erro ao carregar')


if __name__ == '__main__':
    while True:
        print('-' * 34)
        print('    Bem vindo ao mundo POKEMON')
        print('-' * 34)
        print('\t1- Novo Jogo\n\t2- Carregar Jogo\n\t0- Sair')
        print('-' * 34)
        pergunta_usuario = input('Escolha: ')
        if pergunta_usuario == '1':
            nome = input('Digite seu nome: ')
            usuario_player = Player(nome)
            print(f'Ola {nome}, Voce tem um grande desafio pela frente')
            print('Voce comeca com uma quantidade de Jcoin')
            print('Voce podera ganhar mais Lutando com Inimigos')
            usuario_player.mostrar_jcoin()
            print('Voce precisa de um Pokemon Inicial!')
            escolher_pokemon_inicial(usuario_player)
            print('Voce Enfretara seu Primeiro Inimigo, Prepare-se!')
            inimigo = Inimigo('Gary', [PokemonAgua('Squirtle', 1)])
            usuario_player.batalha_contra_inimigos(inimigo)
            salvar_jogo(usuario_player)
            break
        elif pergunta_usuario == '2':
            usuario_player = carregar_jogo()
            break
        elif pergunta_usuario == '0':
            print('Saindo...')
            sleep(1.5)
            exit(0)
        else:
            print('Comando Invalido')

while True:
    print('-' * 34)
    print('\t-----MENU-----')
    print('\t1- Explorar\n'
          '\t2- Lutar\n'
          '\t3- Saldo\n'
          '\t4- Meus Pokemons\n'
          '\t5- Loja de Poções\n'
          '\t6- Vender Pokemon\n'
          '\t0- sair')
    print('-' * 34)
    escolha = input('Escolha: ')
    if escolha == '1':
        usuario_player.explorar()
        salvar_jogo(usuario_player)
    elif escolha == '2':
        inimigo_batalha = Inimigo()
        usuario_player.batalha_contra_inimigos(inimigo_batalha)
        salvar_jogo(usuario_player)
    elif escolha == '3':
        usuario_player.mostrar_jcoin()
        salvar_jogo(usuario_player)
    elif escolha == '4':
        usuario_player.mostrar_pokemons()
        salvar_jogo(usuario_player)
    elif escolha == '5':
        print('Centro de cura SUSKEMON')
        pokemon_curar = usuario_player.escolher_pokemon()
        pocao_cura = Curar(pokemon_curar)
        novo_saldo = pocao_cura.funcao_pocao(usuario_player.jcoin)
        usuario_player.perder_jcoin(novo_saldo)
        salvar_jogo(usuario_player)
    elif escolha == '6':
        usuario_player.vender_pokemon()
    elif escolha == '0':
        print('Saindo...')
        salvar_jogo(usuario_player)
        sleep(1.5)
        break
