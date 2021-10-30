import Q5
import Q6
import Q7
import Q8
import Q9

options = ["Question 5 (Q5)", "Question 6 (Q6)", "Question 7 (Q7)", "Question 8 (Q8)", "Question 9 (Q9)", "Exit"]

while True:
	print("\n========================================")
	print("62760858 - COS4861 - Assignment 4 - 2021")
	print("========================================\n")
	print("Please enter the question you wish to run: (e.g. Q9)")
	for option in options:
		print(">> " + option)
	questionNumber = input(":: ").upper()
	print()

	if questionNumber == "EXIT":
		break
	elif questionNumber == "Q5":
		Q5.main()
	elif questionNumber == "Q6":
		Q6.main()
	elif questionNumber == "Q7":
		Q7.main()
	elif questionNumber == "Q8":
		Q8.main()
	elif questionNumber == "Q9":
		Q9.main()
	else:
		print("Error: Invalid input")