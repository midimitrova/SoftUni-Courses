from project.player import Player


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def __take_last_supply(self, supply_type):
        for sup_index in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[sup_index]).__name__ == supply_type:
                return self.supplies.pop(sup_index)

        if supply_type == 'Food':
            raise Exception("There are no food supplies left!")
        elif supply_type == 'Drink':
            raise Exception("There are no drink supplies left!")

    def __find_player_by_name(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)
        if player.stamina == 100:
            return f"{player_name} have enough stamina."
        supply = self.__take_last_supply(sustenance_type)
        if supply:
            player._sustain_player(supply)
            return f"{player_name} sustained successfully with {supply.name}."

    @staticmethod
    def __attack(player_one, player_two):
        player_two.stamina -= (player_one.stamina / 2)
        if player_one.stamina - (player_two.stamina / 2) < 0:
            player_one.stamina = 0
        else:
            player_one.stamina -= (player_two.stamina / 2)

        if player_one < player_two:
            return f"Winner: {player_two.name}"
        else:
            return f"Winner: {player_one.name}"

    @staticmethod
    def __check_if_the_players_cannot_duel(*players):
        result = []
        for player in players:
            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")
        if result:
            return '\n'.join(result)

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        result = self.__check_if_the_players_cannot_duel(first_player, second_player)
        if result:
            return result

        if first_player < second_player:
            return self.__attack(first_player, second_player)
        else:
            return self.__attack(second_player, first_player)

    def next_day(self):
        for p in self.players:
            if p.stamina - (p.age * 2) < 0:
                p.stamina = 0
            else:
                p.stamina -= (p.age * 2)
        for p in self.players:
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        info = []
        for p in self.players:
            info.append(p.__str__())
        for s in self.supplies:
            info.append(s.details())
        result = "\n".join(info)
        return result
