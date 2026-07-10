import pygame


class GameScene:

    def __init__(self, game_manager):

        self.game_manager = game_manager

        self.font = pygame.font.SysFont(
            None,
            50
        )

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

        screen.blit(day_text, (50, 50))
        screen.blit(money_text, (50, 120))

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