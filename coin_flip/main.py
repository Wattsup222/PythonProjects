from game import Game
from player import Player


def main():
    coin_flip = Game()
    player = Player()
    selection = player.select_choice()
    outcome = coin_flip.flip()
    coin_flip.result(selection)
    print(outcome)


if __name__ == "__main__":
    main()
