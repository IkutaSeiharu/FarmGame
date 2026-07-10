class Crop:

    def __init__(
        self,
        name,
        price,
        grow_days
    ):

        self.name = name
        self.price = price

        self.remaining_days = grow_days