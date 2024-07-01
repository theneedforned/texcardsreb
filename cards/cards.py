from curses import wrapper
from .texparser import cardSet
from .window import Window
import os

def main():
    size = os.get_terminal_size()
    cardset = cardSet('file', 'test.json')
    win = Window(size[1], size[0], cardset)
    win.start()
