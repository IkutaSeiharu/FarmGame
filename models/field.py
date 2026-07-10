class Field:

    def __init__(self):
        self.grid = [[None for _ in range(3)] for _ in range(3)]

    def plant(self, row, col, crop):

        if self.grid[row][col] is None:
            self.grid[row][col] = crop
            return True

        return False

    def grow(self):

        harvested_money = 0

        for row in range(3):
            for col in range(3):

                crop = self.grid[row][col]

                if crop:

                    crop.remaining_days -= 1

                    if crop.remaining_days <= 0:

                        harvested_money += crop.price
                        self.grid[row][col] = None

        return harvested_money