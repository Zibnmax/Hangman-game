import sys
import os
from random import choice
from time import sleep

from ascii_art import hangman_logo, hang, fireworks


class HangmanGame:
    
    def __init__(self) -> None:
        self.word = self.pick_word()
        self.mistakes_letters = []
        self.display = {i:'_ ' for i in range(0, len(self.word))}
        self.clear = self.get_os_name()

    def get_os_name(self) -> str:
        '''
        Get OS name for screen clearing
        '''
        if os.name == 'nt':
            return 'cls'
        else:
            return 'clear'


    def run_intro(self) -> None:
        '''
        Running inrto and rules
        '''
        hangman_logo()
        self.player_name = input('Чтобы выиграть, нужно отгадать загаданное слово. Вы можете вводить по одной букве за раз.\n\
Слово - это существительное в единственном числе. У Вас есть 6 попыток. Удачи :)\nЧтобы продолжить, введите своё имя:\n')


    def pick_word(self) -> str:
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

    def is_letter_in_word(self, letter) -> bool:
        '''
        Checking user input
        '''
        if letter not in 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя':
            print('Пожалуйста, вводите буквы русского алфавита\n')
            return False
        
        if letter in self.mistakes_letters:
            print('Вы уже вводили эту букву, попробуйте другую\n')
            return False

        if letter not in self.word:
            self.mistakes_letters.append(letter)
            print('Такой буквы в слове нет\n')
            return False
        
        return True


    def victory(self) -> None:
        '''
        Display victory fireworks
        '''
        print('\033c')
        print(f'Вы угадали слово "{self.word.upper()}"! Поздравляю!\n\n')
        fireworks()
        sleep(5)
        sys.exit()


    def run_game(self) -> None:
        '''
        Run a game
        '''
        self.run_intro()
        os.system(self.clear)
        print('\n')
        
        while len(self.mistakes_letters) < 6:
            
            hang(mistakes=len(self.mistakes_letters))
            print(f'Количество ошибок: {len(self.mistakes_letters)}')
            print(f'Введенные Вами буквы, которых в слове нет: {" ".join(self.mistakes_letters)}')
            print(f'Слово:    {" ".join(self.display.values())}')
            
            self.letter = input('\nВведите букву: ')[0].lower()
            os.system(self.clear)
            
            if not self.is_letter_in_word(self.letter):
                continue

            
            print(f'Есть буква "{self.letter}" в слове.\n')
            for i, l in enumerate(self.word):
                if l == self.letter:
                    self.display.update({i:l})
            
            if '_ ' not in self.display.values():
                self.victory()

        print(f'Вы проиграли!\nЗагаданное слово было\n{self.word.upper()}')
        hang(mistakes=len(self.mistakes_letters))
        sleep(5)



if __name__ == '__main__':
    
    game = HangmanGame()
    game.run_game()
