import random

man = [" ___ \n", "(o^", "o)\n", "--", "|", "--\n", " / ", "\ \n"]
guess = 0
wrongGuess = 0
show = []
wordLibrary = ["Vikram Vedha", "Taare Zameen Par", "Andhadhun", "Bhaag Milkha Bhaag", "Jo Jeeta Wohi Sikandar",
               "Paan Singh Tomar", "Rang De Basanti", "Gangs of Wasseypur", "A Wednesday", "Dil Chahta Hai",
               "Zindagi Na Milegi Dobara", "Lage Raho Munna Bhai", "Baahubali", "Bajrangi Bhaijaan", "Gangaajal"]


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


org = tuple(random.choice(wordLibrary))
rem = 0;
for i in range(len(org)):
    if org[i] == " ":
        rem += 1
        show.append(' ')
    else:
        show.append('_')
ct = 0
fl = 0
while ct < 3:
    ch = random.randrange(0, org.__len__())
    if show[ch] == '_':
        show[ch] = org[ch]
        rem += 1
        ct += 1
while wrongGuess < 8 and rem < org.__len__():
    inp = displayAndInput()
    flt = 0
    guess += 1
    for i in range(0, org.__len__()):
        temp = "" + org[i]
        if temp.lower() == inp and show[i] == '_':
            show[i] = org[i]
            rem += 1
            flt = 1
    if flt == 0:
        wrongGuess += 1
        man = man[:-1]
    if rem == org.__len__():
        fl = 1;
if fl == 1:
    print("Win:----  ", *org, sep='')
else:
    print("Lost")
