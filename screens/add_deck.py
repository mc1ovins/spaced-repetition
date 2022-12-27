import pygame as pg
from components.Game import Game
from gameinfo import HEIGHT, WHITE, WIDTH
from utils.load_image import load_image
import pygame_textinput

pg.font.init()
ran = False

BG = pg.transform.scale(load_image("bg.gif"), (WIDTH, HEIGHT))

TEXT_INPUT = pygame_textinput.TextInputVisualizer()
TEXT_INPUT.value = ""
TEXT_INPUT.font_color = WHITE
TEXT_INPUT.cursor_color = WHITE

QUESTION_INPUT = pygame_textinput.TextInputVisualizer()
QUESTION_INPUT.value = "Pregunta"
QUESTION_INPUT.font_color = WHITE
QUESTION_INPUT.cursor_color = WHITE

ANSWER_INPUT = pygame_textinput.TextInputVisualizer()
ANSWER_INPUT.value = ""
ANSWER_INPUT.font_color = WHITE
ANSWER_INPUT.cursor_color = WHITE


def add_deck(Game: Game):
    # Draw Background
    Game.WIN.blit(BG, (0, 0))

    Game.WIN.blit(TEXT_INPUT.surface, (60, 60))

    # Update display
    pg.display.update()

    # Use this to run code inside of the function only once
    global ran

    if not ran:
        Game.register_custom_event_handler(TEXT_INPUT.update)
        ran = True
        pass
