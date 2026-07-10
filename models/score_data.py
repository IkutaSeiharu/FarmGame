import json
import os


class ScoreData:

    FILE = "save/highscore.json"

    @classmethod
    def load(cls):

        if not os.path.exists(cls.FILE):
            return 0

        with open(
            cls.FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        return data["highscore"]

    @classmethod
    def save(cls, score):

        with open(
            cls.FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                {"highscore": score},
                f
            )