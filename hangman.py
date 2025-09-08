import random
word_list = ["python","java","mernstack"]
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("word to guess :" + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"{lives}/6 left")
    guess = input("guess a letter :").lower()
    if guess in correct_letters:
        print(f"you have already guessed {guess}")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    # moved outside the loop
    print("word to guess :" + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess}, that's not the word.")
        if lives == 0:
            print(f"it was {chosen_word}! you lose")
            game_over = True

    if "_" not in display:
        game_over = True
        print("you win")
