# This is a sample Python script.
from itertools import count

from bowling.Frame import Frame
from bowling.Game import Game, GameIsOver
from bowling.Printer import print_frames


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def start_game():
    game = Game()

    while True:
        try:
            print("Turn: {}".format(game.get_turn()))
            print("--------------------------------")
            frame = game.throw(int(input("First Strike: ")))
            if frame.is_strike():
                print("A Strike!!!")
            else:
                game.throw(int(input("Second Try: ")))
        except GameIsOver:
            print("The Game is over")
            break

    print_frames(game.frames)


if __name__ == '__main__':
    start_game()
