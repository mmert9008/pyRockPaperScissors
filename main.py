import random


def main() -> None:
    player_wins = 0
    computer_wins = 0

    opts = ["rock", "paper", "scissors"]

    while True:
        turn = input("Choose Rock, Paper, or Scissors or press Q to quit: ").lower()
        if turn == "q":
            break

        if turn not in opts:
            continue

        rng = random.randint(0, 2)
        # rock = 0, paper = 1, scissors = 2

        computer_turn = opts[rng]
        print(f"Computer threw {computer_turn}")

        if turn == "rock" and computer_turn == "scissors":
            print("You win!\n")
            player_wins += 1
        elif turn == "paper" and computer_turn == "rock":
            print("You win!\n")
            player_wins += 1
        elif turn == "scissors" and computer_turn == "paper":
            print("You win!\n")
            player_wins += 1
        elif turn == computer_turn:
            print("Go again, no points!\n")
        else:
            print("You lose, git gud!\n")
            computer_wins += 1

    print(f"\nYou won {player_wins} times.")
    print(f"The computer won {computer_wins} times.")
    if player_wins > computer_wins:
        print("You are the Rock Paper Scissors MASTER!")
    else:
        print("Git gud, sucka!")
    print("Game over!")


if __name__ == "__main__":
    main()
