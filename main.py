import random
list_of_words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = list_of_words[random.randint(0,len(list_of_words)-1)]
word_secret = '-'*len(word)
word_secret_list = list('-'*len(word))
print('Guess the characters')
for characters in word_secret:
    print(characters)

guessed_letters = []
wrong_letters =  []

while True:
    user_character = input("guess a character: ")   
    user_character_alpha = user_character.isalpha()
    if user_character_alpha: 
        if user_character in word:
            if user_character not in guessed_letters:
                guessed_letters.append(user_character)
                for i in range (0,len(word)):
                    if user_character == word[i]:
                        word_secret_list[i] = word[i]
                        word_secret = "".join(word_secret_list)
            else:
                print("You already guessed this letter ")
        elif user_character not in word: 
            if user_character not in wrong_letters:
                wrong_letters.append(user_character)
            else:
                print("You already tried this letter ")
        if word_secret == word:
            break
    else :
        print("You must type a letter")
    for characters in word_secret:
        print(characters)
    print(f"\nRight letters guessed : {guessed_letters}\n")
    print(f"Wrong letters tried : {wrong_letters}\n")

print("You win")
print(f"The word is:  {word}")