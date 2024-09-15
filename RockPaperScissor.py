import random as rd


def generator():
    moves = ['Rock', 'Paper', 'Scissors']
    return rd.choice(moves)


def users():
    user_move = input('Choose your move "Rock", "Paper" or "Scissors": ')
    while user_move not in ['Rock', 'Paper', 'Scissors']:
        print("Invalid Value! Try Again\n")
        user_move = input('Choose your move "Rock", "Paper" or "Scissors": ')
    return user_move


def la_winner(computers, users):
    if users == computers:
        return "It's a Tie!"
    elif ((users == "Rock" and computers == "Paper") or (users == "Scissors" and computers == "Rock") or
          (users == "Paper" and computers == "Scissors")):
        return "You Lose!"
    else:
        return "You Win!"


def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_move = users()
        computer_move = generator()

        winner = la_winner(computer_move, user_move)

        print(f"\nYour Move: {user_move}")
        print(f"Computer's Move: {computer_move}")

        print(f"\nThe Result: {winner}\n")

        replay = input("Do you want to play again? Type '1' to play again, '0' to quit: ")
        print()
        if replay != "1":
            break

    print("Thank you for playing! Goodbye.")


play_game()
