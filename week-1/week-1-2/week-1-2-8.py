def getHeightInCentimetres(personNumber):
    return float(input(f"Enter height for person {personNumber} in centimetres: "))


def calculateAverageHeight(heightsCm):
    return sum(heightsCm) / len(heightsCm)


def convertCmToInches(heightCm):
    return heightCm / 2.54


def convertInchesToFeetAndInches(heightInches):
    fullFeet = int(heightInches) // 12
    remainingInches = int(heightInches) % 12
    return fullFeet, remainingInches


def main():
    heightsCm = [
        getHeightInCentimetres(1),
        getHeightInCentimetres(2),
        getHeightInCentimetres(3),
    ]
    averageHeightCm = calculateAverageHeight(heightsCm)
    averageHeightInches = convertCmToInches(averageHeightCm)
    fullFeet, remainingInches = convertInchesToFeetAndInches(averageHeightInches)

    print(f"Average height: {averageHeightCm:.2f} cm")
    print(f"Average height: {averageHeightInches:.2f} inches")
    print(f"Average height: {fullFeet} feet {remainingInches} inches")


if __name__ == "__main__":
    main()