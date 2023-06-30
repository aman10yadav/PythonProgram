print("Project to swap two numbers...")
choice = int(input("Choose '1' to use third variable for swapping\nChoose '2' for swapping without using third variables\n"))

match choice:
    # Using Third Variable
    case 1:
        firstVariable = input("Enter first variable : ")
        secondVariable = input("Enter second variable : ")

        tempVariable = firstVariable

        firstVariable = secondVariable
        secondVariable = tempVariable

        print("\nAfter swapping")
        print("Your first variable will be ==>", firstVariable)
        print("Your second variable will be ==>", secondVariable)

################################################################
    # Without using third variables
    case 2:
        firstVariable = input("Enter first variable : ")
        secondVariable = input("Enter second variable : ")

        # Swap
        firstVariable, secondVariable = secondVariable, firstVariable

        print("\nAfter swapping")
        print("Your first variable will be ==>", firstVariable)
        print("Your second variable will be ==>", secondVariable)

    case _ :
        print("Invalid choice")


