from model.revolver import Revolver
from model.game import Game
from model.player import Player

player_name = input('enter player name: ')
size = int(input('how many spots in the chamber? '))

# initialize game with empty revolver
print(f'creating game with {size}-shooter revolver...')
game = Game(player_name, size)
print(game.players)

# load the revolver
num_shots = int(input('how mnay shots do you want to load? '))
print(f'loading {num_shots} bullets into the revolver...')
game.revolver.load(num_shots)

# spin the drum
game.revolver.spin()
print('spinning the drum...')

while game.curr_player.is_alive:
    fire_confirm = input('do you want to fire? ')
    if fire_confirm == 'yes':
        target = game.curr_player
        shot_result = game.revolver.fire()
        if shot_result:
            target.take_hit()
        else:
            print('Empty round')
    game.next_turn

print('You died')