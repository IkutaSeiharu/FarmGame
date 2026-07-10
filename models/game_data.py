from models.field import Field

class GameData:

    def __init__(self):

        self.day = 1
        self.money = 0

        self.wheat_seed = 5

        self.field = Field()

        self.seeds = {
            "小麦": 5,
            "トマト": 0,
            "じゃがいも": 0
        }

        self.selected_crop = None