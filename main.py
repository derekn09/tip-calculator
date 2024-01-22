#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print ("Welcome to the Derek's tip calculator!")

bill = float(input("What is the bill? $"))
people = int(input("How many people to split bill? "))
tip_percentage = float(input("What is the tip? 15, 18, 20? "))
total_bill = (tip_percentage /100) * bill + bill
bill_per_person = round(total_bill / people, 2)


print(f"The bill per person is ${bill_per_person}.")