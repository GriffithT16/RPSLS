from player import Player


class Human(Player):
    def __init__(self, name):
        super().__init__(name)
       

    

            # if gesture_chosen == "0":
            #     self.gesture_chosen = "rock"
            #     choice_made = True
            # elif gesture_chosen == "1":
            #     self.gesture_chosen = "paper"
            #     choice_made = True
            # elif gesture_chosen == "2":
            #     self.gesture_chosen = "scissors"
            #     choice_made = True
            # elif gesture_chosen == "3":
            #     self.gesture_chosen = "lizard"
            #     choice_made = True
            # elif gesture_chosen == "4":
            #     self.gesture_chosen = "spock"
            #     choice_made = True


    def choice_compare(self):
        self.human_choice.gesture_chosen