from colorama import init
init()
from colorama import Fore
class TicTacToe:
    def __init__(self):
        self.rows, self.columns = 3, 3
        self.win = " "
        self.z = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turns = 0
        self.turn_counter = 2  # or 3 - 2 for even, 3 for odd

    def tictactoe_board_start(self, z):
        print(f"          x\n      1   2   3\n   1| {z[0][0]} | {z[1][0]} | {z[2][0]}\ny  2| {z[0][1]} | {z[1][1]} | {z[2][1]}\n   3| {z[0][2]} | {z[1][2]} | {z[2][2]}")

    def win_lose(self, z):
        for i in range(self.rows):
            if z[i][0] == z[i][1] == z[i][2] != ' ':
                return z[i][0]
        for i in range(self.columns):
            if z[0][i] == z[1][i] == z[2][i] != ' ':
                return z[0][i]
        if z[0][0] == z[1][1] == z[2][2] != ' ' or z[0][2] == z[1][1] == z[2][0] != ' ':
            return z[1][1]
        return " "

    def turner(self, num):
        if num % 2 == 0:
            return "o"
        else:
            return "x"
    def search_player(self,players,search_value):
        for y in range(1,3):
            if players["choice"][f"p_c_{y}"] == search_value:
                return players["names"][f"p_n_{y}"]

    def choices_inputs(self):
        choice = input("Enter Players Choice [ex x o]: ").split(" ")
        return choice

    def validate_choices(self):
        while True:
            choice = self.choices_inputs()
            if len(choice) != 2 :
                print("Please enter x o (or) o x.")
            if (choice[0] == "x" and choice[1] == "o") or (choice[0] == "o" and choice[1] == "x"):
                return choice
            else:
                print("Wrong Choice! Try Again")
            

    def names_inputs(self):
        names = input("Enter Players Names [ex tan dhar]: ").split(" ")
        return names

    def validate_names(self):
        while True:
            names = self.names_inputs()
            if len(names) != 2:
                print("Please enter exactly 2 player names.")
            else:
                return names
            
    def start(self):
        print('\033[H\033[J')
        print("Welcome To The Game: Tic Tac Toe")
        names = self.validate_names()
        print(f"Players: < {names[0].capitalize()}, {names[1].capitalize()} >")
        choice = self.validate_choices()
        if choice[0].lower() == choice[1].lower():
            print("Can't Select Like that Try Again")
            choice = self.choices_inputs()
        players = {
            "names": {
                "p_n_1": names[0].lower().capitalize(),
                "p_n_2": names[1].lower().capitalize()
            },
            "choice": {
                "p_c_1": choice[0].lower(),
                "p_c_2": choice[1].lower()
            }
        }
        for tr in range(self.rows * self.columns):
            for a in range(self.rows):
                for b in range(self.columns):
                    if self.turns == 0:
                        print('\033[H\033[J')
                        self.tictactoe_board_start(self.z)
                        self.turns += 1
                    value = self.turner(self.turns)
                    current_player = self.search_player(players, value)
                    print(f"Turn -> Current Player: {current_player} ({value})")
                    c, d = input("Coordinates (x,y): ").split(" ")
                    c = int(c) - 1
                    d = int(d) - 1
                    if c > 3 or d > 3:
                        print("Invalid Corrdinates!")
                        break
                    if self.z[c][d] != " ":
                        print("Already set!, you can't change")
                        break
                    else:
                        print('\033[H\033[J')
                        if value == 'x':
                            self.z[c][d] = "x"
                        elif value == 'o':
                            self.z[c][d] = "o"
                        self.tictactoe_board_start(self.z)
                        win = self.win_lose(self.z)
                        if win == "x":
                            print(Fore.YELLOW, f"{current_player}(X) won!")
                            exit()
                        elif win == "o":
                            print(Fore.YELLOW, f"{current_player} (O) won!")
                            exit()
                        elif win == " " and self.turns == 9:
                            print(Fore.RED, "It's a draw!")
                            exit()

                        else:
                            self.turns += 1
                            continue


game = TicTacToe()
game.start()
