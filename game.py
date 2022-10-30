import random
from play import Paper, Rock, Scissors, Lizard, Spock, Result

def run_game():
    display_game()
    user_play = get_user_play()
    comp_play = random_play()
    display_match(user_play,comp_play)
    winner = get_winner(user_play, comp_play)   

    #Asking player to play again
    play_again = another_match() 

    if play_again: 
        run_game()
    else:
        print(random.choice([   "What are you afraid of Chicken Little?",
                                "Are you serious? C'mon!!",
                                "It's just a game, Karen...",
                                "It's the easiest game ever, PLS...Play another one!!!"]))

def another_match(): 
    again = None
    while again == None:
        answer = input("Do you wanna play again? Y/N ").upper().strip()
        if answer == "Y":
            again = True
        elif answer == "N":
            again = False
        
    return again

def display_match(play1,play2):
    print(f"\n{play1.description()} vs {play2.description()} FIGHT!\n ")

def display_game():
    """
    Muestra el nombre del juego
    """
    print("\n\n\t\tRock, Paper, Scissors\n\n")

def get_user_play(): 
    """
    Asks the user what is going to play
    """
    res = get_user_response()

    if res == 1:
        return Rock()
    elif res == 2:
        return Paper()
    elif res == 3:
        return Scissors()
    elif res == 4:
        return Lizard()
    else:
        return Spock()

def get_user_response():
    """
    Shows a menu of options and asks the user to select one.
    Returns a string that represents what play the player chose
    """
    response = None
    while True : 
        print("Choose your play:")
        print("1. Rock 🗿 ")
        print("2. Paper 📄 ")
        print("3. Scissors ✂️ ")
        print("4. Lizard 🦎 ")
        print("5. Spock 🖖🏼 ")

        raw = input("Enter 1, 2 , 3 , 4, 5\t")

        raw = raw.strip() 

        if raw == "1":
            raw = 1
            break 
        elif raw == "2":
            raw = 2
            break
        elif raw == "3":
            raw = 3
            break 
        elif raw == "4":
            raw = 4
            break 
        elif raw == "5":
            raw = 5
            break 
        else:
            continue

    return raw

def random_play():
    """
    Selects random play to play against the player
    """
    return random.choice([Paper(),Rock(),Scissors(),Lizard(),Spock()])

def get_winner(play1,play2):
    """
    Gets the winner
    """
    result = play1.compare(play2)
    winner = ""
    if result == Result.WINS:
          winner = display_victory(play1)
    elif result == Result.EQUAL:
        winner = display_tie(play1,play2)
    else:
        winner = display_victory(play2)
    
    return winner


def display_tie(play1,play2):
    """
    Displays if there's a tie
    """
    print(f"There's a tie between {play1.description()} 🥶") 

def display_victory(winner):
    """
    Shows who won
    """
    print(f"The winner is {winner.description()} 🔥")


if __name__ == '__main__':
    run_game()
