import pygame


class PlantScene:

    def __init__(self, game_data):

        self.game_data = game_data

        self.font = pygame.font.SysFont(
            "meiryo",
            50
        )

        self.wheat_button = pygame.Rect(
            250,
            150,
            300,
            60
        )

        self.tomato_button = pygame.Rect(
            250,
            250,
            300,
            60
        )

        self.potato_button = pygame.Rect(
            250,
            350,
            300,
            60
        )

        self.back_button = pygame.Rect(
            250,
            450,
            300,
            60
        )

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.wheat_button.collidepoint(event.pos):
                return "小麦"

            if self.tomato_button.collidepoint(event.pos):
                return "トマト"

            if self.potato_button.collidepoint(event.pos):
                return "じゃがいも"

            if self.back_button.collidepoint(event.pos):
                return "戻る"

        return None

    def draw(self, screen):

        screen.fill((220, 255, 220))

        title = self.font.render(
            "バッグ",
            True,
            (0, 0, 0)
        )

        screen.blit(
            title,
            (320, 50)
        )

        buttons = [

            (
                self.wheat_button,
                f"小麦 × {self.game_data.seeds['小麦']}"
            ),

            (
                self.tomato_button,
                f"トマト × {self.game_data.seeds['トマト']}"
            ),

            (
                self.potato_button,
                f"じゃがいも × {self.game_data.seeds['じゃがいも']}"
            ),

            (
                self.back_button,
                "戻る"
            )

        ]

        for button, text in buttons:

            pygame.draw.rect(
                screen,
                (180, 220, 180),
                button
            )

            label = pygame.font.SysFont(
                "meiryo",
                35
            ).render(
                text,
                True,
                (0, 0, 0)
            )

            screen.blit(
                label,
                (
                    button.x + 40,
                    button.y + 15
                )
            )