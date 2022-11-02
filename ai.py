from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
        self.choice = random.choice()

    def ai_choice(self):
        self.choice = random.choice(self.gesture_chosen)