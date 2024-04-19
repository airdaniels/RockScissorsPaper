import random


def get_choices():
  player_choice = input("Enter a choice (Rock, Paper, Scissors): ").lower()
  options = ["Paper", "Rock", "Scissors"]
  computer_choice = random.choice(options).lower()
  choices = {"player" : player_choice, "computer" : computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player} | Computer chose {computer}")
  if player == computer:
    return "It is a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes Scissors! You win!"
    else:
      return "Paper covers Rock... You Lose!"
  elif player == "paper":
    if computer == "rock":
      return  "Paper covers Rock! You Win!"
    else:
      return "Scissors cut paper... You lose!"
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cut Paper! You Win!"
    else: 
      return "Rock smashes Scissors.. You Lose!"

choices = get_choices()
results = check_win(choices["player"], choices["computer"])
print(results)
  