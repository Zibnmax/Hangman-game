
def hangman_logo() -> None:

    '''Prints logo'''
    
    hangman_logo = '''
     _
    | |
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |____/
    '''
    print(hangman_logo)

def fireworks() -> None:
    '''Prints victory fireworks'''
    fireworks ="""                *    *
       *                *'          *          *        '
   .           *               |               /
               '.         |    |      '       |   '     *
                 \*        \   \             /
       '          \     '* |    |  *        |*                *  *
            *      `.       \   |     *     /    *      '
  .                  \      |   \          /               *
     *'  *     '      \      \   '.       |
        -._            `                  /         *
  ' '      ``._   *                           '          .      '
   *           *\*          * .   .      *
*  '        *    `-._                       .         _..:='        *
             .  '      *       *    *   .       _.:--'
          *           .     .     *         .-'         *
   .               '             . '   *           *         .
  *       ___.-=--..-._     *                '               '
                                  *       *
                *        _.'  .'       `.        '  *             *
     *              *_.-'   .'            `.               *
                   .'                       `._             *  '
   '       '                        .       .  `.     .
       .                      *                  `
     .                          *        .           *  *"""
    print(fireworks)


def hang(mistakes: int) -> None:
    '''Prints a hang in depend of mistakes'''
    hang = [
        '''
        __________
        |
        |
        |
        |
        |
    ____|__
    |      |__________
    |_________________|
    '''
    ,
    '''
        __________
        |       |
        |       O
        |
        |
        |
    ____|__
    |      |__________
    |_________________|
    '''
    ,
    '''
        __________
        |       |
        |       O
        |       |
        |       |
        |
    ____|__
    |      |__________
    |_________________|
    '''
    ,
    '''
        __________
        |       |
        |       O
        |      /|
        |       |
        |
    ____|__
    |      |__________
    |_________________|
    '''
    ,
    '''
        __________
        |       |
        |       O
        |      /|\\
        |       |
        |
    ____|__
    |      |__________
    |_________________|
    '''
    ,
    '''
        __________
        |       |
        |       O
        |      /|\\
        |       |
        |      /
    ____|__
    |      |__________
    |_________________|
    '''
    ,
    '''
        __________
        |       |
        |       O
        |      /|\\
        |       |
        |      / \\
    ____|__
    |      |__________
    |_________________|
    '''
    ]
    
    print(hang[mistakes])


if __name__ == '__main__':
    hangman_logo()
    hang()
