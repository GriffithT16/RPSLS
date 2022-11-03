from player import Player
import random

class Ai(Player):
    def __init__(self, name):
        super().__init__(name)
            

    def choose_gesture(self):
        self.gesture_chosen = random.choice(self.gesture_options)
        
       
    
        