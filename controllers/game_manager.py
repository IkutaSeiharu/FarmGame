from models.crop import Crop


class GameManager:

    def __init__(self, game_data):

        self.game_data = game_data

    def start_game(self):

        self.game_data.day = 1
        self.game_data.money = 0

        self.game_data.seeds = {
            "小麦": 5,
            "トマト": 0,
            "じゃがいも": 0
        }

        self.game_data.selected_crop = None

    def next_day(self):

        self.game_data.day += 1

        earned_money = self.game_data.field.grow()

        self.game_data.money += earned_money

    def plant_crop(self, row, col):

        selected = self.game_data.selected_crop

        if selected is None:
            return

        if self.game_data.seeds[selected] <= 0:
            print("種が足りません")
            return

        if selected == "小麦":

            crop = Crop(
                "小麦",
                100,
                3
            )

        elif selected == "トマト":

            crop = Crop(
                "トマト",
                300,
                5
            )

        elif selected == "じゃがいも":

            crop = Crop(
                "じゃがいも",
                500,
                7
            )

        else:
            return

        planted = self.game_data.field.plant(
            row,
            col,
            crop
        )

        if planted:

            self.game_data.seeds[selected] -= 1

            
            if self.game_data.seeds[selected] <= 0:

                self.game_data.selected_crop = None

            print(
                selected,
                "残り",
                self.game_data.seeds[selected]
            )

    def buy_seed(self, crop_name):

        prices = {
            "小麦": 50,
            "トマト": 150,
            "じゃがいも": 300
        }

        if crop_name not in prices:
            return False

        price = prices[crop_name]

        if self.game_data.money < price:

            print("お金が足りません")
            return False

        self.game_data.money -= price
        self.game_data.seeds[crop_name] += 1

        print(
            crop_name,
            "購入",
            "残金",
            self.game_data.money
        )

        return True

    def is_game_over(self):

        return self.game_data.day > 30