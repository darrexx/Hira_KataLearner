import Symbols
import random
import sys


def asksymbol(dicti):
    key = random.choice(list(dicti.keys()))
    print(dicti[key])
    answer = input("Eingabe? ")
    if answer == "q":
        sys.exit()
    elif answer == "m":
        mainmethod()
    else:
        print(key == answer)


def learnhira():
    dicti = Symbols.HiraganaDict
    asksymbol(dicti)


def learnallhira():
    dicti = {**Symbols.HiraganaDict, **Symbols.HiraganaDigraphsDiacriticsDict, **Symbols.HiraganaDiacriticsDict,
             **Symbols.HiraganaDigraphsDict}
    asksymbol(dicti)


def learnallkata():
    dicti = {**Symbols.KatakanaDict, **Symbols.KatakanaDiacriticsDict, **Symbols.KatakanaDigraphsDiacriticsDict,
             **Symbols.KatakanaDigraphsDict}
    asksymbol(dicti)


def learnkata():
    dicti = Symbols.KatakanaDict
    asksymbol(dicti)


def learnhiradiacritics():
    dicti = Symbols.HiraganaDiacriticsDict
    asksymbol(dicti)


def learnkatadiacritics():
    dicti = Symbols.KatakanaDiacriticsDict
    asksymbol(dicti)



def learnhiradiagraphs():
    dicti = Symbols.HiraganaDigraphsDict
    asksymbol(dicti)



def learnkatadiagraphs():
    dicti = Symbols.KatakanaDigraphsDict
    asksymbol(dicti)


def learnkatadiacriticsdiagraphs():
    dicti = Symbols.KatakanaDigraphsDiacriticsDict
    asksymbol(dicti)


def learnhiradiacriticsdiagraphs():
    dicti = Symbols.HiraganaDigraphsDiacriticsDict
    asksymbol(dicti)


launchoptions = dict(h=learnhira, k=learnkata, hd=learnhiradiacritics, kd=learnkatadiacritics,
                     hdi=learnhiradiagraphs, kdi=learnkatadiagraphs, hdd=learnhiradiacriticsdiagraphs,
                     kdd=learnkatadiacriticsdiagraphs, ha=learnallhira, ka=learnallkata, q=sys.exit)


def mainmethod(i=0):
    if len(sys.argv) == 1 or i == 0:
        inputkey = input("Was möchten sie lernen? \n"
                         "h: Hiragana\n"
                         "k: Katakana\n"
                         "ha: alle Hiragana\n"
                         "ka: alle Katakana\n"
                         "hd: Hiragana mit Diacritics\n"
                         "kd: Katakana mit Diacritics\n"
                         "hdi: Hiragana mit Diagraphs\n"
                         "kdi: Katakana mit Diagraphs\n"
                         "hdd: Hiragana mit DD\n"
                         "kdd: Katakana mit DD\n")
        while True:
            launchoptions[inputkey]()
    else:
        while True:
            launchoptions[sys.argv[1]]()


if __name__ == "__main__":
    mainmethod()