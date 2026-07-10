import pygame


class TitleScene:

    def __init__(self):

        self.font = pygame.font.SysFont(None, 72)

        self.button = pygame.Rect(
            300,
            300,
            200,
            70
        )

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.button.collidepoint(event.pos):
                return True

        return False

    def draw(self, screen):

        screen.fill((200, 255, 200))

        title = self.font.render(
            "Farm Game",
            True,
            (0, 0, 0)
        )

        screen.blit(title, (250, 150))

        pygame.draw.rect(
            screen,
            (100, 200, 100),
            self.button
        )

        text = pygame.font.SysFont(
            None,
            40
        ).render(
            "Start",
            True,
            (0, 0, 0)
        )

        screen.blit(
            text,
            (360, 320)
        )