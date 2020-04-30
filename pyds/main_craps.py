# -*- coding: utf-8 -*-

from craps import Player


def play_one_game():
    player = Player()
    you_win = player.play()
    print(player)
    if you_win :
        print("You win!")
    else:
        print("You lose!")

def play_many_games():
    number = int(input("Enter the number of games: "))
    wins = 0
    losses = 0
    win_rolls = 0
    loss_rolls = 0
    player = Player()
    for count in range(number):
        has_won = player.play()
        rolls = player.get_number_rolls()
        if has_won:
            wins += 1
            win_rolls += rolls
        else:
            losses += 1
            loss_rolls += rolls
    print("The total number of wins is ", wins)
    print("The total number of losses is ", losses)
    print ("The average number of rolls per win is %0.2f" % \
            (float(win_rolls) / wins))
    print("The winning percentage is %0.3f" % \
            (float(wins) / number))

def main():
    #play_one_game()
    play_many_games()

if __name__ == "__main__":
    main()
