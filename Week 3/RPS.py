

def RPS():
    print("Welcome to rock Paper Scissors!")
    player1 = input ("Player1, please enter your name:")
    player2 = input("Player2, Please enter your name:")
    p1_choice = input(f"{player1} choose between Rock, Paper, and scissors")
    while not IsValidMove(p1_choice):
        print("Invalid Move, please try again")
        p1_choice = input(f"{player1} choose between Rock, Paper, and scissors")
    p2_choice = input(f"{player2} choose between Rock, Paper, and scissors")
    while not IsValidMove(p2_choice):
        print("Invalid Move, please try again")
        p2_choice = input(f"{player2} choose between Rock, Paper, and scissors")
    if p1_choice == p2_choice:
        print("Its a draw!!")
    if p1_choice == "rock" and p2_choice == "scissors":
        print(f"Rock beats scissors, {player1} Wins! ")
    elif p1_choice == "paper" and p2_choice == "rock":
        print(f"paper beats rock, {player1} Wins!")
    elif p1_choice == "scissors" and p2_choice == "paper":
        print (f"scissors beats paper, {player1} Wins!")
    elif p2_choice == "rock" and p1_choice == "scissors":
        print(f"Rock beats scissors, {player2} Wins! ")
    elif p2_choice == "paper" and p1_choice == "rock":
        print(f"paper beats rock, {player2} Wins!")
    elif p2_choice == "scissors" and p1_choice == "paper":
        print (f"scissors beats paper, {player2} Wins!")
def IsValidMove(playermove):
    validMoves= ["rock", "paper", "scissors" ]
    if playermove in validMoves:
        return True
    else:
        return False
RPS()















