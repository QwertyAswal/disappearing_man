import random


class model:
    man = [" ___ \n", "(o^", "o)\n", "--", "|", "--\n", " / ", "\ \n"]
    guess = 0
    wrongGuess = 0
    show = []
    wordLibrary = ["Vikram Vedha", "Taare Zameen Par", "Andhadhun", "Bhaag Milkha Bhaag", "Jo Jeeta Wohi Sikandar",
                   "Paan Singh Tomar", "Rang De Basanti", "Gangs of Wasseypur", "A Wednesday", "Dil Chahta Hai",
                   "Zindagi Na Milegi Dobara", "Lage Raho Munna Bhai", "Baahubali", "Bajrangi Bhaijaan", "Gangaajal"]


class view:
    def displayAndInput():
        print(*model.man, sep='')
        print("Number Of Guesses:- ", model.guess)
        print("Number Of Wrong Guesses:- ", model.wrongGuess)
        print("\n")
        print(*model.show, sep='')
        ch1 = input("Enter Input:- ")
        print("\n")
        print("*---------------------------*")
        return ch1


org = tuple(random.choice(model.wordLibrary))
rem = 0;
for i in range(len(org)):
    if org[i] == " ":
        rem += 1
        model.show.append(' ')
    else:
        model.show.append('_')
ct = 0
fl = 0
while ct < 3:
    ch = random.randrange(0, org.__len__())
    if model.show[ch] == '_':
        model.show[ch] = org[ch]
        rem += 1
        ct += 1
while model.wrongGuess < 8 and rem < org.__len__():
    inp = view.displayAndInput()
    flt = 0
    model.guess += 1
    for i in range(0, org.__len__()):
        temp = "" + org[i]
        if temp.lower() == inp and model.show[i] == '_':
            model.show[i] = org[i]
            rem += 1
            flt = 1
            # break
    if flt == 0:
        model.wrongGuess += 1
        model.man = model.man[:-1]
    if rem == org.__len__():
        fl = 1;
if fl == 1:
    print("Win:----  ", *org, sep='')
else:
    print("Lost")
