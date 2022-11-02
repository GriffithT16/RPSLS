from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def human_choice(self):
        print("Choose 0 for rock.\nChoose 1 for paper.\nChoose 2 for scissors.\nChoose 3 for lizard.\nChoose 4 for spock.")
        choice_made = False
        while choice_made == False:
            gesture_chosen = input("Choose your gesture: ")
            if gesture_chosen == "0":
                self.gesture_chose = "rock"
                choice_made = True
            elif gesture_chosen == "1":
                self.gesture_chosen = "paper"
                choice_made = True
            elif gesture_chosen == "2":
                self.gesture_chosen = "scissors"
                choice_made = True
            elif gesture_chosen == "3":
                self.gesture_chosen = "lizard"
                choice_made = True
            elif gesture_chosen == "4":
                self.gesture_chosen = "spock"
                choice_made = True


