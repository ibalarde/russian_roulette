class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.shakiness = 0.0
        self.is_alive = True
        self.items = []
    
    def take_hit(self) -> None:
        self.is_alive = False