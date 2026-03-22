import random
import time
while True:
    time.sleep(1)
    print("Choose between Stone, Paper and Scissor")
    time.sleep(1)
    Choices = ('s','p','r')
    Your_choice = input("What is your choice?(R,P,S) ").strip().lower()
    if Your_choice not in Choices:
        print('Choose a suitable choice')
        time.sleep(2)
        continue
    Transform = {'s':'Scissors ✂️','r':' Stone 🪨','p':'Paper 📜'}
    My_choice = random.choice(Choices)
    print(f'''Your choice is {Transform[Your_choice]}''')
    time.sleep(1)
    print(f'''My choice is {Transform[My_choice]}''')
    time.sleep(2)
    if Your_choice == 'r' and My_choice == 's' \
    or Your_choice == 'p' and My_choice == 'r'\
    or Your_choice == 's' and My_choice == 'p' :
        print('Congo! you win 🍾')
    elif Your_choice == My_choice :
        print('''It's a tie''')
    else:
        print('Yay! I win 🏆')
    time.sleep(1)
    Repeat = input('Do you want to continue?(y/n) ')
    if Repeat != 'y':
        time.sleep(1)
        print('GG!🫡')
        break
