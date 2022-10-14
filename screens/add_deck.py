import pygame as pg
from components.Game import Game
from gameinfo import HEIGHT, WIDTH
from utils.load_image import load_image

pg.font.init()
ran = False

BG = pg.transform.scale(load_image("bg.gif"), (WIDTH, HEIGHT))


def add_deck(Game: Game):
    # Draw Background
    Game.WIN.blit(BG, (0, 0))

    # Update display
    pg.display.update()

    # Use this to run code inside of the function only once
    global ran

    if not ran:
        ran = True
        pass
