import os
import pygame as pg


def load_image(filename):
    return pg.image.load(os.path.join("assets", filename))
