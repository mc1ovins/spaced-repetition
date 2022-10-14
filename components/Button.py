from gameinfo import PURPLE, WHITE
from utils.load_image import load_image
import pygame as pg


class Button:
    def __init__(self, text, icon, onClick) -> None:
        # Texto
        self._font = pg.font.SysFont("Arial", 24)
        self.text = self._font.render(text, True, WHITE)

        # Icono
        self.icon = pg.transform.scale(load_image(icon), (24, 24))

        # Width and height
        self.width = self.text.get_width() + self.icon.get_width() + 35
        self.height = 45

        self.onClick = onClick
        self.rect = None

    def draw(self, WIN, x, y):
        # Draw button
        self.rect = pg.draw.rect(
            WIN, PURPLE, (x, y, self.width, 45), border_radius=10)

        # Draw icon
        WIN.blit(self.icon, (x + 10, y + 10))

        # Draw text
        WIN.blit(self.text, (x + 10 + self.icon.get_width() + 10, y + 10))
