#HANGMAN GAME
import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')


display = []
for n in chosen_word:
    display.append('_')
print(display)
lose = 6
win = False
number = int(len(chosen_word))
while win == False:
    guess = input("Guess a letter: ").lower()
    print(f"You guessed {guess}")
    for n in range(number) :
        letter = chosen_word[n]
        if letter == guess:
            display[n] = guess
            if '_' not in display:
                win = True

    if not guess in chosen_word:
        lose -= 1
        print("That's not in the word. You lose a life. :( ")
    if guess in display:
        print("You've already guessed that letter. Pick another one")

    

    print(hangman_art.stages[lose])            
    if lose == 0:
        print('You Lose.')
        break
    print(f'Correct answer:\n{display}\n\n')
else:
    print('You won!')