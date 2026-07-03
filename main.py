import pygame
from models.game_data import GameData
from controllers.game_manager import GameManager
from scenes.title_scene import TitleScene
from scenes.game_scene import GameScene

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("農場ゲーム")

clock = pygame.time.Clock()

game_data = GameData()
game_manager = GameManager(game_data)

current_scene = "title"

title_scene = TitleScene()
game_scene = GameScene(game_manager)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if current_scene == "title":
            if title_scene.handle_event(event):
                game_manager.start_game()
                current_scene = "game"

        elif current_scene == "game":
            game_scene.handle_event(event)

    if current_scene == "title":
        title_scene.draw(screen)

    elif current_scene == "game":
        game_scene.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()