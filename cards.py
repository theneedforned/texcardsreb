from curses import wrapper
import argparse
import window
import os

def main():
    size = os.get_terminal_size()
    win = window.Window(size[1], size[0])
    win.start()
