# Hangman is a puzzle game in which a player tries to guess a word letter by letter.
# If you fail, you'll be “hanged”. If you win, you'll survive. 

# random module
import random

print("H A N G M A N")

# play the game if a player enters 'play' or exit if a player enters 'exit'
while True:

    # select the menu to play the game
    menu_selection = input('Type "play" to play the game, "exit" to quit: > ')
    print()

    # play the game
    if menu_selection == 'play':
        words_list = ['python', 'java', 'kotlin', 'javascript']
        random_word = words_list[random.randint(0, ((len(words_list)) - 1))]
        hidden_word = random_word.replace(random_word, '-' * len(random_word))
        print(hidden_word)
        characters_list = list(hidden_word)
        progress = "".join(characters_list)

        # total lives for guessing word
        lives = 8

        # lists containing already guessed characters and guessed letters
        guessed_words = []
        letter_list = []

        # loop runs until lives == 0
        while lives != 0:

            # guess for the random character according to the rules defined
            # character guessed must be a single lowercase english letter
            guess = input("Input a letter: > ")
            letter_list = list(guess)
            while not guess.isalpha() or not guess.islower() or not len(letter_list) == 1:
                if len(letter_list) == 1:
                    if not guess.isalpha():
                        print("Please enter a lowercase English letter\n")
                        print(progress)
                        guess = input("Input a letter: > ")
                        letter_list = list(guess)
                    elif not guess.islower():
                        print("Please enter a lowercase English letter\n")
                        print(progress)
                        guess = input("Input a letter: > ")
                        letter_list = list(guess)
                else:
                    print("You should input a single letter\n")
                    print(progress)
                    guess = input("Input a letter: > ")
                    letter_list = list(guess)

            # guess the word again if player guess the same word again
            if guess in guessed_words:
                print("You've already guessed this letter\n")
                print(progress)
                continue

            # print the progress if the guessed character is in random word
            elif guess in random_word:
                guessed_words.append(guess)
                index_list = [index for index in range(len(random_word)) if random_word.startswith(guess, index)]
                for j in index_list:
                    characters_list[j] = guess
                progress = "".join(characters_list)
                if progress == random_word:
                    print("You guessed the word", progress + "!")
                    break
                else:
                    print()
                    print(progress)

            # reduce the lives by 1 if the character guessed is not in the random word
            else:
                if lives == 1:
                    print("That letter doesn't appear in the word")
                    lives -= 1
                else:
                    print("That letter doesn't appear in the word", "\n")
                    lives -= 1
                    guessed_words.append(guess)
                    index_list = [index for index in range(len(random_word)) if random_word.startswith(guess, index)]
                    for j in index_list:
                        characters_list[j] = guess
                    progress = "".join(characters_list)
                    print(progress)
        print("You survived!" if progress == random_word else "You lost!")
        print()

    # exit the game
    elif menu_selection == 'exit':
        break

    # ask to enter the menu again if a player entered anything other than 'play' or 'exit'
    else:
        continue
