class Crop:
    def __init__(self, name, grow_days, price):
        self.name = name
        self.grow_days = grow_days
        self.price = price
        self.remaining_days = grow_days