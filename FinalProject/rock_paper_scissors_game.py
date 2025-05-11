''' GAME RULES:
Rock beats Scissors (Rock crushes Scissors)
• Scissors beats Paper (Scissors cut Paper)
• Paper beats Rock (Paper covers Rock)
• If both players choose the same, its a tie (no winner)
• The player that gets 3 first wins the game.'''

import random

cpu_score = 0
player_score = 0

def main():
    while True:
        global player_score, cpu_score

        computer = get_computer_choice()
        player = get_user_choice()

        if(check_if_invalid_option(player)):
            print(f"Error! {player} is an invalid option")
            continue;

        result = play(computer, player)

        print(result)

        if(player_score == 3 or cpu_score == 3):
            print()
            print(f"Final Scores: \nComputer: {cpu_score} \nPlayer: {player_score}")
            if player_score == 3:
                print("You win the game!")
            else:
                print("You lost the game!")
                break
            
# CPU CHOICES
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices).lower()

#USER INPUT CHOICES
def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        player = input("rock, paper or scissors? ").lower()
        if player in choices:
            return player
        else:
            print(f"Error! {player} is an invalid option")
            continue

#CHECK IF USER INPUT IS VALID
def check_if_invalid_option(player):
    choices = ['rock', 'paper', 'scissors']
    if player not in choices:
        return True
    else:
        return False

# CHECK TIE
def check_if_a_tie(computer, player):
    if computer == player:
        return True
    else:
        return False
    
    # CHECK IF PLAYER WINS
def check_if_player_wins(computer, player):
    if ((player == 'rock' and computer == 'scissors') or
        (player == 'scissors' and computer == 'paper') or
        (player == 'paper' and computer == 'rock')):
        return True
    else:
        return False
    
def play(computer, player):
    global player_score, cpu_score

    if check_if_a_tie(computer, player):
        return "The round was a tie!"
    elif check_if_player_wins(computer, player):
        player_score += 1
        return "You win the round!"
    else:
        cpu_score += 1
        return "Computer wins the round!"
    
    
if __name__ == "__main__":
    main()