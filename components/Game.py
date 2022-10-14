from typing import Tuple
import pygame as pg
import vlc
from gameinfo import DB
from datetime import date

from utils.date import days_elapsed
from utils.db import write_db
from dateutil import parser


class Game:
    """
    The Game class is the main class of the program. It handles the main game logic.
    It has several methods, including some of them that are called every frame.

    - `draw_screen`: Draws the current screen
    - `handle_events`: Handles the events of the current screen

    It also has some useful methods, such as:

    - `register_click_event`: Registers a click event
    - `play_audio`: Plays an audio file
    - `update_streak`: Updates the streak
    - `change_screen`: Changes the current screen
    - `quit`: Quits the program gracefully
    """

    def __init__(self, w, h, t, s):
        """
        ### The constructor of the Game class.
        Handles the initialization of the game, this includes:

        Program info:
        - w: Width of the window
        - h: Height of the window
        - t: Title of the window
        - s: Screens of the game

        Other initialization:
        - run: Whether the game is running or not
        - click_events: Click events of the game
        - current_screen: Current screen of the game
        - WIN (pygame.Surface): Window of the game
        """
        self.width = w
        self.height = h
        self.title = t
        self.run = True

        self.click_events: list[Tuple[pg.Rect, function]] = []
        self.screens = s
        self.current_screen = self.screens[0]
        self.WIN = pg.display.set_mode((w, h))
        pg.display.set_caption(t)

    def draw_screen(self):
        """
        ### This function is called every frame. Mind the performance.
        Draws the current screen by calling `self.current_screen(self)`.
        """
        self.current_screen(self)

    # Gets called every frame -> keep fast
    def handle_events(self):
        """
        ### This function is called every frame. Mind the performance.
        Handles the events of the current screen.

        Returns whether the game is running or not.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

            elif event.type == pg.MOUSEBUTTONDOWN:
                for click_event in self.click_events:
                    mouse_x, mouse_y = pg.mouse.get_pos()
                    rect, onClick = click_event
                    if rect.collidepoint(mouse_x, mouse_y):
                        onClick()

        return self.run

    def register_click_event(self, event):
        """
        ### Registers a click event.
        - event: A tuple of the form (rect, onClick)

        The rect is the rectangle that will be checked for collision with the mouse.
        The onClick is the function that will be called when the mouse collides with the rect.
        """
        self.click_events.append(event)

    def play_audio(self, path):
        """
        ### Plays an audio file.
        - path: Path to the audio file
        """
        p = vlc.MediaPlayer(path)
        p.play()

    def update_streak(self):
        """
        ### Updates the streak.

        The streak is the number of days in a row that the user has studied.

        The streak is stored in the database, in the `streak` key.
        The last day the user studied is stored in the `last` key.

        The streak is updated by checking the difference between the current date and the last date the user studied.
        If the difference is 1, then the streak is incremented by 1.
        If the difference is 0, then the streak is not changed.
        If the difference is greater than 1, then the streak is set to 1.
        """
        last = parser.parse(DB["streak"]["last"], dayfirst=True)
        today = date.today()

        elapsed = days_elapsed(today, date(last.year, last.month, last.day))

        if elapsed == 1:
            DB["streak"]["current"] += 1
        elif elapsed > 1:
            DB["streak"]["current"] = 0

        if DB["streak"]["current"] > DB["streak"]["best"]:
            DB["streak"]["best"] = DB["streak"]["current"]

        DB["streak"]["last"] = date.today().strftime("%d/%m/%Y")

    def change_screen(self, idx):
        """
        ### Changes the current screen.

        - idx: Index of the screen to change to

        The index is the index of the screen in the `self.screens` list.
        """
        self.current_screen = self.screens[idx]

    def quit(self):
        """
        ### Quits the program gracefully.

        Writes the database to the file.
        This function is called when the user clicks the close button.
        """
        write_db(DB, "data.txt")
        print("Shutting down gracefully...")
        self.run = False
