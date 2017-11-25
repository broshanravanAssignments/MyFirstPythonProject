
def ConvertCelsiusToFarenhite(celsiusIn):
    fahrenheit = celsiusIn * 9/5 + 32
    return fahrenheit

celsius = input("Please enter the Temprature in celsus: \n")

temp = float(celsius)

if(temp < -273.15):
    print("This temprature is not physically possible")
else:
    fahrenheit = ConvertCelsiusToFarenhite(temp)
    print(str(celsius) + " degrees celsius is equal to: \n" + str(fahrenheit) + " degrees fahrenheit")