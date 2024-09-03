while True:
    guess = int(input('Pick a number between 1 and 10: '))
    if guess == 3:
        print('You won')
        break
    elif guess > 10 or guess < 1:
        print ('unvalid number')
    elif guess < 3:
        print('too low')
    elif guess > 3:
        print('too high')
    
