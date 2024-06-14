import random

class Revolver:
    def __init__(self, size: int) -> None:
        self.size = size
        self.chamber = [False for x in range(size)]
        self.round = 0
    
    def load(self, bullets: int) -> None:
        self.chamber[:bullets] = [True] * bullets
        
    def spin(self) -> None:
        random.shuffle(self.chamber)
    
    def fire(self) -> bool:
        '''
        fires a single shot from the revolver
        returns True if shot was bullet
        returns False if shot was blank
        '''
        curr_round = self.chamber[self.round]
        if curr_round:
            self.chamber[self.round] = False
        self.round += 1
        return curr_round
    
    def empty(self) -> None:
        self.chamber = [False for x in range(self.size)]

    def __str__(self) -> str:
        return str(self.chamber)
    