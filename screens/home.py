import pygame as pg
from components.Button import Button
from components.Deck import Deck
from components.Game import Game
from gameinfo import DB, HEIGHT, WHITE, WIDTH
from utils.load_image import load_image

pg.font.init()
ran = False

# Define assets: This code runs once when the module is imported
ADD_DECK = Button("Nuevo mazo", "plus.svg", None)
EXIT = Button("Salir", "close.svg", None)
BG = pg.transform.scale(load_image("bg.gif"), (WIDTH, HEIGHT))
FONT = pg.font.SysFont("Arial", 30, bold=True)
DECKS: list[Deck] = []

for k in DB["decks"]:
    DECKS.append(
        Deck(k, DB["decks"][k]["cards"], DB["decks"][k]["image"]))


def home(Game: Game):
    # Draw Background
    Game.WIN.blit(BG, (0, 0))

    # Draw title in the middle
    text = FONT.render("Spaced Repetition Cards", True, WHITE)
    Game.WIN.blit(text, (WIDTH / 2 - text.get_width() / 2, 60))

    # Rendering decks
    for i, deck in enumerate(DECKS[0:3]):
        # Separation between decks
        x = 75 + (i * 345)
        y = HEIGHT / 2 - deck.height / 2

        deck.draw(Game.WIN, x, y)

    # Render streak
    streak = DB["streak"]["current"]
    font = pg.font.SysFont("Arial", 30, bold=True)
    text = font.render(f"Racha: {streak}", True, WHITE)
    Game.WIN.blit(text, (75, HEIGHT - 75))

    # Draw button in the middle bottom
    ADD_DECK.draw(Game.WIN, WIDTH / 2 - ADD_DECK.width / 2, HEIGHT - 80)

    # exit button in the right bottom
    EXIT.draw(Game.WIN, WIDTH - 75 - EXIT.width, HEIGHT - 80)

    # Update display
    pg.display.update()

    # Use this to run code inside of the function only once
    global ran

    if not ran:
        ADD_DECK.onClick = lambda: Game.change_screen(1)
        EXIT.onClick = lambda: Game.quit()

        Game.register_click_event((ADD_DECK.rect, ADD_DECK.onClick))
        Game.register_click_event((EXIT.rect, EXIT.onClick))

        ran = True
