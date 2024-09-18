import random

def print_with_stars(message):
    print(f"********** {message}*****")

def user_ch():
    while True:
        print_with_stars('Choose 1 for rock, 2 for paper or 3 for scissors')
        user_ch = input("Enter your number: ")
        
        if user_ch == "quit":
            break
    
        if user_ch not in ["1", "2", "3"]:
            print_with_stars("not allow")
            continue 
    
        user_ch = int(user_ch)    
        computer_ch = random.randint(1,3)

        if  user_ch == computer_ch:
            print_with_stars("tie")
        elif (user_ch == "1" and computer_ch == "3") or (user_ch == "2" and computer_ch == "1") or (user_ch == "3" and computer_ch == "2"):
            print_with_stars("won")
        else:
            print_with_stars("lose")
    
user_ch()