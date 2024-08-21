import random

class RoPaScGame:
    def __init__(player):
        player.A_score= 0
        player.B_score= 0
        player.choice={1: "Rock", 2: "Paper", 3: "Scissors"}
    
    def play(player):
       # while True:
            playerA = random.randrange(1, 4)
            playerB = random.randrange(1, 4)
            print(f"Player 1 chose {player.choice[playerA]}, Player 2 chose {player.choice[playerB]}")
            if playerA == playerB:
                print("It's Draw")
            elif (playerA == 1 and playerB == 3) or (playerA == 2 and playerB == 1) or (playerA == 3 and playerB == 2 ) :
                player.A_score += 1
            else:
                player.B_score += 1
            print(f"Score: Player 1: {player.A_score} | Player 2 : {player.B_score}")

    def Rounds(player):
        for i in range(4):
            player.play()
        player.winner()
    def winner(player):
        print(f"\nTotal Score: Player 1: {player.A_score} | Player 2 : {player.B_score}")
        if player.A_score > player.B_score:
            print("Player 1 is the Winner")
        elif player.A_score < player.B_score:
            print("Player 2 is the Winner")
        else:
            print("It's a Draw")
    def reset(player):
        player.A_score= 0
        player.B_score= 0
competition = RoPaScGame()
competition.Rounds()
input("\nPress \n1.To play again \n2.To exit\n")

if input() == '1':
    competition.reset()
    competition.Rounds()
elif input() == '2':
        exit()
else:
    print("Invalid Input")
    exit()