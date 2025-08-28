print("welcome to the pizza calculator")

size = input("Which size of pizza would you want? S, M, L:")
pepperoni = input("would you want pepperoni on your pizza? Y or N:")
extra_cheese = input(" do you want extra cheese ? Y or N")

bill = 0
if size == "S":
    bill += 50
elif size == "M":
    bill += 75
elif size == "L":
    bill += 100
else:
    print("we dont have such size of pizza")


if pepperoni == "Y":
    if size == "S":
        bill += 5
    elif size == "M":
        bill += 10
    elif size == "L":
        bill += 10


if extra_cheese == "Y":
    if size == "S":
        bill += 3
    elif size == "M":
        bill += 5
    elif size == "L":
        bill += 7

print(f"Your final bill is $ {bill}.")