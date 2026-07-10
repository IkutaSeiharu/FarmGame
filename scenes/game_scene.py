import pygame


class GameScene:

    def __init__(self, game_manager):

        self.game_manager = game_manager

        self.font = pygame.font.SysFont(
            "meiryo",
            40
        )

        self.sleep_button = pygame.Rect(
            550,
            450,
            180,
            60
        )

        self.back_button = pygame.Rect(
            50,
            450,
            180,
            60
        )

        self.shop_button = pygame.Rect(
            300,
            450,
            180,
            60
        )

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            # Bag
            if self.back_button.collidepoint(event.pos):
                return "plant"

            # Shop
            if self.shop_button.collidepoint(event.pos):
                return "shop"

            # Sleep
            if self.sleep_button.collidepoint(event.pos):

                self.game_manager.next_day()

            # 畑クリック
            for row in range(3):
                for col in range(3):

                    x = 350 + col * 110
                    y = 100 + row * 110

                    rect = pygame.Rect(
                        x,
                        y,
                        100,
                        100
                    )

                    if rect.collidepoint(event.pos):

                        self.game_manager.plant_crop(
                            row,
                            col
                        )

        return None

    def draw(self, screen):

        screen.fill((150, 220, 150))

        day_text = self.font.render(
            f"Day : {self.game_manager.game_data.day}",
            True,
            (0, 0, 0)
        )

        money_text = self.font.render(
            f"Money : {self.game_manager.game_data.money}",
            True,
            (0, 0, 0)
        )

        screen.blit(day_text, (20, 20))
        screen.blit(money_text, (20, 70))

        selected = self.game_manager.game_data.selected_crop

        if selected is None:
            selected = "なし"

        selected_text = self.font.render(
            f"選択中 : {selected}",
            True,
            (0, 0, 0)
        )

        screen.blit(selected_text, (20, 120))

        wheat_text = pygame.font.SysFont(
            "meiryo",
            28
        ).render(
            f"小麦 : {self.game_manager.game_data.seeds['小麦']}",
            True,
            (0, 0, 0)
        )

        tomato_text = pygame.font.SysFont(
            "meiryo",
            28
        ).render(
            f"トマト : {self.game_manager.game_data.seeds['トマト']}",
            True,
            (0, 0, 0)
        )

        potato_text = pygame.font.SysFont(
            "meiryo",
            28
        ).render(
            f"じゃがいも : {self.game_manager.game_data.seeds['じゃがいも']}",
            True,
            (0, 0, 0)
        )

        screen.blit(wheat_text, (20, 200))
        screen.blit(tomato_text, (20, 240))
        screen.blit(potato_text, (20, 280))

        # 畑
        for row in range(3):
            for col in range(3):

                x = 350 + col * 110
                y = 100 + row * 110

                rect = pygame.Rect(
                    x,
                    y,
                    100,
                    100
                )

                pygame.draw.rect(
                    screen,
                    (160, 82, 45),
                    rect
                )

                crop = self.game_manager.game_data.field.grid[row][col]

                if crop:

                    color = (255, 255, 0)

                    if crop.name == "トマト":
                        color = (255, 0, 0)

                    elif crop.name == "じゃがいも":
                        color = (139, 69, 19)

                    pygame.draw.circle(
                        screen,
                        color,
                        rect.center,
                        20
                    )

                    small_font = pygame.font.SysFont(
                        "meiryo",
                        18
                    )

                    name_text = small_font.render(
                        crop.name,
                        True,
                        (0, 0, 0)
                    )

                    remain_text = small_font.render(
                        str(crop.remaining_days),
                        True,
                        (0, 0, 0)
                    )

                    screen.blit(
                        name_text,
                        (x + 5, y + 5)
                    )

                    screen.blit(
                        remain_text,
                        (x + 40, y + 75)
                    )

        # Bagボタン
        pygame.draw.rect(
            screen,
            (220, 220, 220),
            self.back_button
        )

        bag_text = pygame.font.SysFont(
            "meiryo",
            30
        ).render(
            "Bag",
            True,
            (0, 0, 0)
        )

        screen.blit(
            bag_text,
            (110, 465)
        )

        # Shopボタン
        pygame.draw.rect(
            screen,
            (255, 220, 120),
            self.shop_button
        )

        shop_text = pygame.font.SysFont(
            "meiryo",
            30
        ).render(
            "Shop",
            True,
            (0, 0, 0)
        )

        screen.blit(
            shop_text,
            (355, 465)
        )

        # Sleepボタン
        pygame.draw.rect(
            screen,
            (180, 220, 255),
            self.sleep_button
        )

        sleep_text = pygame.font.SysFont(
            "meiryo",
            30
        ).render(
            "Sleep",
            True,
            (0, 0, 0)
        )

        screen.blit(
            sleep_text,
            (605, 465)
        )