import pygame


class GameScene:

    def __init__(self, game_manager):

        self.game_manager = game_manager

        self.font = pygame.font.SysFont(None, 50)

        self.sleep_button = pygame.Rect(
            300,
            450,
            200,
            70
        )

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.sleep_button.collidepoint(event.pos):
                self.game_manager.next_day()

            for row in range(3):
                for col in range(3):

                    x = 250 + col * 110
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

        seed_text = self.font.render(
            f"Seed : {self.game_manager.game_data.wheat_seed}",
            True,
            (0, 0, 0)
        )

        screen.blit(day_text, (50, 50))
        screen.blit(money_text, (50, 120))
        screen.blit(seed_text, (50, 190))

        pygame.draw.rect(
            screen,
            (200, 200, 255),
            self.sleep_button
        )

        sleep_text = pygame.font.SysFont(
            None,
            40
        ).render(
            "Sleep",
            True,
            (0, 0, 0)
        )

        screen.blit(
            sleep_text,
            (355, 470)
        )

        for row in range(3):
            for col in range(3):

                x = 250 + col * 110
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

                    pygame.draw.circle(
                        screen,
                        (255, 255, 0),
                        rect.center,
                        20
                    )

                    day_font = pygame.font.SysFont(
                        None,
                        30
                    )

                    remain = day_font.render(
                        str(crop.remaining_days),
                        True,
                        (0, 0, 0)
                    )

                    screen.blit(
                        remain,
                        (x + 40, y + 40)
                    )