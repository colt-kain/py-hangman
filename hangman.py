import random

with open('words_db.txt', 'r') as db_file:
    words = [line.strip() for line in db_file.readlines()]

secret_word = random.choice(words)
display_word = []
for letter in secret_word:
    display_word += '_'

guesses_left = 7
is_game_over = False
while not is_game_over:
    print(f'[Guesses left: {guesses_left}]')
    print(' '.join(display_word) + '\n')

    user_guess = input('Guess a letter: ').lower()
    print() # For pretty console prompt

    for i, letter in enumerate(secret_word):
        if user_guess == letter:
            display_word[i] = user_guess

    if user_guess not in secret_word:
        guesses_left -= 1

        if guesses_left == 0:
            print('You lose...')
            print(f'The correct word was: "{secret_word}"')
            is_game_over = True

    if '_' not in display_word:
        print('You win!')
        print(' '.join(display_word) + '\n')
        is_game_over = True
