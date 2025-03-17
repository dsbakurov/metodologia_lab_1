import sys

from games.nok import NOK
from games.progression import Progression

games = {
    "nok": NOK,
    "prog": Progression
}

if __name__ == '__main__':
    game_name = sys.argv[1]
    if game_name in games:
        game = games[game_name]()
        game.start()
    else:
        print("Choose correct game name")
