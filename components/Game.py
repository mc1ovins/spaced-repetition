from typing import Tuple
import pygame as pg
import vlc
from gameinfo import DB
from datetime import date
from utils.date import days_elapsed
from utils.db import write_db
from dateutil import parser


class Game:
    def __init__(self, w, h, t, s):
        self.width = w
        self.height = h
        self.title = t
        self.run = True

        self.click_events = []
        self.custom_event_handlers = []
        self.screens = s
        self.current_screen = self.screens[0]
        self.WIN = pg.display.set_mode((w, h))
        pg.display.set_caption(t)

    def draw_screen(self):
        self.current_screen(self)

    def handle_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.run = False

            elif event.type == pg.MOUSEBUTTONDOWN:
                for click_event in self.click_events:
                    mouse_x, mouse_y = pg.mouse.get_pos()
                    rect, onClick = click_event
                    if rect.collidepoint(mouse_x, mouse_y):
                        onClick()

        for custom_handler in self.custom_event_handlers:
            custom_handler(events)

        return self.run
    
    def register_custom_event_handler(self, handler):
        self.custom_event_handlers.append(handler)

    def register_click_event(self, event):
        self.click_events.append(event)

    def play_audio(self, path):
        p = vlc.MediaPlayer(path)
        p.play()

    def update_streak(self):
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
        self.current_screen = self.screens[idx]

    def quit(self):
        write_db(DB, "data.txt")
        print("Shutting down gracefully...")
        self.run = False
