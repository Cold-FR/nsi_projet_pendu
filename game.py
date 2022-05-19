import string
import random
from xmlrpc.client import Boolean

pendus = [
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
    ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
]

with open('mots.txt', 'r') as f:
    words = f.read().splitlines()

with open('mots_bis.txt', 'r', encoding='latin-1') as f:
    words_bis = f.read().splitlines()

def simpleStrategy(letters_tried: list, letters_found: list) -> str:
    letters = [letter for letter in list(string.ascii_uppercase) if
               letter not in letters_tried and letter not in letters_found]
    return random.choice(letters)


def complexStrategy(words: list, letters: str, letters_tried: list, letters_found: list) -> str:
    lenWords = [word.upper() for word in words if len(word) == len(letters)]

    lettersWords = []
    for word in lenWords:
        isOk = [False] * len(letters)
        for i in range(0, len(letters)):
            if word[i] in letters_tried:
                break

            if word[i] == letters[i] or letters[i] == '_':
                isOk[i] = True

        result = all(elem is True for elem in isOk)
        if result:
            lettersWords.append(word)

    lettersProbabilities = {}
    for word in lettersWords:
        lettersFetched = []
        for letter in word:
            if letter not in letters_found and letter not in lettersFetched:
                lettersFetched.append(letter)
                lettersProbabilities[letter] = lettersProbabilities.get(letter, 0) + 1

    lettersProbabilities = dict(sorted(lettersProbabilities.items(), reverse=True, key=lambda item: item[1]))
    return list(lettersProbabilities.keys())[0]


def game(isHuman: bool, nbStrategy: int, nbList: int):
    global words
    global words_bis
    parties = {
        'count': 0,
        'victories': 0,
        'defeats': 0,
        'tries': []
    }
    while parties['count'] != 5000 or (isHuman == True and parties['count'] != 1):
        wordsList = []
        if nbList == 1: 
            wordsList = words
        elif nbList == 2:
            wordsList = words_bis
        else:
            print('Liste introuvable')
            break
        wordToFind = random.choice(wordsList).upper()
        wordInProgress = '_' * len(wordToFind)
        lettersTried = []
        lettersFound = []
        tries = 0
        while wordInProgress != wordToFind:
            if isHuman:
                proposition = input('Proposition de lettre : ').upper()
            else:
                if nbStrategy == 1:
                    proposition = simpleStrategy(lettersTried, lettersFound)
                elif nbStrategy == 2:
                    proposition = complexStrategy(wordsList, wordInProgress, lettersTried, lettersFound)
                else:
                    print('Stratégie introuvable.')
                    break
            print(f'\nTa proposition est : {proposition}')
            if proposition in wordToFind and proposition not in lettersFound:
                lettersFound.append(proposition)
            elif proposition not in wordToFind:
                if proposition not in lettersTried:
                    lettersTried.append(proposition)
                    tries += 1
                    parties['tries'] += [tries]
                    print(pendus[tries - 1])
                    if tries < 7:
                        print(f'Il te reste {7 - tries} essais pour deviner le mot.')
                    elif tries == 7:
                        print(
                            f'Tu as perdu ! Le mot à trouver était {wordToFind} !\nTu as trouvé {len(lettersFound)} lettre(s) : {wordInProgress}')
                        if isHuman == False:
                            parties['defeats'] += 1
                            parties['count'] += 1
                        break
                else:
                    print('Tu as déjà essayé cette lettre.')
            elif proposition in lettersTried:
                print('Tu as déjà essayé cette lettre.')

            wordInProgress = wordToFind
            for letter in wordInProgress:
                if letter not in lettersFound:
                    wordInProgress = wordInProgress.replace(letter, '_')

            print(f'Voici la liste des lettres que tu as essayé : {",".join(lettersTried)}')
            print(f'Voici les lettres que tu as trouvé : {wordInProgress}')

            if wordInProgress == wordToFind:
                print(f'Tu as gagné ! Le mot était {wordToFind}')
                if isHuman == False:
                    parties['victories'] += 1
                    parties['count'] += 1
                break
    
    if parties['count'] == 1000 and isHuman == False:
        print(f'L\'IA a gagné {parties["victories"]} parties et a perdu {parties["defeats"]} parties avec une moyenne de {sum(parties["tries"])/len(parties["tries"])} essais.')