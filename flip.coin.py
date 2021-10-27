import random

x = input('Please press "Y" to flip coin\n ....' )
xx = random.randint(1,2)

if x == 'y' or x == 'Y':
    if xx == 1:
        print("HEADS")
    elif xx == 2:
        print("TAILS")
else:
    print('u did not choose flip coin')
