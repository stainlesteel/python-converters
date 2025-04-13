# this program is supposed to calculate ibs to kg, or kg to ibs
selec = input("Select 1 to calculate pounds to kilograms, select 2 to calculate kilograms to pounds. ")
weight = float(input("Enter your weight : "))

if selec == "1" :
    result = round(weight * 0.45359, 1)
    print(f"The result is {result} kg")
elif selec == "2" :
    result = round(weight * 2.204623, 1)
    print(f"The result is {result} ibs")
else :
    print("1 or 2 wasn't selected, restart this program.")    