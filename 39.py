import random
nambas = [0, 1, 2, 3, 4]
x = slice(1, 3) # prepare slice, similar to Array.prototype.slice

print(nambas[x], "01234"[x], random.choice(nambas)) 