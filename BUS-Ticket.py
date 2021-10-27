
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