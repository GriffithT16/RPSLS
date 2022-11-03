from player import Player
from ai import Ai
from human import Human
import time
import antigravity

class Game:
    def __init__(self):
        self.player_1 = None
        self.player_2 = None
    
    
    def run_game(self):
        self.welcome_message()
        self.rules_of_the_game()
        self.determine_how_many_players()
        self.gameplay()
        self.check_total_wins()
    
    def welcome_message(self):
        print('\nWelcome to RPSLS\nWho will be the winner?\nStart the game to find out!\n')
        time.sleep(3)

    def rules_of_the_game(self):
        print('The rules of the game are as follows!\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock')
        time.sleep(6)

    def determine_how_many_players(self):
        choice_made = False
        while choice_made == False:
            player_count = input("\nHow many players will there be - 1 or 2?\nEnter 3 for AI vs AI.\n")
            if player_count == "1":
                self.player_1 = Human('')
                self.player_2 = Ai('Computer')
                self.player_1.name = input("\nInput player 1's name here:\n")
                print(f"\n{self.player_1.name} vs. AI\n")
                choice_made = True
            elif player_count == "2":
                self.player_1 = Human('')
                self.player_2 = Human('')
                self.player_1.name = input("\nInput player 1's name here:\n")
                self.player_2.name = input("\nInput player 2's name here:\n")
                print(f"\n{self.player_1.name} vs {self.player_2.name}\n")
                choice_made = True
            elif player_count == "3":
                self.player_1 = Ai('Dell')
                self.player_2 = Ai('Macintosh')
                print(f"{self.player_1.name} vs. {self.player_2.name}")
                choice_made = True
                
    def gameplay(self):
        print(f"{self.player_1.name}'s turn")
        time.sleep(1.25)
        self.player_1.choose_gesture()
        print(f"\n{self.player_1.name} has chosen {self.player_1.gesture_chosen}!\n")
        time.sleep(1.25)
        print(f"{self.player_2.name}'s turn")
        time.sleep(1.25)
        self.player_2.choose_gesture()
        print(f"\n{self.player_2.name} has chosen {self.player_2.gesture_chosen}!\n")
        time.sleep(1.25)
        self.determine_winner()


    def determine_winner(self):
        if self.player_1.gesture_chosen == self.player_2.gesture_chosen:
            self.player_1.total_wins += 0
            self.player_2.total_wins += 0
        elif self.player_1.gesture_chosen == "rock" and self.player_2.gesture_chosen == "spock":
            self.player_2.total_wins += 1
            print(f"{self.player_2.name} has {self.player_2.total_wins} wins!")
        elif self.player_1.gesture_chosen == "rock" and self.player_2.gesture_chosen == "paper":
            self.player_2.total_wins += 1
            print(f"{self.player_2.name} has {self.player_2.total_wins} wins!")
        elif self.player_1.gesture_chosen == "rock" and self.player_2.gesture_chosen == "lizard":
            self.player_1.total_wins += 1
            print(f"{self.player_1.name} has {self.player_1.total_wins} wins!")
        elif self.player_1.gesture_chosen == "rock" and self.player_2.gesture_chosen == "scissors":
            self.player_1.total_wins += 1
            print(f"{self.player_1.name} has {self.player_1.total_wins} wins!")
        elif self.player_1.gesture_chosen == "spock" and self.player_2.gesture_chosen == "rock":
            self.player_1.total_wins += 1
            print(f"{self.player_1.name} has {self.player_1.total_wins} wins!")
        elif self.player_1.gesture_chosen == "spock" and self.player_2.gesture_chosen == "paper":
            self.player_2.total_wins += 1
            print(f"{self.player_2.name} has {self.player_2.total_wins} wins!")
        elif self.player_1.gesture_chosen == "spock" and self.player_2.gesture_chosen == "lizard":
            self.player_2.total_wins += 1
            print(f"{self.player_2.name} has {self.player_2.total_wins} wins!")
        elif self.player_1.gesture_chosen == "spock" and self.player_2.gesture_chosen == "scissors":
            self.player_1.total_wins += 1
            print(f"{self.player_1.name} has {self.player_1.total_wins} wins!")
        elif self.player_1.gesture_chosen == "paper" and self.player_2.gesture_chosen == "rock":
            self.player_1.total_wins += 1
            print(f"{self.player_1.name} has {self.player_1.total_wins} wins!")
        elif self.player_1.gesture_chosen == "paper" and self.player_2.gesture_chosen == "spock":
            self.player_1.total_wins += 1
            print(f"{self.player_1.name} has {self.player_1.total_wins} wins!")
        elif self.player_1.gesture_chosen == "paper" and self.player_2.gesture_chosen == "lizard":
            self.player_2.total_wins += 1
            print(f"{self.player_2.name} has {self.player_2.total_wins} wins!")
        elif self.player_1.gesture_chosen == "paper" and self.player_2.gesture_chosen == "scissors":
            self.player_2.total_wins += 1
            print(f"{self.player_2.name} has {self.player_2.total_wins} wins!")
        elif self.player_1.gesture_chosen == "lizard" and self.player_2.gesture_chosen == "rock":
            self.player_2.total_wins += 1
            print(f"{self.player_2.name} has {self.player_2.total_wins} wins!")
        elif self.player_1.gesture_chosen == "lizard" and self.player_2.gesture_chosen == "spock":
            self.player_1.total_wins += 1
            print(f"{self.player_1.name} has {self.player_1.total_wins} wins!")
        elif self.player_1.gesture_chosen == "lizard" and self.player_2.gesture_chosen == "paper":
            self.player_1.total_wins += 1
            print(f"{self.player_1.name} has {self.player_1.total_wins} wins!")
        elif self.player_1.gesture_chosen == "lizard" and self.player_2.gesture_chosen == "scissors":
            self.player_2.total_wins += 1
            print(f"{self.player_2.name} has {self.player_2.total_wins} wins!")
        elif self.player_1.gesture_chosen == "scissors" and self.player_2.gesture_chosen == "rock":
            self.player_2.total_wins += 1
            print(f"{self.player_2.name} has {self.player_2.total_wins} wins!")
        elif self.player_1.gesture_chosen == "scissors" and self.player_2.gesture_chosen == "spock":
            self.player_2.total_wins += 1
            print(f"{self.player_2.name} has {self.player_2.total_wins} wins!")
        elif self.player_1.gesture_chosen == "scissors" and self.player_2.gesture_chosen == "paper":
            self.player_1.total_wins += 1
            print(f"{self.player_1.name} has {self.player_1.total_wins} wins!")
        elif self.player_1.gesture_chosen == "scissors" and self.player_2.gesture_chosen == "lizard":
            self.player_1.total_wins += 1
            print(f"{self.player_1.name} has {self.player_1.total_wins} wins!")

    def check_total_wins(self):
        while self.player_1.total_wins < 2 and self.player_2.total_wins < 2:
            self.gameplay()
        if self.player_1.total_wins == 2:
            print(f"{self.player_1.name} wins the best of three!")
        elif self.player_2.total_wins == 2:
            print(f"{self.player_2.name} wins the best of three!")
            
    
        


   


