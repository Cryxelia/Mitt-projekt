import os, random
from colored import fg


# platserna på spelbrädet
board = ["_", "_", "_",  
         "_", "_", "_", 
         "_" , "_", "_" ]    

print("\nVälkommen till tic-tac-toe!") 

game_mode  = input("\nvälj en eller två spelare: ")

# Vem som ska börja
if game_mode == "två spelare":
    player = fg('red') + "O" + "\033[0m"  # Färg för spelare 1 (röd O) och reset
    player2 = fg('blue') + "X" + "\033[0m"  # Färg för spelare 2 (blå X) och reset
elif game_mode == "en spelare":
    player = fg('red') + "O" + "\033[0m"  # Färg för spelare 1 (röd O) och reset
    computer = fg('blue') + "X" + "\033[0m"  # Färg för spelare 2 (blå X) och reset
else:
    print("du angav inget giltigt spelarläge")

current_player = player
winner = None
game_running = True
high_score_p1 = 0   # räknar spelare 1:s poäng
high_score_p2 = 0
high_score_single = 0  # räknar poäng när man spelar själv

# hur datorn gör drag
def computer_move():
    global computer
    valid_move = False
    while not valid_move:
        move = random.randint(0, 8)
        if board[move-1] == "_":
            board[move-1] = computer
            valid_move = True


score_file = "high_score.txt"
p2_score_file = "player2_highscore.txt"
single_mode = "single_score.txt"

# läser antalet vinster från filen
def read_high_score():
    if os.path.exists(score_file):
        with open(score_file, "r") as f:
            content = f.read().strip()
            if content:  
                return int(content)
    return 0 

def read_p2_score():
    if os.path.exists(p2_score_file):
        with open(p2_score_file, "r") as y:
            content_2 = y.read().strip()
            if content_2:  
                return int(content_2)
    return 0 

def read_single_score():
    if os.path.exists(single_mode):
        with open(single_mode, "r") as l:
            content_3 = l.read().strip()
            if content_3:  
                return int(content_3)
    return 0 

# skriver och uppdaterar vinster till filen
def write_high_score(score):
    if game_running == False and winner != None:
     with open(score_file, "w") as f:
            f.write(str(score))

def write_p2_score(score):
    if game_running == False and winner != None:
     with open(p2_score_file, "w") as y:
            y.write(str(score))

def write_singele_score(score):
    if game_running == False and winner != None:
     with open(single_mode, "w") as l:
            l.write(str(score))

# Laddar high score från filen
high_score_p1 = read_high_score()
high_score_p2 = read_p2_score()
high_score_single = read_single_score()

# Layouten för spelbrädet 
def print_board(board):                                     
    print(board[0] + fg("yellow") + " | "  + "\033[0m" + board[1] + fg("yellow") + " | " + "\033[0m" + board[2])
    print(fg("yellow") + "__________" + "\033[0m")
    print(board[3] + fg("yellow") + " | "  + "\033[0m" + board[4] + fg("yellow") + " | " + "\033[0m" + board[5])
    print(fg("yellow") +"__________" + "\033[0m")
    print(board[6] + fg("yellow") + " | "  + "\033[0m" + board[7] +  fg("yellow") + " | " + "\033[0m" + board[8])

# Spelaren gör ett drag
def player_input():
    valid_move = False
    while not valid_move:
        try:
            awnser = int(input("\nVar vill du lägga ditt drag? Skriv ett tal mellan 1-9:"))  
        except ValueError: 
            print("Du angav ingen giltig plats på spelbrädet")
            continue  
        
        if awnser >= 1 and awnser <= 9 and board[awnser-1] == "_":
            board[awnser-1] = current_player
            valid_move = True  
        elif awnser >= 1 and awnser <= 9 and board[awnser-1] != "_": 
            print("Den här platsen är redan tagen!")
        else:
            print("Du angav ingen giltig plats på spelbrädet")

class Result:
    # Kollar om spelaren har tre i rad vågrät
    def check_horizontal(self):
        global winner
        if board[0] == board[1] == board[2] and board[1] != "_":
            winner = board[0]
            return True
        elif board[3] == board[4] == board[5] and board[3] != "_":
            winner = board[3]
            return True
        elif board[6] == board[7] == board[8] and board[6] != "_":
            winner = board[6]
            return True

    # Kollar om spelaren har tre i rad lodrät
    def check_row(self): 
        global winner
        if board[0] == board[3] == board[6] and board[0] != "_":
            winner = board[0]
            return True
        elif board[1] == board[4] == board[7] and board[1] != "_":
            winner = board[1]
            return True
        elif board[2] == board[5] == board[8] and board[2] != "_":
            winner = board[2]
            return True
        
    # Kollar om spelaren har tre i rad diagonalt
    def check_diagonal(self): 
        global winner
        if board[0] == board[4] == board[8] and board[0] != "_":
            winner = board[0]
            return True
        elif board[2] == board[4] == board[6] and board[2] != "_":
            winner = board[2]
            return True

    # Kollar om det är oavgjort
    def check_tie(self): 
        global game_running
        if "_" not in board:
            game_running = False
            
    # Kollar om spelare uppfyller någon av kriterierna för att vinna
    def check_win(self):
        global game_running
        if self.check_diagonal() or self.check_row() or self.check_horizontal():
            game_running = False

# Byter spelare
class ChangePlayer:
    @staticmethod
    def switching_player(): 
        global current_player
        if current_player == player:
            current_player = player2
            print("\nspelare 2:s tur!")
        else:
            current_player = player
            print("\nspelare 1:s tur!")

resultat = Result()
changeplayer = ChangePlayer()

class Start:
    # Startar spelet
    @staticmethod
    def game_start_2p():   
        global high_score_p2, high_score_p1
        while game_running:
            os.system("cls")  
            print_board(board)
            if current_player == player:
                print("\nspelare 1:s tur!")
                player_input()
            else:
                print("\nspelare 2:s tur!")
                player_input()
            resultat.check_win()
            resultat.check_tie()
            if not game_running:
                print_board(board)
                if winner is None:
                    print("\nDet blev oavgjort")
                else:
                    print(f"\nVinnaren är: {winner}")
                    if player == winner:
                        high_score_p1 += 1
                        write_high_score(high_score_p1)
                        print(f"\nplayer 1:s high score är: {high_score_p1}")
                    else:
                        high_score_p2 += 1
                        write_p2_score(high_score_p2)
                        print(f"\nplayer 2:s high score är: {high_score_p2}")
                break
            else:
                ChangePlayer.switching_player()

    @staticmethod
    def game_start_1p():   
        global high_score_single, current_player, game_running, winner
        while game_running:
            os.system("cls")  
            print_board(board)
            if current_player == player:
                print("\nDin tur!")
                player_input()  
                resultat.check_win()
                resultat.check_tie()
            else:
                print("\nDatorns tur!")
                computer_move()  
                resultat.check_win()
                resultat.check_tie()
            if not game_running:  
                print_board(board)
                if winner is None:
                    print("\nDet blev oavgjort")
                else:
                    if winner == player:
                        print(f"\nVinnaren är: {winner}")
                        high_score_single += 1
                        write_singele_score(high_score_single)
                        print(f"\nDitt highscore är: {high_score_single}")
                    elif winner == computer:
                       print(f"\nVinnaren är: {winner}")
                break  
            else:
                if current_player == player:  # byter mellan datporn och spelaren
                    current_player = computer
                else:
                    current_player = player


if game_mode == "två spelare":
    Start.game_start_2p()
elif game_mode == "en spelare":
    Start.game_start_1p()
else: 
    print("spelarläget du angav är ogiltigt")




