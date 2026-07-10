from models.crop import Crop

class GameManager:

    def __init__(self, game_data):
        self.game_data = game_data

    def start_game(self):

        self.game_data.day = 1
        self.game_data.money = 0
        self.game_data.wheat_seed = 5

    def next_day(self):

        self.game_data.day += 1

        earned_money = self.game_data.field.grow()

        self.game_data.money += earned_money

    def plant_crop(self, row, col):

        if self.game_data.wheat_seed <= 0:
            return

        crop = Crop(
            "小麦",
            100,
            3
        )

        planted = self.game_data.field.plant(
            row,
            col,
            crop
        )

        if planted:
            self.game_data.wheat_seed -= 1

    def is_game_over(self):

        return self.game_data.day > 30