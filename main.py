import curses
from curses import wrapper
import argparse
import cards.cards as cards

parser = argparse.ArgumentParser(prog = 'texcards',
                    description = 'CLI script to study flashcards',
                    epilog = 'made by theNeedForNed')
parser.add_argument('--id', type=str, required=False, help='Load flash cards using an ID')
parser.add_argument('--file', type=str, required=False, help='Load flash cards using a JSON file')
parser.add_argument('-q', '--quiz',
                    action='store_true')

args = parser.parse_args()
print(args)
cards.main(file = args.file)