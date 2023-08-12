import curses
import os


class Window(object):
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.stdscr = curses.initscr()
        self.ovwin = curses.newwin(rows, columns, 0, 0)
        self.ttext = ""
        self.genb = curses.newwin(rows-1, columns, 1, 0)#(columns//2)-10, 1,columns//2+1)
        self.genw = curses.newwin(rows-3, columns-2, 2, 1)#(columns//2)-10, 1,columns//2+1)
        self.gtext = ""
        #self.bwin = curses.newwin(1, columns-2, self.columns, 0)#(columns//2)-10, 1,columns//2+1)

    
    def changedim(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.genb.resize(self.rows-1, self.columns)
        self.genw.resize(self.rows-3, self.columns-2)
        self.refreshwin()


    def refreshwin(self, ocontent = None, pcontent = None):
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

        if ocontent == None and pcontent == None:
            ocontent = self.ttext
            pcontent = self.gtext
        else:
            self.ttext = ocontent
            self.gtext = pcontent

        for x in ocontent:
            self.ovwin.addch(x)
        
        self.genb.border('|', '|', '-', '-', '+', '+', '+', '+')
        self.renderinpad(self.genw, pcontent, self.columns-1)
        
        self.ovwin.refresh()
        self.genb.refresh()
        self.genw.refresh()
    

    def start(self):
        curses.noecho()
        curses.cbreak()
        self.refreshwin(f"E", "e")
        while True:
            ch = self.genb.getch()
            if ch == curses.KEY_RESIZE:
                size = os.get_terminal_size()
                self.gtext = str(size)
                self.changedim(size[1], size[0])
                #self.refresh(f"{size.columns}, {size.lines}", "e")

        
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