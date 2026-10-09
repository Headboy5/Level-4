"""COM4013 Software Development, Week 2 exercise runner.

Source document: COM4013 Software Development, Week 2 - Variables, Operators
and Conditions, pages 1-4.

Choose an exercise from the menu. This file requires Python 3.10 or newer
because the menu uses match case.
"""


# Question: Which variable declarations are good, poor, or invalid?
def variableDeclarations() -> None:
    declarations = [
        ("numberStudents", "Poor", "valid but vague"),
        ("wall_length", "Good", "valid and descriptive"),
        ("wall", "Poor", "valid but vague"),
        ("totalCash = 210.50", "Good", "valid and descriptive"),
        ("num = 45.5", "Poor", "valid but abbreviated"),
        ("height = 3.14159", "Good", "valid and descriptive"),
        ('myID = "G1423"', "Good", "valid and meaningful"),
        ("AccountBalance", "Poor", "valid but uses class-style capitalization"),
        ('myName = "Bob"', "Good", "valid and descriptive"),
        ("firstLetter = 'A'", "Good", "valid and descriptive"),
        ("1stPlaceScore", "Invalid", "identifiers cannot begin with a digit"),
        ('secondLetter = "B"', "Good", "valid and descriptive"),
    ]

    for declaration, classification, reason in declarations:
        print(f"{declaration}: {classification} ({reason})")


# Question: How can item price, 20% tax, quantity, and total cost be calculated?
def variablesAndOperators() -> None:
    itemPrice = float(input("Enter the item price: "))
    itemTax = itemPrice * 20 / 100
    totalPrice = itemPrice + itemTax
    numberOfItems = int(input("How many items do you want to buy? "))
    totalCost = totalPrice * numberOfItems

    print(f"Tax on the item is {itemTax:.2f}")
    print(f"Total item price is {totalPrice:.2f}")
    print(f"The price for {numberOfItems} items is {totalCost:.2f}")


# Question: How can a year be tested using the complete leap-year rules?
def isLeapYear(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Question: How can birth years be compared as the same, older, or younger?
def conditions() -> None:
    birthYear = int(input("Enter the year you were born: "))
    if isLeapYear(birthYear):
        print("You were born in a leap year")
    else:
        print("You were not born in a leap year")

    comparisonYear = int(input("Enter my comparison birth year: "))
    if birthYear == comparisonYear:
        print("You were born in the same year as me!")
    elif birthYear < comparisonYear:
        print("You're older than me")
    else:
        print("You're younger than me")


# Question: How can one half be calculated as a float and its type displayed?
def divisionTypes() -> None:
    half = 1.0 / 2.0
    print(f"One half (1/2) = {half}")
    print(type(half))


# Question: How can Celsius be converted to Fahrenheit using the given formula?
def temperatureConversion() -> None:
    celsius = float(input("Enter a temperature in Celsius: "))
    fahrenheit = celsius * (9 / 5) + 32
    print(f"{celsius:g}C = {fahrenheit:.2f}F")


# Question: How can an amount be converted in either currency direction?
def currencyConversion() -> None:
    conversionChoice = int(input("Type 1 for GBP to USD, or type 2 for USD to GBP: "))
    amount = float(input("Enter the amount: "))
    exchangeRate = float(input("Enter the exchange rate (USD per GBP): "))

    if conversionChoice == 1:
        convertedAmount = amount * exchangeRate
        print(f"GBP {amount:.2f} = USD {convertedAmount:.2f}")
    else:
        convertedAmount = amount / exchangeRate
        print(f"USD {amount:.2f} = GBP {convertedAmount:.2f}")


# Question: How can the maximum of five integers be found using comparisons?
def maximumNumber() -> None:
    numbers = [int(input(f"Enter integer {numberIndex}: ")) for numberIndex in range(1, 6)]
    maximumValue = numbers[0]
    if numbers[1] > maximumValue:
        maximumValue = numbers[1]
    if numbers[2] > maximumValue:
        maximumValue = numbers[2]
    if numbers[3] > maximumValue:
        maximumValue = numbers[3]
    if numbers[4] > maximumValue:
        maximumValue = numbers[4]
    print("The maximum number is", maximumValue)


# Question: How can five integers be sorted using only comparisons and swaps?
def sorting() -> None:
    numbers = [int(input(f"Enter integer {numberIndex}: ")) for numberIndex in range(1, 6)]

    if numbers[1] < numbers[0]:
        numbers[0], numbers[1] = numbers[1], numbers[0]
    if numbers[2] < numbers[0]:
        numbers[0], numbers[2] = numbers[2], numbers[0]
    if numbers[3] < numbers[0]:
        numbers[0], numbers[3] = numbers[3], numbers[0]
    if numbers[4] < numbers[0]:
        numbers[0], numbers[4] = numbers[4], numbers[0]
    if numbers[2] < numbers[1]:
        numbers[1], numbers[2] = numbers[2], numbers[1]
    if numbers[3] < numbers[1]:
        numbers[1], numbers[3] = numbers[3], numbers[1]
    if numbers[4] < numbers[1]:
        numbers[1], numbers[4] = numbers[4], numbers[1]
    if numbers[3] < numbers[2]:
        numbers[2], numbers[3] = numbers[3], numbers[2]
    if numbers[4] < numbers[2]:
        numbers[2], numbers[4] = numbers[4], numbers[2]
    if numbers[4] < numbers[3]:
        numbers[3], numbers[4] = numbers[4], numbers[3]

    print("Increasing order:", ", ".join(str(number) for number in numbers))


# Question: How can a user select one COM4013 Week 2 exercise to run?
def main() -> None:
    while True:
        print("\nCOM4013 Week 2 Exercises")
        print("1. Variable declarations")
        print("2. Variables and operators")
        print("3. Conditions")
        print("4. Division types")
        print("5. Temperature conversion")
        print("6. Currency conversion")
        print("7. Maximum number")
        print("8. Sorting")
        print("0. Exit")

        choice = input("Choose an exercise: ")
        match choice:
            case "1":
                variableDeclarations()
            case "2":
                variablesAndOperators()
            case "3":
                conditions()
            case "4":
                divisionTypes()
            case "5":
                temperatureConversion()
            case "6":
                currencyConversion()
            case "7":
                maximumNumber()
            case "8":
                sorting()
            case "0":
                print("Goodbye")
                break
            case _:
                print("Invalid choice. Select a number from 0 to 8.")


if __name__ == "__main__":
    main()