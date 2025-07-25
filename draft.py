# elif user_character not in guessed_letter:
#             guessed_letter.append(user_character)
#             for i in range (0,len(word)):
#                 if user_character == word[i]:
#                     word_secret_list[i] = word[i]
#                     word_secret = "".join(word_secret_list)
elements = []
while True : 
    guess = input (">")
    if guess in elements:
        print("IN.")
    if guess == 'q':
        break
    if guess not in elements:
        elements.append(guess)
        print("ADDED.")
    print(elements)

print(elements)

