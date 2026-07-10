import pygame
from models.score_data import ScoreData


class ScoreScene:

    def __init__(self, score):

        self.score = score

        self.highscore = ScoreData.load()

        self.font = pygame.font.SysFont(None, 60)

        self.back_button = pygame.Rect(
            250,
            400,
            300,
            70
        )

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.back_button.collidepoint(event.pos):
                return True

        return False

    def draw(self, screen):

        screen.fill((200, 220, 255))

        title = self.font.render(
            "GAME OVER",
            True,
            (0, 0, 0)
        )

        score_text = self.font.render(
            f"Score : {self.score}",
            True,
            (0, 0, 0)
        )

        high_text = self.font.render(
            f"High Score : {self.highscore}",
            True,
            (0, 0, 0)
        )

        screen.blit(title, (220, 100))
        screen.blit(score_text, (180, 220))
        screen.blit(high_text, (120, 320))

        pygame.draw.rect(
            screen,
            (150, 255, 150),
            self.back_button
        )

        text = pygame.font.SysFont(
            None,
            40
        ).render(
            "Back To Title",
            True,
            (0, 0, 0)
        )

        screen.blit(
            text,
            (285, 420)
        )