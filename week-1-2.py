from pathlib import Path
import subprocess
import sys


programs = {
	"1": ("Say Hello", "week-1-2-1.py"),
	"2": ("Shout My Name", "week-1-2-2.py"),
	"3": ("Count the Characters", "week-1-2-3.py"),
	"4": ("Average Height", "week-1-2-4.py"),
	"5": ("Convert the Average to Inches", "week-1-2-5.py"),
	"6": ("Convert the Height to Feet and Inches", "week-1-2-6.py"),
	"7": ("Enter Heights in Feet and Inches", "week-1-2-7.py"),
	"8": ("Complete Height Program", "week-1-2-8.py"),
}


def displayMenu():
	print("\nWeek 1-2 Programs")
	print("=================")
	for choice, (programName, _) in programs.items():
		print(f"{choice}. {programName}")
	print("Q. Quit")


def launchProgram(programFileName):
	programPath = Path(__file__).parent / "week-1-2" / programFileName
	subprocess.run([sys.executable, str(programPath)], check=False)


def main():
	while True:
		displayMenu()
		selectedChoice = input("Choose a program: ").strip().lower()

		if selectedChoice == "q":
			print("Goodbye!")
			break

		selectedProgram = programs.get(selectedChoice)
		if selectedProgram is None:
			print("Please choose a number from 1 to 8, or Q to quit.")
			continue

		launchProgram(selectedProgram[1])
		input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
	main()
