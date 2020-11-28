import random
import os

def new_line(multiply=1):
    print('\n'* multiply)

words = ['strength', 'Equality', 'abyss', 'azure', 'zodiac', 'zipper', 'syndrome', 'jigsaw', 'gnostic', 'injury', 'ivory', 'quiz', 'quixotic']

def draw(attempts):
    if attempts ==  7:
        print(f'\u001b[36m  ____')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print('*=====*')
        print('*=====*\u001b[0m')
    elif attempts == 6:
        print(f'\u001b[36m  ____')
        print('  |   |')
        print('      |')
        print('      |')
        print('      |')
        print('*=====*')
        print('*=====*\u001b[0m')
    elif attempts == 5:
        print('\u001b[36m  ____')
        print('  |   |')
        print('  O   |')
        print('      |')
        print('      |')
        print('*=====*')
        print('*=====*\u001b[0m')
    elif attempts == 4:
        print('\u001b[36m  ____')
        print('  |   |')
        print('  O   |')
        print('-     |')
        print('      |')
        print('*=====*')
        print('*=====*\u001b[0m')
    elif attempts == 3:
        print('\u001b[36m  ____')
        print('  |   |')
        print('  O   |')
        print('- |   |')
        print('      |')
        print('*=====*')
        print('*=====*\u001b[0m')
    elif attempts == 2:
        print('\u001b[36m  ____')
        print('  |   |')
        print('  O   |')
        print('- | - |')
        print('      |')
        print('*=====*')
        print('*=====*\u001b[0m')
    elif attempts == 1:
        print('\u001b[36m  ____')
        print('  |   |')
        print('  O   |')
        print('- | - |')
        print(' /    |')
        print('*=====*')
        print('*=====*\u001b[0m')
    else:
        print('\u001b[36m  ____')
        print('  |   |')
        print('  O   |')
        print('- | - |')
        print(' / |  |')
        print('*=====*')
        print('*=====*\u001b[0m')



#it only defines a random word for playing.
def randomword():
    word = words[random.randrange(0,(len(words)))]
    constant_word = word
    return (word, constant_word)

#it returns a tuple that returns the letter position or return a False, and return the word without the input
def storage(player_choice, word):
    to_storage = []
    for i in range(0, len(word)):
        word = list(word)
        if word[i] == player_choice:
            word[i] = '-'
            to_storage.append(i)
            word = ''.join(word)
        else:
            word = ''.join(word)
    return (to_storage, word)


#function that return the len of the word
def hyphen_representaion(word):
    return ('_'*len(word))



def selectedword(to_storage, player_choice, hyphen):
    for i in range(0, len(to_storage)):
        hyphen = list(hyphen)
        hyphen[to_storage[i]] = player_choice
        hyphen = ''.join(hyphen)
    return hyphen


def replay():
    play_again = input('\u001b[34;1m do you wanna play again? yes or no: \u001b[0m').lower()
    if play_again == 'yes':
        return True
    else:
        return False


print('Welcome to Hangman')
os.system('cls')

while True:

    attempts = 7

    word, constant_word = randomword()

    hyphen = hyphen_representaion(word)

    player_choice = ''

    play_game = input('\u001b[32;1mready to play? y or n? : \u001b[0m').lower()

    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        new_line(20)

        draw(attempts)

        to_storage, word = storage(player_choice, word)

        hyphen = selectedword(to_storage, player_choice, hyphen)

        new_line()
        print(hyphen)
        new_line(2)
        #select letter
        player_choice = input('\u001b[35;1mWhat letter do you wanna pick?: \u001b[0m').lower()


        if hyphen == constant_word:
            new_line()
            print('\033[93mYou Win\u001b[0m')
            game_on = False
        else:
            if to_storage:
                attempts = attempts
            else:
                if attempts == 0:
                    new_line()
                    print('\u001b[31mYou Failed\u001b[0m')
                    print(f'The word was {constant_word}')
                    break
                else:
                    attempts -= 1

    if not replay():
        break
