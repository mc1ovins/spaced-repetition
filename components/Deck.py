import pygame as pg
from gameinfo import PURPLE, WHITE
from utils.load_image import load_image


class Deck:
    """
    The Deck class is the class that represents a deck. 
    It has a main `draw` method that is called every frame. 
    It's an abtraction for the UI of a deck.
    """
    def __init__(self, title, cards, image) -> None:
        self.cards = cards
        self.image = load_image(image)
        self.width = 315
        self.height = 340

        self._title_font = pg.font.SysFont("Arial", 20, bold=True)
        self.title = self._title_font.render(title, True, WHITE)

        self._cards_font = pg.font.SysFont("Arial", 15)
        self.cards_length = self._cards_font.render(
            f"{len(self.cards)} cards", True, WHITE)

    def draw(self, WIN, x, y):
        # Draw a 315 x 340 rectangle
        # Border radius 10
        pg.draw.rect(WIN, WHITE,
                     (x, y, self.width, self.height), border_radius=10)

        # Draw image
        WIN.blit(self.image, (x, y))

        # Draw another rectangle inside the first one
        # Bottom border radius 10
        pg.draw.rect(WIN, PURPLE,
                     (x, y + self.height - 50, self.width, 50), border_radius=10)

        # Draw title
        WIN.blit(self.title, (x + 15, y + self.height - 45))

        # Draw cards length
        WIN.blit(self.cards_length, (x + 15, y + self.height - 20))

        # Render 40*40 rectangle on the bottom right
        # Border radius 10
        pg.draw.rect(WIN, WHITE, (x + self.width -
                     45, y + self.height - 45, 40, 40), border_radius=10)

        # Draw arrow in the middle of the rectangle
        arrow = pg.transform.scale(load_image("arrow.png"), (16, 25))
        WIN.blit(arrow, (x + self.width - 45 + 12, y + self.height - 45 + 7))

        return self
