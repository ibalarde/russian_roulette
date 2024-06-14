from model.revolver import Revolver
from model.player import Player

class Game:
    def __init__(self, players: list[str], size: int = 6) -> None:
        self.players = []
        for name in players:
            self.players.append(Player(name))
        self.revolver = Revolver(size)
        self.curr_player_index = 0
        self.curr_player = self.players[self.curr_player_index]
    
    def next_turn(self) -> None:
        self.curr_player_index += 1
        if self.curr_player_index > len(self.players) - 1:
            self.curr_player_index = 0
