from ai import Ai
from human import Human
import time

class Game:
    def __init__(self):
        self.player_1 = Human
        self.ai = Ai('WORK')
    
    
    def run_game(self):        
        self.welcome_message()
        self.rules_of_the_game()
        self.determine_how_many_players()
        self.ai.choose_gesture()
        self.gameplay()

    
    def welcome_message(self):
        print('\nWelcome to RPSLS\nWho will be the winner?\nStart the game to find out!\n')

    def rules_of_the_game(self):
        print('The rules of the game are as follows!\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock')
    
    def determine_how_many_players(self):
        choice_made = False
        while choice_made == False:
            player_count = input("How many players will there be - 1 or 2? ")
            if player_count == "1":
                print("Player 1 vs. AI")
                choice_made = True
            elif player_count == "2":
                print("Player 1 vs Player 2")
                choice_made = True
                
    def gameplay(self):
        self.player_1.human_choice()


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



