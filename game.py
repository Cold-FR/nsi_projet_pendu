import string
import random

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


def simpleStrategy(letters_tried: list, letters_found: list) -> str:
    letters = [letter for letter in list(string.ascii_uppercase) if
               letter not in letters_tried and letter not in letters_found]
    return random.choice(letters)


def complexStrategy(words: list, letters: str, letters_tried: list, letters_found: list) -> str:
    lenWords = [word for word in words if len(word) == len(letters)]

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


def game(isHuman, nbStrategy):
    global words
    wordToFind = random.choice(words)
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
                proposition = complexStrategy(words, wordInProgress, lettersTried, lettersFound)
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
                print(pendus[tries - 1])
                if tries < 7:
                    print(f'Il te reste {7 - tries} essais pour deviner le mot.')
                elif tries == 7:
                    print(
                        f'Tu as perdu ! Le mot à trouver était {wordToFind} !\nTu as trouvé {len(lettersFound)} lettre(s) : {wordInProgress}')
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
            break