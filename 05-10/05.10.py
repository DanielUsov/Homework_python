import random

def randmain(a,b,c,d):
    e = 0
    while e < d:
        yield (random.choice(a) + random.choice(b) + random.choice(c))
        e = e + 1
        

for i in randmain(["Aaaa", "Bbbb", "Cccc", "Dddd"],["631", "313", "194", "612"],["eee", "ggg", "iii", "hhh"],10):
    print(i)
