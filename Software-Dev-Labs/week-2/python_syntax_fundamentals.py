"""
Source documents:
- COM4103 Week 2 Workshop Worksheet.pdf
- COM4103 Week 2 Python Syntax.pdf
"""


# Question: What does a Python program display when it prints two messages?
def activityOne() -> None:
    print("Hello, World!")
    print("I am learning Python programming.")


# Question: How can meaningful variables be created and displayed?
def activityTwo() -> None:
    studentName = "Alex"
    studentAge = 20
    courseName = "Python Programming"

    print(studentName)
    print(studentAge)
    print(courseName)


# Question: How are strings, comments, and the newline escape character used?
def activityThree() -> None:
    programmingLanguage = "Python"
    courseDescription = "Python is a beginner-friendly programming language."
    courseInformation = """Python can be used for:
software development,
data analysis,
automation,
and many other tasks."""

    print(programmingLanguage)
    print(courseDescription)
    print(courseInformation)

    # Store and display the student's name.
    studentName = "Aisha"
    print(studentName)
    print("Python\nProgramming")


# Question: How can a program collect and display student details with input()?
def activityFour() -> None:
    studentName = input("Enter your name: ")
    courseName = input("Enter your course: ")
    studentCity = input("Enter your city: ")
    favouriteLanguage = input("Enter your favourite programming language: ")

    print("\nStudent Profile")
    print("Name:", studentName)
    print("Course:", courseName)
    print("City:", studentCity)
    print(studentName, "likes programming in", favouriteLanguage)


# Question: How should a score be classified as Excellent, Very Good, Pass, or Fail?
def classifyScore(studentScore: int) -> str:
    if studentScore >= 80:
        return "Excellent"
    if studentScore >= 70:
        return "Very Good"
    if studentScore >= 50:
        return "Pass"
    return "Fail"


# Question: How can age and score conditions be written with if, elif, and else?
def activityFive() -> None:
    studentAge = int(input("Enter your age: "))
    if studentAge >= 18:
        print("You are an adult student.")
    else:
        print("You are under 18.")

    studentScore = int(input("Enter your score: "))
    print(classifyScore(studentScore))


# Question: How can a Student Welcome Program display details and classifications?
def miniProject() -> None:
    studentName = input("Enter the student's name: ")
    courseName = input("Enter the course name: ")
    studentAge = int(input("Enter the student's age: "))
    favouriteLanguage = input("Enter the favourite programming language: ")
    studentScore = int(input("Enter the Python test score: "))

    print("\nStudent Profile")
    print("Name:", studentName)
    print("Course:", courseName)
    print("Age:", studentAge)
    print("Favourite language:", favouriteLanguage)
    print("Classification:", "Adult student" if studentAge >= 18 else "Young student")
    print("Score:", classifyScore(studentScore))
    print("Welcome to Python,", studentName + "!")


def main() -> None:
    choice = input("Which program would you like to run? (1-5 for activities, 6 for mini project): ")
    match choice:
        case "1":
            activityOne()
        case "2":
            activityTwo()
        case "3":
            activityThree()
        case "4":
            activityFour()
        case "5":
            activityFive()
        case "6":
            miniProject()
        case _:
            print("Invalid choice. Please select a number from 1 to 6.")

if __name__ == "__main__":
    main()