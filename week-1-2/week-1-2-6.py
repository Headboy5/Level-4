def convertCmToInches(heightCm):
    return heightCm / 2.54


def convertInchesToFeetAndInches(heightInches):
    fullFeet = int(heightInches) // 12
    remainingInches = int(heightInches) % 12
    return fullFeet, remainingInches


def main():
    userHeightCm = float(input("Enter your height in centimetres: "))
    leftNeighbourHeightCm = float(input("Enter the height of the person on your left: "))
    rightNeighbourHeightCm = float(input("Enter the height of the person on your right: "))
    numberOfPeople = 3

    averageHeightCm = (
        userHeightCm + leftNeighbourHeightCm + rightNeighbourHeightCm
    ) / numberOfPeople
    averageHeightInches = convertCmToInches(averageHeightCm)
    fullFeet, remainingInches = convertInchesToFeetAndInches(averageHeightInches)

    print(f"Average height: {fullFeet} feet {remainingInches} inches")


if __name__ == "__main__":
    main()