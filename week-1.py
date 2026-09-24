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

def calculate_average(num1, num2):
    average = (num1 + num2) / 2 
    return average