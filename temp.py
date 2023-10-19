#Step 1 - Convert Temperature from Celcius to Fahrenheit
#Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32.
#celcius = input ("Enter the temperature in celcius>>>") 
#celcius = int()
#print (f"The temeperature is {celcius} degrees celcius. That's {fahrenheit_calc} degrees in Fahrenheit!")

#Step 2 - Function to Convert Temperature from Celcius to Fahrenheit
tempselect = input("what temperature do you have right now? (F/C)>>>").lower()
if tempselect == "c":
    def celcius_to_fahrenheit():
        celcius = int(input ("Enter the temperature in celcius>>>"))
        fahrenheit_calc = celcius * 9 / 5 + 32
        print (f"The temeperature is {celcius} degrees celcius. That's {fahrenheit_calc} degrees in fahrenheit!")
    celcius_to_fahrenheit()
    #Step 3 - Do the same but in reverse
elif tempselect == "f":
    def fahrenheit_to_celcius():
        farenheit = int(input("Enter the temperature in fahrenheit>>>"))
        celcius_calc = farenheit - 32 * 5 / 9
        print (f"The temeperature is {farenheit} degrees fahrenheit. That's {celcius_calc} degrees in celcius!")
    fahrenheit_to_celcius()
else:
    print("Not a valid response. Please try again later")