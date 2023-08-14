from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode


def main():

    # create a player object then create node for that player
    new_player_101 = Player('101', 'Soren')
    player_101_node = PlayerNode(new_player_101)
    player_list = PlayerList()

    player_list.append_head(player_101_node)


if __name__ == '__main__':
    main()
