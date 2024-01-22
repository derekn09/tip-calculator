print ("Welcome to the Derek's tip calculator!")

bill = float(input("What is the bill? $"))
people = int(input("How many people to split bill? "))
tip_percentage = float(input("What is the tip? 15, 18, 20? "))
total_bill = (tip_percentage /100) * bill + bill
bill_per_person = round(total_bill / people, 2)


print(f"The bill per person is ${bill_per_person}.")
