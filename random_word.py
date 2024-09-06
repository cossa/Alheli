import random
# List of words to choose from
word_list = ['python', 'java', 'javascript', 'ruby', 'html', 'css']
print('python', 'java', 'javascript', 'ruby', 'html', 'css')
# Randomly select a word from the list
selected_word = random.choice(word_list)
# Initialize the user's guess
word = input( 'Guess the word ')
while True: 
    if word == selected_word:
        print('congratulations you won!')
        break
    elif word != selected_word: 
        print('wrong, try again')
        word = input( 'Guess the word')