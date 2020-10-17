import random

man = [" ___ \n", "(o^", "o)\n", "--", "|", "--\n", " / ", "\ \n"]
guess = 0 # Total guesses
wrongGuess = 0 # Total wrong guesses
maxWrongGuesses = 8 # The maximum number of wrong guesses allowed before a loss
show = []


wordLibrary = [] # List with the names of all movies

# Adds the movies from movies.txt into the wordLibrary list
with open("movies.txt") as f:
    for line in f.readlines():
        movie_name = line.strip()
        wordLibrary.append(movie_name)

def displayAndInput():
    print(*man, sep='')
    print("Number Of Guesses:- ", guess)
    print("Number Of Wrong Guesses:- ", wrongGuess)
    print("\n")
    print(*show, sep='')
    print("Enter Input:- ")
    ch1 = input()
    print("\n")
    print("*---------------------------*")
    return ch1

# Actual code starts from here
org = tuple(random.choice(wordLibrary))
rem = 0

# Generates the word with letters crossed out
for i in range(len(org)):
    if org[i] == " ":
        rem += 1
        show.append(' ')
    else:
        show.append('_')

ct = 0
fl = 0

while ct < 3:
    ch = random.randrange(0, len(org))
    if show[ch] == '_':
        show[ch] = org[ch]
        rem += 1
        ct += 1

while wrongGuess < maxWrongGuesses and rem < len(org):
    inp = displayAndInput()
    flt = 0
    guess += 1
    for i in range(0, len(org)):
        temp = "" + org[i]
        if temp.lower() == inp and show[i] == '_':
            show[i] = org[i]
            rem += 1
            flt = 1
    if flt == 0:
        wrongGuess += 1
        man = man[:-1]
    if rem == len(org):
        fl = 1

if fl == 1:
    print("Win:----  ", *org, sep='')
else:
    print("Lost")
