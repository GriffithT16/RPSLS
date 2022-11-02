from player import Player
from ai import Ai

class Game:
    
    
    def run_game(self):
        self.welcome_message()
    
    
    def welcome_message(self):
        print('\nWelcome to RPSLS\nWho will be the winner?\nStart the game to find out!\n')
    
    def name_to_number(name):
        if name == "rock":
            return 0
        elif name == "paper":
            return 1
        elif name == "scissors":
            return 2
        elif name == "lizard":
            return 3
        elif name == "spock":
            return 4
        else:
            return name + "is not a valid choice"


    def number_to_name(number):
        if number == 0:
            return "rock"
        elif number == 1:
            return "paper"
        elif number == 2:
            return "scissors"
        elif number == 3:
            return "lizard"
        elif number == 4:
            return "spock"
        else:
            return "Enter number 0-4"

    
        self.ai_choice()