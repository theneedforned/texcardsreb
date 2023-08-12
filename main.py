import curses
from curses import wrapper
import argparse
import window
import cards

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

parser.add_argument('-f' ,'--filename')           # positional argument
parser.add_argument('-q', '--quiz', action='store_true')      # option that takes a value
#parser.add_argument('-v', '--verbose',
#                    action='store_true')  # on/off flag
args = parser.parse_args()

#if args.filename != None:
print(args.filename, args.quiz)

cards.main()
#win = window.Window()
#wrapper()

