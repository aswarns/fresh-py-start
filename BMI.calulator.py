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