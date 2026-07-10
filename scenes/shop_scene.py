import pygame


class ShopScene:

    def __init__(self):

        self.font = pygame.font.SysFont(
            "meiryo",
            40
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

        screen.fill((255, 240, 180))

        title = self.font.render(
            "SHOP",
            True,
            (0, 0, 0)
        )

        screen.blit(
            title,
            (330, 50)
        )

        buttons = [

            (
                self.wheat_button,
                "小麦種 50G"
            ),

            (
                self.tomato_button,
                "トマト種 150G"
            ),

            (
                self.potato_button,
                "じゃがいも種 300G"
            ),

            (
                self.back_button,
                "戻る"
            )
        ]

        for button, text in buttons:

            pygame.draw.rect(
                screen,
                (220, 220, 220),
                button
            )

            label = pygame.font.SysFont(
                "meiryo",
                30
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