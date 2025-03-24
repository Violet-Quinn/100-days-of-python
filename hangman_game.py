import random
hangman= [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']
lives=6
word_list = [
    'python', 'hangman', 'challenge', 'programming', 'development',
    'function', 'variable', 'syntax', 'algorithm', 'testing']
chosen_word=random.choice(word_list)
print(chosen_word)
placeholder = ["_"] * len(chosen_word)
print("".join(placeholder))
game_over=False
correct_letters=[]

while not game_over:
    print("========",lives," lives remaining========")

    guess=input("guess a random alphabet for the word:").lower()
    print(guess)
    word = ""
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over = True
            print(f"The chosen word was {chosen_word}")
            print("Game Over")

    if guess in correct_letters:
        print("You already guessed that letter!")
        continue

    for letter in chosen_word:
        if guess == letter:
            word+=guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            word+=letter
        else:
            word+="_"
# word="".join(word)
    print(word)
    if "_" not in word:
        game_over=True
        print("You won")

    print(hangman[lives])
if game_over:
    print("Game Over")