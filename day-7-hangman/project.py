import random
from art import logo, stages
from words import word_list

chosen_word = random.choice(word_list)
display = []
lives = 6

print(logo)

for l in chosen_word:
    display.append('_')

end_of_game = False
while not end_of_game:
    guess = input('What letter do you want to guess? ').lower()

    if guess in display:
        print(f"You've already guessed letter '{guess}'")

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life. (Remaining: {lives})")
        if lives == 0:
            end_of_game = True
            print(f'You lose! The chosen word was: {chosen_word}')
    
    print(stages[lives])
    print(f"{' '.join(display)}")


    if '_' not in display:
        end_of_game = True
        print('You win!')