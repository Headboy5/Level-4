import statistics as stats
def static_print():
    #Create an algorith of how I got into LTU this morning
    print("Leave the house\nWalk to the train station\nWait for the train\nBoard the train\nRide the train to LTU\nExit the train\nExit the train station\nWalk to LTU\nArrive at LTU")
    #Make python introduce you
    print("Hello, my name is Yea Nah")
    #Two truths and a lie
    print("I have missed a flight")
    print("I know a world famous author")
    print("I have been to Madrid")
    #Build your student profile
    name = "Yea Nah"
    age = 19
    course = "Computer Science"
    favourite_number = 64
    new_student = False
    print(f"My name is {name}, I am {age} years old, I am studying {course}, my favourite number is {favourite_number}, and it is {new_student} that I am a new student.")
    # Guess the data type
    # studentName = "Alex" - Sting
    # studentAge = 19 - Int
    # averageScore = 72.5 - Float
    # isRegistered = True - Bool

def input_print():
    # Ask your partner for their name, age, and favourite number. Then print out a statement about them using f-strings.
    partner_name = input("What is your name? ")
    partner_age = input("What is your age? ")
    partner_favourite_number = input("What is your favourite number? ")
    print(f"Your name is {partner_name}, you are {partner_age} years old, and your favourite number is {partner_favourite_number}.")

def predict_score():
    # Predict what will happen:
    studentScore = 75
    prediction = input("Prediction: 'pass' or 'fail': ")
    if studentScore >= 60:
        print("Challenge completed!")
        if prediction == "pass":
            print("You predicted correctly!")
        else:
            print("You predicted incorrectly!")
    else:
        print("Try again!")
        if prediction == "fail":
            print("You predicted correctly!")
        else:
            print("You predicted incorrectly!")

def mood_checker():
    mood = input("How are you feeling today? ")
    if mood == "happy":
        print("Wonderous.")
    elif mood == "tired":
        print("Python will abosolutely not wake you up.")
    elif mood == "sad":
        print("Same.")
    else:
        print("Have a great Welcome Day!")

def example_function():
    print("Welcome to python!")

def personalised_greeting(name):
    print(f"Hello, {name}! Welcome to Python programming!")

def calculate_average_score(num1, num2):
    average = stats.mean([num1, num2])
    return average

# Your job is to identify what type of function they are looking at.
# Mystery Function 1
# print("Hello")
# This is a procedure because it doesn't return a value.

# Mystery Function 2
def displayMessage():
    print("Welcome!")
# This is a procedure because it doesn't return a value.

# Mystery Function 3
def greetStudent(studentName):
    print("Hello", studentName)
# This is a procedure because it doesn't return a value.

# Mystery Function 4
def calculateSquare(number):
    squaredNumber = number * number
    return squaredNumber
# This is a function because it returns a value.

# What does this return?
def double():
    def calculateDouble(number):
        return number * 2
    print(calculateDouble(6))
# 12

def test_list():
    welcomeActivities = [
    "Campus Tour",
    "Meet Your Tutor",
    "Library Visit",
    "Python Challenge"
    ]
    print(welcomeActivities[0]) # Output: Campus Tour
    welcomeActivities.append("Free Pizza") # Add a new activity to the list
    for activity in welcomeActivities:
        print(activity)

def test_tuple():
    classroomLocation = ("Computing Building", "Room 101")
    print(classroomLocation[0]) # Output: Computing Building
    print(classroomLocation[1]) # Output: Room 101

def test_duplicate():
    studentNumbers = {101, 102, 102, 103, 103, 103}
    # How many numbers do you think Python will display?
    # Answer: 3 (sets only store unique values)
    print(studentNumbers)

def identity_card():
    studentDetails = {
    "name": "Maya",
    "studentId": 1024,
    "course": "Computing",
    "year": 1
    }
    print(studentDetails["course"]) # Output: Computing
    studentDetails["favouriteLanguage"] = "Python" # Add a new key-value pair to the dictionary
    print(studentDetails)

def welcome_day_generator():
    studentName = input("Enter your name: ")
    studentAge = input("Enter your age: ")
    favouriteActivity = input("Enter your favourite activity: ")
    surpriseQuestion = input("Would you like a surprise welcome challenge? (yes/no): ")

    def greet(studentName):
        print(f"Hello, {studentName}! Welcome to Python programming!")

    def personalised_message(studentName, studentAge):
        print(f"{studentName}, at {studentAge} years old, you are officially ready to start your amazing LTU journey!")

    def activity_decision(favouriteActivity):
        if favouriteActivity == "games":
            print("Try the Games Society!")
        elif favouriteActivity == "coding":
            print("Join the Coding Club!")
        elif favouriteActivity == "sports":
            print("Visit the Sports Centre!")
        elif favouriteActivity == "music":
            print("Head to the Music Lounge!")
        else:
            print("Explore the Welcome Fair!")

    def funny_response(surpriseQuestion):
        if surpriseQuestion.lower() == "yes":
            print("Consume the flesh of the innocent.") # FOR LEGAL REASONS THIS IS A JOKE
        else:
            print("Perish in the void of despair.")

    greet(studentName)
    personalised_message(studentName, studentAge)
    activity_decision(favouriteActivity)
    funny_response(surpriseQuestion)

    studentProfile = {
        "name": studentName,
        "age": studentAge,
        "favourite_activity": favouriteActivity,
        "course": "Computer Science",
        "welcome_status": "Ready to learn"
    }
    print("Student information:")
    print(studentProfile)

    welcomeActivities = [
    "Campus Tour",
    "Coding Club",
    "Games Society",
    "Sports Centre",
    "Music Lounge"
    ]
    print("Today's activities:")
    for activityName in welcomeActivities:
        print(activityName)



def main():
    static_print()
    input_print()
    predict_score()
    mood_checker()
    example_function()
    personalised_greeting("Yea Nah")
    avg = calculate_average_score(10, 20)
    print(f"The average score is {avg}.")
    double()
    test_list()
    test_tuple()
    test_duplicate()
    identity_card()
    welcome_day_generator()
if __name__ == "__main__":
    main()
