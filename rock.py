import random

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    print("Choose one: Rock, Paper, or Scissors")
    
    choices = ['Rock', 'Paper', 'Scissors']
    
    player_choice = input("Your choice: ")
    player_choice = player_choice.capitalize()
    
    computer_choice = random.choice(choices)
    
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}\n")
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose!")
        
    play_again = input("\nDo you want to play again? (yes/no): ")
    
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thank you for playing!")
        
play_game()
