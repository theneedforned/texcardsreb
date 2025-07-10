import json
import random
# Message Box

class cardSet:
    def __init__(self, type, data):
        if type == "file":
            print(data)
            self.wordlist, self.jsonlist2 = self.fetchlist(data, 'file')
        self.inverse = False
        self.position = 0

    def __str__(self):
        a = f"{self.wordlist} --- {self.jsonlist2}"
        return a
    
    def display(self):
        return self.wordlist[self.position][::-1] if self.inverse else self.wordlist[self.position]
    
    def increment(self, amt = 0, inv = False):
        self.inverse = True if inv == True else False
        self.position += amt
        if self.position < 0:
            self.position = len(self.wordlist) - 1
        elif self.position == len(self.wordlist):
            self.position = 0
        #messagebox.showinfo("Title", f"position changed to {self.position}")
        
        return True
    
    
    #@classmethod
    def shuffle(self):
        '''
        mydict = {

        }
        mylist = []
        keys = list(self.cards.keys())
        random.shuffle(keys)
        for key in keys:
            mydict[key] = self.cards[key]
        for k, v in mydict.items():
        mylist.append([k, v])
        '''
        random.shuffle(self.wordlist)
        print(self.wordlist)
        return True
        #return mylist, mydict


    def fetchlist(self, info, forid):
        if forid == 'id' and info == 'debug':
            list = [
                ["word1", "this is the definition for word one"],
                ["word2", "this is the definition for word two"],
                ["word3", "this is the definition for word three"],
                ["word4", "this is the definition for word four"]
            ]
            return list
        if forid == 'file':
            jsonlist = open(info, 'r')
            jsonlist2 = json.loads(jsonlist.read())
            jsonlist.close()
            list = []
            for k, v in jsonlist2.items():
                list.append([k, v])
            return list, jsonlist2