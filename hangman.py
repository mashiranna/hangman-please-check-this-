# Problem Set 2, hangman.py
# Name: Anna Mashyr
# Collaborators: Llanowar
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    counter = 0
    for element in secret_word:
        if element in letters_guessed:
            counter += 1
    return counter == len(secret_word)


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    word = list('_' * len(secret_word))

    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            index = letters_guessed.index(secret_word[i])
            word[i] = letters_guessed[index]
    return(' '.join(word))



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    available_letters = sorted(list(set(all_letters) - set(letters_guessed)))
    return (', '.join(available_letters))

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    guesses = 6
    warnings = 0
    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters_guessed = []
    vowels = ['a', 'o', 'u', 'e', 'i']

    print('Secret word contains', len(secret_word), 'letters')

    while guesses > 0:

        print('You have', guesses, 'guesses left')
        print('You have', 3 - warnings, 'warnings left')
        print(get_guessed_word(secret_word, letters_guessed))

        letter = input('Please, guess a letter: ').lower()

        while letter not in all_letters:
            print('Invalid symbol. Try again.')
            if warnings != 3:
                warnings += 1
                print('You have', 3 - warnings, 'warnings left')
            if warnings == 3:
                print('You have just lost 1 life')
                guesses -= 1
                print('You have', guesses, 'guesses left')

            if guesses < 0:
                print('You lose!')
                break

            letter = input('Please, guess a letter: ').lower()

        while letter in letters_guessed:
            print('You have already used this letter. Try another one')
            if warnings != 3:
                warnings += 1
                print('You have', 3 - warnings, 'warnings left')
            if warnings == 3:
                print('You have just lost 1 life')
                guesses -= 1
                print('You have', guesses, 'guesses left')

            if guesses < 0:
                print('You lose!')
                break

            letter = input('Please, guess a letter: ').lower()
            while letter not in all_letters:
                print('Invalid symbol. Try again.')
                if warnings != 3:
                    warnings += 1
                    print('You have', 3 - warnings, 'warnings left')
                if warnings == 3:
                    print('You have just lost 1 life')
                    guesses -= 1
                    print('You have', guesses, 'guesses left')

                if guesses < 0:
                    print('You lose!')
                    break

                letter = input('Please, guess a letter: ').lower()

            if guesses < 0:
                break

        if guesses < 0:
            print('You lose!')
            break

        letters_guessed.append(letter)


        if letter not in secret_word:
            print('Oops! This letter is not in secret word.')
            guesses -= 1
            if letter in vowels:
                guesses -= 1
        else:
            print('Oooh!!! You guessed a letter. You are a lucky person!')
            print(get_guessed_word(secret_word, letters_guessed))

        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations!!! You won.')
            print('Your total score for this game is:', guesses * len(set(secret_word)))
            break

        print('Available letters:\n', get_available_letters(letters_guessed))
        print('Used letters:\n', ', '.join(letters_guessed))

    print('Secret word was', secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''

    counter = 0

    letters = list(other_word)

    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if list(my_word)[i] == letters[i]:
                counter += 1
            elif list(my_word)[i] == '_':
                if letters[i] in list(my_word):
                    counter -= 1
                else:
                    counter += 1

    return counter == len(my_word)



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''

    possible_matches = []

    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)

    if len(possible_matches) == 0:
        print('No matches found!')
    else:
        print(', '.join(possible_matches))


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''

    guesses = 6
    warnings = 0
    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters_guessed = []
    vowels = ['a', 'o', 'u', 'e', 'i']

    print('Secret word contains', len(secret_word), 'letters')

    while guesses > 0:

        my_word = ''.join(get_guessed_word(secret_word, letters_guessed).split(' '))

        print('You have', guesses, 'guesses left')
        print('You have', 3 - warnings, 'warnings left')
        print(get_guessed_word(secret_word, letters_guessed))

        letter = input('Please, guess a letter: ').lower()

        while letter == '*':
            print('Possible words:')
            show_possible_matches(my_word)
            letter = input('Please, guess a letter: ').lower()

        while letter not in all_letters:
            print('Invalid symbol. Try again.')
            if warnings != 3:
                warnings += 1
                print('You have', 3 - warnings, 'warnings left')
            if warnings == 3:
                print('You have just lost 1 life')
                guesses -= 1
                print('You have', guesses, 'guesses left')

            if guesses < 0:
                print('You lose!')
                break

            letter = input('Please, guess a letter: ').lower()

        while letter in letters_guessed:
            print('You have already used this letter. Try another one')
            if warnings != 3:
                warnings += 1
                print('You have', 3 - warnings, 'warnings left')
            if warnings == 3:
                print('You have just lost 1 life')
                guesses -= 1
                print('You have', guesses, 'guesses left')

            if guesses < 0:
                print('You lose!')
                break

            letter = input('Please, guess a letter: ').lower()
            while letter not in all_letters:
                print('Invalid symbol. Try again.')
                if warnings != 3:
                    warnings += 1
                    print('You have', 3 - warnings, 'warnings left')
                if warnings == 3:
                    print('You have just lost 1 life')
                    guesses -= 1
                    print('You have', guesses, 'guesses left')

                if guesses < 0:
                    print('You lose!')
                    break

                letter = input('Please, guess a letter: ').lower()

            if guesses < 0:
                break

        if guesses < 0:
            print('You lose!')
            break

        letters_guessed.append(letter)


        if letter not in secret_word:
            print('Oops! This letter is not in secret word.')
            guesses -= 1
            if letter in vowels:
                guesses -= 1
        else:
            print('Oooh!!! You guessed a letter. You are a lucky person!')
            print(get_guessed_word(secret_word, letters_guessed))

        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations!!! You won.')
            print('Your total score for this game is:', guesses * len(set(secret_word)))
            break

        print('Available letters:\n', get_available_letters(letters_guessed))
        print('Used letters:\n', ', '.join(letters_guessed))

    print('Secret word was', secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


#if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
