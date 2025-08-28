print("welcome to the demo tip calculator on python !")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage would you want to tip? 10, 30, 50 "))
people = int(input("How many people are splitting the bill?"))
tip_as_percentage = tip/100
total_tip_amount = bill * tip_as_percentage
total_amount = bill + total_tip_amount
bill_per_person = total_amount / people
final_amount = round(bill_per_person, 2)
print("each person should contribute" + " " + "$" f"{final_amount}")
