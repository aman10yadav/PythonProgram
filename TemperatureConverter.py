print("Temperature Converter...")
print("Enter '1' to convert Celsius into Fahrenheit")
print("Enter '2' to convert Celsius to kelvin")
print("Enter '3' to convert Fahrenheit to Celsius")
print("Enter '4' to convert Fahrenheit to Kelvin")
print("Enter '5' to convert Kelvin to Celsius")
print("Enter '6' to convert Celsius to Kelvin")
choice = int(input("Enter your choice : "))

def getTemperatureInput(degree, convertedDegree) :
    temperature = float(input(f"Enter the amount of temperature(in {degree}) you want to convert(in {convertedDegree}) : "))
    return temperature

match choice:
    # Celsius to Fahrenheit conversion
    case 1:
        celsius = getTemperatureInput("C", "F")
        # F = ( (c) * (9/5) ) + 32
        fahrenheit = (celsius * (9/5)) + 32
        print(f"The converted temperature of {celsius}C to fahrenheit is {fahrenheit}F")

    # Celsius to Kelvin conversion
    case 2:
        celsius = getTemperatureInput("C", "K")
        # K = C + 273.15
        kelvin = celsius + 273.15
        print(f"The converted temperature of {celsius}C to kelvin is {kelvin}K")

    # Fahrenheit to Celsius conversion
    case 3:
        fahrenheit = getTemperatureInput("F", "C")
        # C = (9/5) * (F - 32)
        celsius = ( (9/5) * (fahrenheit - 32))
        print(f"The converted temperature of {fahrenheit}F to celcius is {celsius}C")

    # Fahrenheit to Celsius conversion
    case 4:
        fahrenheit = getTemperatureInput("F", "K")
        # C = ( (9/5) * (F - 32) ) + 273.15
        kelvin = ((9/5) * (fahrenheit - 32)) + 273.15
        print(f"The converted temperature of {fahrenheit}F to celcius is {kelvin}K")

    # Kelvin to Celsius conversion
    case 5:
            kelvin = getTemperatureInput("K", "C")
            # K = C + 273.15
            celsius = kelvin - 273.15
            print(f"The converted temperature of {kelvin}K to Celsius is {celsius}C")

    # Celsius to Kelvin conversion
    case 6:
            celsius = getTemperatureInput("C", "K")
            # K = C + 273.15
            kelvin = celsius + 273.15
            print(f"The converted temperature of {celsius}C to Celsius is {kelvin}K")

    case _ :
        print("Invalid choice")