class Player:
    def __init__(self, name):
        self.name = name
        self.gesture_options = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.gesture_chosen = ""
        self.total_wins = 0
    
    def choose_gesture(self):
        print("Choose 0 for rock.\nChoose 1 for paper.\nChoose 2 for scissors.\nChoose 3 for lizard.\nChoose 4 for spock.")
        choice_made = False
        while choice_made == False:
            number_chosen = int(input("Choose your gesture: "))
            if number_chosen >= 0 and number_chosen <= 4:
                choice_made = True
            else:
                print("Poor choice")

        self.gesture_chosen = self.gesture_options[number_chosen]

            
                
            
            


        # self.gesture_chosen

    
    