def main():
    userHeightCm = float(input("Enter your height in centimetres: "))
    leftNeighbourHeightCm = float(input("Enter the height of the person on your left: "))
    rightNeighbourHeightCm = float(input("Enter the height of the person on your right: "))
    numberOfPeople = 3

    averageHeightCm = (
        userHeightCm + leftNeighbourHeightCm + rightNeighbourHeightCm
    ) / numberOfPeople
    print(f"Average height: {averageHeightCm:.2f} cm")


if __name__ == "__main__":
    main()