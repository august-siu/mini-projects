# LEAP YEAR CHECK
#notice how all are true to be nested but in above BMI, elif are each not true statements
year = int(input("What year do you wish to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
          print("Leap year")
        else:
          print("Not leap year")
    else:
      print("Leap year")
else:
  print("Not leap year")