from texparser import cardSet

cardset = cardSet('file', 'test.json')
print(cardset.display())
print(cardset.position)
cardset.increment(amt = 1, inv = True)
print(cardset.position)
a = cardset.display()
print(a)