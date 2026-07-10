class GameManager:

    def __init__(self, game_data):
        self.game_data = game_data

    def start_game(self):
        self.game_data.day = 1
        self.game_data.money = 0

    def next_day(self):
        self.game_data.day += 1