from p06_project.player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild in self.name:
            return f"Player {player.name} is already in the guild."
        if player.guild != Player.PLAYER_DEFAULT_GUILD:
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = Player.PLAYER_DEFAULT_GUILD
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = ''
        result += f"Guild: {self.name}\n"
        for player in self.players:
            result += player.player_info()

        return result
