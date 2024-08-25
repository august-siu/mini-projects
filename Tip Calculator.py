print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give?"))
party = int(input("How many people to split the bill?"))
bill_with_tip = tip/100 * bill + bill
split = bill_with_tip/party
amount = round(split,2)
amount = "{:.2f}".format(split)
#the above is from google to convert ex of $2.2 to $2.20
print(f"Each person should pay ${amount}.")