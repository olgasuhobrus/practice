# Problem Set 2, hangman.py
# Name: 
# Collaborators:
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
#secret_word = choose_word(wordlist)
#secret_word global
secret_word = 'secret'
print(secret_word)


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = letters_guessed
    letters_list = list(letters_guessed)
    word_letters = list(secret_word)
    return letters_list == word_letters


print(is_word_guessed('secret', 'SeCRet'))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_list = []
    for letter in secret_word:
        if letter in letters_guessed:
            letters_list.append(letter)
        else:
            letters_list.append('_ ')
    wordInProgress = ''.join(letters_list)
    return wordInProgress
print(get_guessed_word(secret_word, 'sdfgh'))



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters
    have not yet been guessed.
    '''
    available_letters = string.ascii_lowercase
    still_available = ''.join([letter for letter in available_letters if letter not in letters_guessed])
    return still_available

    

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
    warnings = 3
    guesses = 6
    letters_guessed = []
    vowels = list('aeoiu')

    print(f'Welcome to the game Hangman!\n '
          f'I am thinking of a word that is {len(secret_word)} letters long.\n' 
          f'You have {warnings} warnings. \n'
          f'You have {guesses} guesses.\n'
          f'Available letters: {get_available_letters(letters_guessed)}')

    while guesses > 0 and is_word_guessed(secret_word, letters_guessed) is False:

        letter_guess = input('Guess a letter: ').lower()
        if letter_guess not in list(string.ascii_lowercase):

            if warnings > 0:
                warnings -= 1
            else:
                guesses -= 1

            print(f'Oops! That is not a valid letter. \n'
                  f'Only letters of latin alphabet are allowed.' 
                  f'You have {warnings} warnings left \n'
                  f'{get_guessed_word(secret_word, letters_guessed)}')
        else:
            if letter_guess in letters_guessed:
                if warnings > 0:
                    warnings -= 1
                else:
                    guesses -= 1
                print(f'Oops! That is not a valid letter. \n'
                      f'Choose one of the available letters.\n'
                      f'You have {warnings} warnings left \n'
                      f'{get_guessed_word(secret_word, letters_guessed)}')
            elif letter_guess in secret_word:
                letters_guessed.append(letter_guess)
                print(letters_guessed)
                print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')
            else:
                print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}')
                if letter_guess in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
            letters_guessed.append(letter_guess)
            print('______________________________\n'
                f'You have {guesses} guesses left. \n'
                f'Available letters: {get_available_letters(letters_guessed)}')

    if is_word_guessed(secret_word, letters_guessed) is True:
        print(f'Congratulations, you won! '
              f'Your total score for this game is: {guesses * len(list(secret_word))}')
    else:
        print(f'You ran out of guesses. The word was {secret_word}')





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
    my_word = ''.join(my_word.split(' '))
    if len(my_word) == len(other_word):
        for x in range(len(my_word)):
            if my_word[x] != '_':
                False
            elif my_word.count(my_word[x]) != other_word.count(my_word[x]):
                return False
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    return ' '.join([other_word for other_word in wordlist if match_with_gaps(my_word, other_word) is False])

    #suggestions = []
    #for other_word in wordlist:
     #   if match_with_gaps(my_word, other_word) is False:
      #      suggestions.append(other_word)
    #if suggestions == []:
     #   print("No matches found")
    #else:
    #    print("Possible word matches are:", ' '.join(suggestions))




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
    warnings = 3
    guesses = 6
    letters_guessed = []
    vowels = list('aeoiu')

    print(f'Welcome to the game Hangman!\nI am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {warnings} warnings left.')

    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        print('-------------\n'
              f'You have {guesses} guesses left.\n'
              f'Available letters: {get_available_letters(letters_guessed)}')
        letter_guess = input('Please guess a letter: ').lower()

        if letter_guess == '*':
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))

        elif letter_guess not in list(string.ascii_lowercase):
            if warnings > 0:
                warnings -= 1
            else:
                guesses -= 1
            print(f'Oops! That is not a valid letter. You have {warnings} '
                  f'warnings left: {get_guessed_word(secret_word, letters_guessed)}')
        else:
            if letter_guess in letters_guessed:
                if warnings > 0:
                    warnings -= 1
                else:
                    guesses -= 1
                print(f"Oops! You've already guessed that letter. You have {warnings} warnings left: "
                      f"{get_guessed_word(secret_word, letters_guessed)}")
            elif letter_guess in secret_word:
                letters_guessed.append(letter_guess)
                print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')
            else:
                print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}')
                if letter_guess in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
            letters_guessed.append(letter_guess)

    print('______________________________')
    if is_word_guessed(secret_word, letters_guessed) is True:
        print(f'Congratulations, you won! '
              f'Your total score for this game is: {guesses * len(list(secret_word))}')
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
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
