unit = input("Is this  temperature in Celcius or Fahrenheit(C/F): ")
temp = float(input("Enter the temperature: "))

if unit =="C":
    temp = round((9*temp)/ 5+32,1)
    print(f"the Temperature in fahreheit is {temp}F")
elif unit =="F":
    temp = round((temp-32) *5 / 9,1)
    print(f"the temperture in Celcius is: {temp}C")
else:
    print(f"{unit} is an invalid  unit of measurement")

    
