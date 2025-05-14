import os, time

print('\033[?25l', end="") # hide cursor

# print 1 - 10 with a space after each number instead on newline
# for i in range(10):
#     print(i, end=" "); # use end param to add space after every number

# for i in range(20):
#     print(i, sep=', ') #add a separator


for i in range(5): # print 0 -19 one after the other
    print(i, sep=', ') 
    time.sleep(0.2) 
    os.system("clear")


def println(color, word):
    if color == 'red':
        print('\033[31m', word, sep="", end = "")
    elif color == 'green':
        print('\033[32m', word, sep="", end = "")
    elif color == 'blue':
        print('\033[33m', word, sep="", end = "")
    else:
        print('\033[0m', word, sep="", end = "")


println('green', 'Now is the best time ')
println('blue', 'to go lock in ')
println('red', 'It\'s now or never! ')
println('white', 'now or never !!! ')