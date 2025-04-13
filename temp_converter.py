# python temperature converter program
unit = input("Celsius or Farenheit? (C/F) : ")

temp = float(input("What is the temperature?"))

if unit ==  "C" :
    temp = round((temp * 1.8) + 32 , 0)
    print(f"The temperature is {temp} degrees farenheit.")
elif unit == "F" :
    temp = round((temp - 32) / 1.8, 0)
    print(f"The temperature is {temp} degrees celsius.")
else : 
    print("A suitable temperature scale was not sent, restart this program.")    