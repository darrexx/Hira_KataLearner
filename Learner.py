import Symbols
import random
import sys



def learnhira():
    dicti = Symbols.HiraganaDict
    key = random.choice(list(dicti.keys()))
    print(dicti[key])
    answer = input("Eingabe? ")
    print(key == answer)


def learnallhira():
    dicti = {**Symbols.HiraganaDict, **Symbols.HiraganaDigraphsDiacriticsDict, **Symbols.HiraganaDiacriticsDict,
             **Symbols.HiraganaDigraphsDict}
    key = random.choice(list(dicti.keys()))
    print(dicti[key])
    answer = input("Antwort? ")
    print(key == answer)


def learnallkata():
    dicti = {**Symbols.KatakanaDict, **Symbols.KatakanaDiacriticsDict, **Symbols.KatakanaDigraphsDiacriticsDict,
             **Symbols.KatakanaDigraphsDict}
    key = random.choice(list(dicti.keys()))
    print(dicti[key])
    answer = input("Antwort? ")
    print(key == answer)


def learnkata():
    dicti = Symbols.KatakanaDict
    key = random.choice(list(dicti.keys()))
    print(dicti[key])
    answer = input("Antwort? ")
    print(key == answer)


def learnhiradiacritics():
    dicti = Symbols.HiraganaDiacriticsDict
    key = random.choice(list(dicti.keys()))
    print(dicti[key])
    answer = input("Eingabe? ")
    print(key == answer)


def learnkatadiacritics():
    dicti = Symbols.KatakanaDiacriticsDict
    key = random.choice(list(dicti.keys()))
    print(dicti[key])
    answer = input("Eingabe? ")
    print(key == answer)


def learnhiradiagraphs():
    dicti = Symbols.HiraganaDigraphsDict
    key = random.choice(list(dicti.keys()))
    print(dicti[key])
    answer = input("Antwort? ")
    print(key == answer)


def learnkatadiagraphs():
    dicti = Symbols.KatakanaDigraphsDict
    key = random.choice(list(dicti.keys()))
    print(dicti[key])
    answer = input("Antwort? ")
    print(key == answer)


def learnkatadiacriticsdiagraphs():
    dicti = Symbols.KatakanaDigraphsDiacriticsDict
    key = random.choice(list(dicti.keys()))
    print(dicti[key])
    answer = input("Antwort? ")
    print(key == answer)


def learnhiradiacriticsdiagraphs():
    dicti = Symbols.HiraganaDigraphsDiacriticsDict
    key = random.choice(list(dicti.keys()))
    print(dicti[key])
    answer = input("Antwort? ")
    print(key == answer)


launchoptions = dict(h=learnhira, k=learnkata, hd=learnhiradiacritics, kd=learnkatadiacritics,
                     hdi=learnhiradiagraphs, kdi=learnkatadiagraphs, hdd=learnhiradiacriticsdiagraphs,
                     kdd=learnkatadiacriticsdiagraphs, ha=learnallhira)


def mainmethod():
    if len(sys.argv) == 1:
        launchoptions[input("Was möchten sie lernen? \n"
                            "h: Hiragana\n"
                            "k: Katakana\n"
                            "ha: alle Hiragana\n"
                            "ka: alle Katakana\n"
                            "hd: Hiragana mit Diacritics\n"
                            "kd: Katakana mit Diacritics\n"
                            "hdi: Hiragana mit Diagraphs\n"
                            "kdi: Katakana mit Diagraphs\n"
                            "hdd: Hiragana mit DD\n"
                            "kdd: Katakana mit DD\n")]()
    else:
        launchoptions[sys.argv[1]]()


if __name__ == "__main__":
    mainmethod()
    # learnhira()
