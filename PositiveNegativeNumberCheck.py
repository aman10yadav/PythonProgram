# Program to check whether number is positive, negative or zero
inputNumber = float(input("Enter a number to check for positive, negative or zero : "))

# Check number is greater than 0
if inputNumber > 0 :
    print(f"The number '{inputNumber}' is Positive !!")
# Check number is eqaul to 0
elif inputNumber == 0 :
    print(f"The number '{inputNumber}' is Zero !!")
# Else check number is negative
else :
    print(f"The number '{inputNumber}' is Negative !!")

