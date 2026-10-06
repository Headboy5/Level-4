def convertFeetAndInchesToInches(heightFeet, heightInches):
    return (heightFeet * 12) + heightInches


def main():
    firstHeightFeet = int(input("Person 1 feet: "))
    firstHeightInches = int(input("Person 1 inches: "))
    secondHeightFeet = int(input("Person 2 feet: "))
    secondHeightInches = int(input("Person 2 inches: "))
    thirdHeightFeet = int(input("Person 3 feet: "))
    thirdHeightInches = int(input("Person 3 inches: "))

    firstHeightTotalInches = convertFeetAndInchesToInches(
        firstHeightFeet, firstHeightInches
    )
    secondHeightTotalInches = convertFeetAndInchesToInches(
        secondHeightFeet, secondHeightInches
    )
    thirdHeightTotalInches = convertFeetAndInchesToInches(
        thirdHeightFeet, thirdHeightInches
    )

    averageHeightInches = (
        firstHeightTotalInches
        + secondHeightTotalInches
        + thirdHeightTotalInches
    ) / 3
    print(f"Average height: {averageHeightInches:.2f} inches")


if __name__ == "__main__":
    main()