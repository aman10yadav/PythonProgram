# A number is prime if it is only divisible by itself and 1
numberInput = int(input("Enter a number to check whether it is prime or not : "))

startingNumber = 2

# start checking from number 2 to the input number
while (startingNumber * startingNumber) <= numberInput:
    if numberInput % startingNumber == 0:
        print(f"The number '{numberInput}' is not a prime number !!")
        break
    startingNumber += 1
else :
    print(f"The number '{numberInput}' is a prime number !!")