print("Rock...")
print("Papper...")
print("Scissors...")

player1 = input("Player one, make your move: ")
player2 = input("Player two, make your move: ")

if player1 == "rock" and player2 == "scissors":
    print("payer1 wins")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins!")
elif player1 == "paper" and player2 == "rock":
    print("payer1 wins")
elif player1 == "paper" and player2 == "scissors":
    print("player2 wins!")
elif player1 == "scissors" and player2 == "paper":
    print("payer1 wins")
elif player1 == "scissors" and player2 == "rock":
    print("player2 wins!")
elif player1 == player2:
    print("It`s a tie!")
else:
    print("Something went wrong!")