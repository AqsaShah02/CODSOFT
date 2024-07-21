import random


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])



def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    

    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You won the game !")
    else:

        print(" oopsie, You lose!")


def play_game():
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, try again.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
