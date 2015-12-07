import Symbols
import random


def learnhira():
    dicti = Symbols.HiraganaDict
    key = random.choice(list(dicti.keys()))
    print(dicti[key])
    answer = input("Eingabe? ")
    print(key == answer)


def learnkata():
    dicti = Symbols.KatakanaDict
    key = random.choice(list(dicti.keys()))
    print(dicti[key])
    answer = input("Antwort? ")
    print(key == answer)


def learnhiradakuten():
    dicti = Symbols.HiraganaDakutenDict
    key = random.choice(list(dicti.keys()))
    print(dicti[key])
    answer = input("Eingabe? ")
    print(key == answer)


def learnkatadakuten():
    dicti = Symbols.KatakanaDakutenDict
    key = random.choice(list(dicti.keys()))
    print(dicti[key])
    answer = input("Eingabe? ")
    print(key == answer)

if __name__ == "__main__":
    learnhira()
