import pygame

from models.game_data import GameData
from models.score_data import ScoreData

from controllers.game_manager import GameManager

from scenes.title_scene import TitleScene
from scenes.game_scene import GameScene
from scenes.plant_scene import PlantScene
from scenes.shop_scene import ShopScene
from scenes.score_scene import ScoreScene


pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("農場ゲーム")

clock = pygame.time.Clock()

game_data = GameData()
game_manager = GameManager(game_data)

title_scene = TitleScene()
game_scene = GameScene(game_manager)
plant_scene = PlantScene(game_data)
shop_scene = ShopScene()

score_scene = None

current_scene = "title"

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # タイトル画面
        if current_scene == "title":

            if title_scene.handle_event(event):

                game_manager.start_game()

                current_scene = "game"

        # ゲーム画面
        elif current_scene == "game":

            result = game_scene.handle_event(event)

            if result == "plant":
                current_scene = "plant"

            elif result == "shop":
                current_scene = "shop"

        # Bag画面
        elif current_scene == "plant":

            selected = plant_scene.handle_event(event)

            if selected == "戻る":

                current_scene = "game"

            elif selected is not None:

                game_data.selected_crop = selected

                print("選択:", selected)

                current_scene = "game"

        # Shop画面
        elif current_scene == "shop":

            selected = shop_scene.handle_event(event)

            if selected == "戻る":

                current_scene = "game"

            elif selected is not None:

                game_manager.buy_seed(selected)

                current_scene = "shop"

        # スコア画面
        elif current_scene == "score":

            if score_scene.handle_event(event):

                current_scene = "title"

    # 描画
    if current_scene == "title":

        title_scene.draw(screen)

    elif current_scene == "game":

        game_scene.draw(screen)

    elif current_scene == "plant":

        plant_scene.draw(screen)

    elif current_scene == "shop":

        shop_scene.draw(screen)

    elif current_scene == "score":

        score_scene.draw(screen)

    # ゲーム終了判定
    if current_scene == "game":

        if game_manager.is_game_over():

            score = game_data.money

            highscore = ScoreData.load()

            if score > highscore:
                ScoreData.save(score)

            score_scene = ScoreScene(score)

            current_scene = "score"

    pygame.display.flip()
    clock.tick(60)

pygame.quit()