import sys
from random import choice
from time import sleep

from ascii_art import hangman_logo, hang, fireworks

def intro() -> None:
    '''
    Running inrto and rules
    '''
    hangman_logo()
    print('Чтобы выиграть, нужно отгадать загаданное слово. Вы можете вводить по одной букве за раз.\n\
Слово - это существительное в единственном числе. У Вас есть 6 попыток. Удачи :)\n')
    
    
def pick_word() -> str:
    '''
    Picking a random word from "words.txt"
    '''
    try:
        with open('words.txt', encoding='utf_8') as file:
            words = file.readlines()
            return choice(words).rstrip('\n').lower()
    except:
        print('Что-то не так со словарем :(')
        sys.exit()

def main() -> None:
    '''
    Run a game
    '''
    word = pick_word()
    result = {i:'_ ' for i in range(0, len(word))}
    mistakes_letters = []

    while len(mistakes_letters) < 6:
        
        hang(mistakes=len(mistakes_letters))
        print(f'Количество ошибок: {len(mistakes_letters)}')
        print(f'Введенные Вами буквы, которых в слове нет: {" ".join(mistakes_letters)}')
        print(f'Слово:    {" ".join(result.values())}')
        
        letter = input('\nВведите букву: ')[0].lower()
        
        print('\033c')
        
        if letter in mistakes_letters:
            print('Вы уже вводили эту букву, попробуйте другую\n')
            continue
        if letter not in word:
            mistakes_letters.append(letter)
            print('Такой буквы в слове нет\n')
            continue
        
        print(f'Есть буква "{letter}" в слове.')
        for i, l in enumerate(word):
            if l == letter:
                result.update({i:l})
        
        if '_ ' not in result.values():
            print('\033c')
            print(f'Вы угадали слово "{word}"! Поздравляю!\n\n')
            fireworks()
            sleep(5)
            sys.exit()

    print(f'Вы проиграли!\nЗагаданное слово было\n{word.upper()}')
    hang(mistakes=len(mistakes_letters))
    sleep(5)



if __name__ == '__main__':
    
    intro()
    main()
