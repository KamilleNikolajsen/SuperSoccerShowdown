from domain.player import Player


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        if isinstance(player, Player):
            self.players.append(player)
        else:
            raise ValueError("You can only add Player objects to a team")