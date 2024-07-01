import curses
import os
import math

class Window(object):
    def __init__(self, rows, columns, cardset):
        self.rows = rows
        self.columns = columns
        self.stdscr = curses.initscr()
        self.ovwin = curses.newwin(rows, columns, 0, 0)
        self.ttext = ""
        self.genb = curses.newwin(rows-2, columns, 1, 0)
        self.genw = curses.newwin(rows-4, columns-2, 2, 1)
        self.gtext = ""
        self.bwin = curses.newwin(1, columns-2, self.columns, 0)
        self.bwintext = ""
        self.cardset = cardset
        self.cardfl = False
        self.currentcard = self.cardset.display()

    
    def changedim(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.genb.resize(self.rows-2, self.columns)
        self.genw.resize(self.rows-4, self.columns-2)
        self.bwin.resize(1, self.columns-2)
        self.refreshwin()


    def refreshwin(self, ocontent = None, pcontent = None, bcontent = None):
        """
        ### summary
        a function to refresh both the window and the pad made, the fuck did i make this for?.

        ### params

        ocontent - content of the window\n
        pcontent - content of the pad
        """
        self.ovwin.clear()
        self.genb.clear()
        self.genw.clear()
        self.bwin.clear()

        #if nothing is passed just refresh that shit
        if ocontent == None and pcontent == None and bcontent == None:
            ocontent = self.ttext
            pcontent = self.gtext
            bcontent = self.bwintext
        else:
            self.ttext = ocontent
            self.gtext = pcontent
            self.bwintext = bcontent

        #printing respectively
        for x in ocontent:
            self.ovwin.addch(x)
        
        #centering
        sub = math.floor((self.columns - len(bcontent)) / 2)
        self.ovwin.addstr(self.rows-1, sub, bcontent)

        self.genb.border('|', '|', '-', '-', '+', '+', '+', '+')
        self.renderinpad(self.genw, pcontent, self.columns-1)

        self.ovwin.refresh()
        self.genb.refresh()
        self.genw.refresh()
        self.bwin.refresh()
    

    def start(self):
        curses.noecho()
        curses.cbreak()
        while True:
            self.currentcard = self.cardset.display()
            self.refreshwin(
                "texcards v0.1, q to exit",
                self.currentcard[1] if self.cardfl else self.currentcard[0], 
                "H Go left - |_| Flip - R Rotate - S Shuffle - Go right L"
            )
            ch = self.genb.getch()

            if ch == curses.KEY_RESIZE:
                size = os.get_terminal_size()
                self.changedim(size[1], size[0])
            #esc
            elif ch == 81 or ch == 113:
                curses.reset_shell_mode()
                break
            #r rotate key
            #elif ch == 114 or ch == 82:
            #    state = not state
            #    tstate = state
            #s shuffle key
            #elif ch == 115 or ch == 83:
            #    list, futurelist = logics.shuffle(futurelist)
            elif ch == 32:
                self.cardfl = not self.cardfl

            elif ch == 108:
                self.cardset.increment(amt = 1)

            elif ch == 104:
                self.cardset.increment(amt = -1)
            
            elif ch == 115:
                self.cardset.shuffle()

            #reading directions 4 later
            #elif ch == curses.KEY_UP and level > 0:
            #    level -= 1

            #elif ch == curses.KEY_DOWN:
            #    level += 1


        
    def renderinpad(self, pad, string, base = 73):
        """
        ### summary
        a function to render text properly without cutoffs, within a pad.

        ### params

        pad - the actual pad\n
        string - the string in question\n
        base - the pad length
        """

        amt = 0
        string = string.split(' ')
        #string tactics to not cut words across lines
        for word in string:
            word += ' '
            print(len(word), base, amt, 6)
            if len(word) > (base - amt):
                stringt = ' ' * (base-amt)
                pad.addstr(stringt)
                amt = 0
            for char in word:
                pad.addstr(char)
                amt += 1