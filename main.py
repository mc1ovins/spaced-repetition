import pygame as pg
from gameinfo import FPS, HEIGHT, TITLE, WIDTH
from components.Game import Game
from screens.add_deck import add_deck
from screens.home import home


def main():
    game = Game(WIDTH, HEIGHT, TITLE, [home, add_deck])
    game.play_audio("assets/song.webm")
    game.update_streak()

    run = True
    clock = pg.time.Clock()

    while run:
        clock.tick(FPS)
        game.draw_screen()
        run = game.handle_events()

    game.quit()
    pg.quit()


if __name__ == "__main__":
    main()
