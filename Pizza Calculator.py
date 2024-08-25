#PIZZA
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza would you like? S, M or L?")
bill = 0
if size == "S":
    bill = 15
    print("Small pizzas are $15.")
    add_pepperoni = input("Add pepperoni to small pizza? $2 Extra. Yes or No?")
    if add_pepperoni == "Yes":
        bill += 28
elif size == "M":
    bill = 20
    print("Medium pizzas are $20.")
    add_pepperoni = input("Add pepperoni to pizza? $3 Extra. Yes or No?")
    if add_pepperoni == "Yes":
      bill += 3
elif size == "L":
    bill = 25
    print("Large pizzas are $25.")
    add_pepperoni = input("Add pepperoni to pizza? $3 Extra. Yes or No?")
    if add_pepperoni == "Yes":
     bill += 3
extra_cheese = input("Add Cheese to Pizza? $1 Extra. Yes or No?")
if extra_cheese == "Yes":
    bill += 1
print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: ${bill}.")

