from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode


def main():

    # create a player object then create node for that player
    new_player_101 = Player('101', 'Soren', 'ez_2_hack')
    new_player_102 = Player('102', 'Lars', 'hard_2_hack')
    new_player_103 = Player('103', 'Kris', 'has_already_been_hacked')

    player_node_101 = PlayerNode(new_player_101)
    player_node_102 = PlayerNode(new_player_102)
    player_node_103 = PlayerNode(new_player_103)

    player_node_list = [player_node_101, player_node_102, player_node_103]
    player_list = PlayerList(player_node_list)
    player_list.display(False)


if __name__ == '__main__':
    main()

