# Worksheet Answers

## Practical Activity Questions

### Python Syntax Workshop

**Question 1:** What does the Hello Python program display?

**Answer:** The program displays `Hello, World!` and `I am learning Python
programming.` See [python_syntax_fundamentals.py](python_syntax_fundamentals.py).

**Question 2:** Which of the listed variable names are valid Python
identifiers?

**Answer:** `studentName`, `student1`, `_studentName`, `studentAge`, and
`courseName` are valid. See [Identifier Practice](#identifier-practice).

**Question 3:** Why are `studentName` and `StudentName` different variables?

**Answer:** Python is case-sensitive, so uppercase and lowercase names differ.

**Question 4:** Create strings, comments, and a newline escape sequence in
Python.

**Answer:** This is implemented in `activityThree()` in
[python_syntax_fundamentals.py](python_syntax_fundamentals.py).

**Question 5:** Write a program that displays a student's name, course, and
level.

**Answer:** This is implemented in `activityFour()` in
[python_syntax_fundamentals.py](python_syntax_fundamentals.py).

**Question 6:** How can a program accept the student's name, course, and city?

**Answer:** Use `input()` for each value, as implemented in `activityFour()`.

**Question 7:** How can an `if`, `elif`, and `else` structure classify a test
score?

**Answer:** Use the `classifyScore()` function in
[python_syntax_fundamentals.py](python_syntax_fundamentals.py).

**Question 8:** Correct the indentation, missing colon, invalid variable name,
and old `print` syntax in the debugging examples.

**Answer:** The corrected programs are shown in
[Debugging Corrections](#debugging-corrections).

**Question 9:** Create a Student Welcome Program that displays the student's
details, classifies age, and grades a Python test score.

**Answer:** This is implemented in `miniProject()` in
[python_syntax_fundamentals.py](python_syntax_fundamentals.py).

### Variables, Operators, and Conditions

**Question 1:** Which variable declarations are good, poor, or invalid?

**Answer:** The classifications are listed in
[Variable Declaration Classification](#variable-declaration-classification).

**Question 2:** How can an item price, 20% tax, and quantity be used to
calculate a total?

**Answer:** Run the variables-and-operators option in
[com4013_week_2.py](com4013_week_2.py).

**Question 3:** How can a birth year be checked for a leap year?

**Answer:** Use `isLeapYear()` in [com4013_week_2.py](com4013_week_2.py).

**Question 4:** How can two birth years be compared to report older, younger,
or the same?

**Answer:** Run the conditions option in
[com4013_week_2.py](com4013_week_2.py).

**Question 5:** Why should `1.0 / 2.0` be used when demonstrating a
floating-point result?

**Answer:** The decimal operands make the intended floating-point calculation
clear, producing `0.5` and a `float` result.

**Question 6:** How can Celsius be converted to Fahrenheit?

**Answer:** Use `Celsius * (9 / 5) + 32` in the temperature option.

**Question 7:** How can an amount be converted between GBP and USD in either
direction?

**Answer:** Select the currency option and use an exchange rate; multiply from
GBP to USD and divide from USD to GBP.

**Question 8:** How can the maximum of five integers be found using
comparisons?

**Answer:** Compare each number with the current maximum in the maximum-number
option.

**Question 9:** How can five integers be sorted using comparison and swap
statements?

**Answer:** Compare each later value with the earlier positions and swap when a
smaller value is found, as implemented in the sorting option.

## Identifier Practice

### Question

Determine which of these are valid Python identifiers:
`studentName`, `student1`, `_studentName`, `1student`, `student-name`,
`class`, `studentAge`, and `courseName`.

### Answer

Valid identifiers:

- `studentName`
- `student1`
- `_studentName`
- `studentAge`
- `courseName`

Invalid identifiers:

- `1student` starts with a digit.
- `student-name` contains a hyphen.
- `class` is a Python keyword.

`studentName` and `StudentName` are different because Python is
case-sensitive.

## Variable Declaration Classification

### Question

Classify each declaration as good, poor, or invalid:
`numberStudents`, `wall_length`, `wall`, `totalCash = 210.50`,
`num = 45.5`, `height = 3.14159`, `myID = "G1423"`, `AccountBalance`,
`myName = "Bob"`, `firstLetter = 'A'`, `1stPlaceScore`, and
`secondLetter = "B"`.

### Answer

| Declaration | Classification | Reason |
| --- | --- | --- |
| `numberStudents` | Poor | Valid, but not descriptive without a value or context. |
| `wall_length` | Good | Valid and descriptive. |
| `wall` | Poor | Valid, but vague. |
| `totalCash = 210.50` | Good | Valid and descriptive. |
| `num = 45.5` | Poor | Valid, but abbreviated and vague. |
| `height = 3.14159` | Good | Valid and descriptive. |
| `myID = "G1423"` | Good | Valid and meaningful. |
| `AccountBalance` | Poor | Valid, but class-style capitalization is less suitable for a variable. |
| `myName = "Bob"` | Good | Valid and descriptive. |
| `firstLetter = 'A'` | Good | Valid and descriptive. |
| `1stPlaceScore` | Invalid | An identifier cannot begin with a digit. |
| `secondLetter = "B"` | Good | Valid and descriptive. |

## Debugging Corrections

### Question

Correct these programs so that they run without errors:

```python
studentName = input("Enter your name: ")

if studentName:
print("Hello", studentName)
else
    print("No name entered")
```

```python
student-name = "Sam"
print student-name
```

### Answer

```python
studentName = input("Enter your name: ")

if studentName:
    print("Hello", studentName)
else:
    print("No name entered")
```

```python
studentName = "Sam"
print(studentName)
```

The first broken example has incorrect indentation and a missing colon after
`else`. The second has an invalid hyphenated variable name and Python 2 print
syntax.

## Knowledge Check

**Question 1:** Why is indentation important in Python?

**Answer:** Indentation defines which statements belong to a code block.

**Question 2:** What is camelCase?

**Answer:** camelCase starts with a lowercase word and capitalises each later
word, without spaces.

**Question 3:** Give two examples of meaningful camelCase variable names.

**Answer:** `studentScore` and `favouriteLanguage` are examples.

**Question 4:** Why is `studentScore` better than `x`?

**Answer:** `studentScore` explains what the value represents, while `x` does
not.

**Question 5:** What symbol begins a Python comment?

**Answer:** A Python comment begins with `#`.

**Question 6:** What is the purpose of `input()`?

**Answer:** `input()` reads text entered by the user and returns it as a string.

## Syntax Review

**Question 1:** What is Python syntax?

**Answer:** Python syntax is the set of rules for writing valid Python
programs.

**Question 2:** What extension is normally used for Python source-code files?

**Answer:** Python source files normally use the `.py` extension.

**Question 3:** What is an identifier?

**Answer:** An identifier is a name used for a variable, function, class,
module, or another Python object.

**Question 4:** Give three examples of valid Python identifiers.

**Answer:** `studentName`, `student1`, and `_total` are valid examples.

**Question 5:** Why cannot `class` be used as a normal variable name?

**Answer:** `class` is reserved as a Python keyword.

**Question 6:** Is Python case-sensitive?

**Answer:** Yes. Python is case-sensitive.

**Question 7:** Why is indentation important?

**Answer:** Indentation defines suites and code blocks.

**Question 8:** What character begins a Python comment?

**Answer:** Comments begin with `#`.

**Question 9:** What is the difference between single and triple quotation
marks?

**Answer:** Single and double quotes create one-line strings; triple quotes can
span multiple lines.

**Question 10:** What does `\n` represent?

**Answer:** `\n` represents a newline.

**Question 11:** What function receives user input?

**Answer:** Use `input()` to receive user input.

**Question 12:** What is the purpose of a colon in an `if` statement?

**Answer:** The colon starts the indented suite belonging to an `if`
statement.

**Question 13:** Why are blank lines useful?

**Answer:** Blank lines separate sections and improve readability.

**Question 14:** What command displays Python command-line help?

**Answer:** `python3 -h` displays Python command-line help.