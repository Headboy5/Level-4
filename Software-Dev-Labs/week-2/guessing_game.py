import random

def play_single_round() -> int:
	random_number = random.randint(1, 100)
	attempts = 0
	max_attempts = 10
	guess = None

	print(f"Guess the number from 1 to 100. You have {max_attempts} attempts.")

	while guess != random_number and attempts < max_attempts:
		try:
			guess = int(input("Enter your guess: "))
		except ValueError:
			print("Please enter a valid whole number.")
			continue

		attempts += 1

		if guess < random_number:
			print("Too low!")
		elif guess > random_number:
			print("Too high!")
		else:
			print(f"Correct! You guessed the number in {attempts} attempts.")
			return attempts

		print(f"Remaining attempts: {max_attempts - attempts}")

	print(f"Game over. The correct number was {random_number}.")
	return max_attempts

def play_game() -> None:
	total_rounds = 3
	total_score = 0

	print("Welcome to the Guessing Game!")

	for round_number in range(1, total_rounds + 1):
		print(f"\nRound {round_number} of {total_rounds}")
		score = play_single_round()
		total_score += score

	print("\nGame over!")
	print(f"Your total score is {total_score} attempts.")

	excellent_score = 7 * total_rounds
	good_score = 9 * total_rounds
	if total_score <= excellent_score:
		print("Excellent guessing skills!")
	elif total_score <= good_score:
		print("Good job!")
	else:
		print("Better luck next time!")


if __name__ == "__main__":
	play_game()
