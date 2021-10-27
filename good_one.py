#pint BMI calculater with age & height + BOLD Char in printing
w = float(input("what's ur weight in kg"))
h = float(input("what's ur height in meter"))

bmi = w / (h * h)
bmi = round(bmi, 2)
print(bmi)

s = '\033[1m'
e = '\033[0m'

if bmi <= float(18.5):
    print(f"ur BMI is {bmi} and it is {s}under weight{e}.")
elif bmi <= float(25):
    print(f"ur BMI is {bmi} and it is {s}normal weight{e}.")
elif bmi <= float(30):
    print(f"ur BMI is {bmi} and it is {s}over weight{e}.")
elif bmi <= float(35):
    print(f"ur BMI is {bmi} and it is {s}obese weight{e}.")
elif bmi > float(35):
    print(f"ur BMI is {bmi} and it is check with {s}DR for ur weight{e}.")

###################################################



h = int(input("enter u r height"))
age = int(input("Enter age"))
photo= input("u need photo than say y if no than say N")
if h <= 100:
    if age <= 12:
        bill = 10
        print(f"ur age {age} is less than 12 years please pay 10 ")
    elif age <= 18:
        bill = 20
        print(f"ur age {age} is between 12-18, please pay 20 ")
    elif age <= 60:
        bill = 150
        print(f"ur age {age} is between 18-60 years, please pay 150")
    elif age > 60:
        bill = 0
        print(f"ur age is greater than {age}, it is free for u ")
    else:
        pass


    if photo == "y" or photo == "Y":
        bills = int(bill) + int(3)
        print(f"Please pay additional {bills} RS")
    else:
        print(f"pls pay regular fee no additional pay {bill}")

else:
    print("Sorry ur height is less")

###########################################################


print("welcome to the GAME")
player = input("to play either press right or left\n....").lower()

if player == "right" or player == "r":
    print("\ngoing to right direction , u will see SEA soon")
    player = input("to play either press right or left\n....").lower()
    if player == "right" or player == "r":
        print("going to right direction , u will see CAR soon")
        player = input("to play either press right or left\n....").lower()
        if player == "right" or player == "r":
            print("going to right direction , u will see TV soon")
            print("WOOOOOOOOOOON")
        elif player == "left" or player == 'l':
            print("GOING NO WHERE, GAME OVER")
        else:
            print("GAME OVEEEEEEEEEER")
    else:
        print("GAME OVER, u fell in SEA")
else:
    print("GAME OVER, u fell in SEA")



###########################################################


###########################################################

###########################################################

###########################################################


###########################################################


###########################################################


###########################################################


###########################################################

###########################################################

###########################################################


###########################################################


###########################################################


###########################################################


###########################################################

###########################################################

###########################################################


###########################################################


###########################################################


###########################################################


###########################################################

###########################################################

###########################################################


###########################################################


###########################################################


###########################################################


###########################################################

###########################################################

###########################################################


###########################################################


###########################################################