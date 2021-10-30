from Q5 import BookingTokenizer
from Q7 import RedundantTokenRemover
from Q8 import QueryTagger
from dateutil import parser
import re

class AutomatedBooker:
	def __init__(self):
		# We will store the data tokens in these lists
		self._dataElements = {
			"date": [],
			"time": [],
			"player": [],
			"name": []
		}

		# We may need to convert spelled out numbers to integers
		# Recall the assumption that a maximum of 99 players are allowed per booking
		self._numbers = {
			"one" : 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
			"seven" : 7, "eight" : 8, "nine" : 9, "ten" : 10, "eleven" : 11,
			"twelve" : 12, "thirteen" : 13, "fourteen" : 14, "fifteen" : 15,
			"sixteen" : 16, "seventeen" : 17, "eighteen" : 18, "nineteen" : 19,
			'twenty' : 20, 'twentyone' : 21, 'twentytwo' : 22, 'twentythree' : 23,
			'twentyfour' : 24, 'twentyfive' : 25, 'twentysix' : 26, 'twentyseven' : 27,
			'twentyeight' : 28, 'twentynine' : 29, 'thirty' : 30, 'thirtyone' : 31,
			'thirtytwo' : 32, 'thirtythree' : 33, 'thirtyfour' : 34, 'thirtyfive' : 35,
			'thirtysix' : 36, 'thirtyseven' : 37, 'thirtyeight' : 38, 'thirtynine' : 39,
			'fourty' : 40, 'fourtyone' : 41, 'fourtytwo' : 42, 'fourtythree' : 43,
			'fourtyfour' : 44, 'fourtyfive' : 45, 'fourtysix' : 46, 'fourtyseven' : 47,
			'fourtyeight' : 48, 'fourtynine' : 49, 'fifty' : 50, 'fiftyone' : 51,
			'fiftytwo' : 52, 'fiftythree' : 53, 'fiftyfour' : 54, 'fiftyfive' : 55,
			'fiftysix' : 56, 'fiftyseven' : 57, 'fiftyeight' : 58, 'fiftynine' : 59,
			'sixty' : 60, 'sixtyone' : 61, 'sixtytwo' : 62, 'sixtythree' : 63,
			'sixtyfour' : 64, 'sixtyfive' : 65, 'sixtysix' : 66, 'sixtyseven' : 67,
			'sixtyeight' : 68, 'sixtynine' : 69, 'seventy' : 70, 'seventyone' : 71,
			'seventytwo' : 72, 'seventythree' : 73, 'seventyfour' : 74,
			'seventyfive' : 75, 'seventysix' : 76, 'seventyseven' : 77,
			'seventyeight' : 78, 'seventynine' : 79, 'eighty' : 80,
			'eightyone' : 81, 'eightytwo' : 82, 'eightythree' : 83, 'eightyfour' : 84,
			'eightyfive' : 85, 'eightysix' : 86, 'eightyseven' : 87,
			'eightyeight' : 88, 'eightynine' : 89, 'ninety' : 90, 'ninetyone' : 91,
			'ninetytwo' : 92, 'ninetythree' : 93, 'ninetyfour' : 94,
			'ninetyfive' : 95, 'ninetysix' : 96, 'ninetyseven' : 97,
			'ninetyeight' : 98,  'ninetynine' : 99
		}

	def MakeBooking(self):
		# First, let's get the user's query
		query = input("Please enter the booking information: \nRemember to provide: \n- A name\n- A date\n- A time\n- And the number of players \n")

		# Next, we tokenise it
		tokenizer = BookingTokenizer(query)
		queryTokens = tokenizer.Tokenize()

		# Then, we remove all redundant tokens
		remover = RedundantTokenRemover(queryTokens)
		reducedTokens = remover.RemoveRedundantTokens()

		# Now we tag the reduced token set
		tagger = QueryTagger(reducedTokens)
		taggedTokens = tagger.Tag()

		# Next, we extract the data
		for token in taggedTokens:
			for pattern in self._dataElements:
				match = re.search(f"(.*)/{pattern}\d?", token)
				if match is not None:
					self._dataElements[pattern].append(match.group(1))

		# Test for missing information
		for pattern in self._dataElements:
			if len(self._dataElements[pattern]) == 0:
				if pattern == "player":
					print("Error: Please provide the number of players.")
				else:
					print(f"Error: Please provide a {pattern}.")
				return
		
		# We can now convert the extracted data into proper objects
		# Start with the date and time
		try:
			# Replace '.' with ':'
			timeString = re.sub("\.", ':', ' '.join(self._dataElements['time']))

			# Also change 'morning' and 'afternoon' to 'am' and 'pm' respectively
			timeString = re.sub("(?i)morning", "am", timeString)
			timeString = re.sub("(?i)afternoon", "pm", timeString)

			# Change 'noon' and 'midday' to '12:00'
			timeString = re.sub("(?i)noon|midday", "12:00", timeString)

			# Change 'midnight' to '00:00'
			timeString = re.sub("(?i)midnight", "00:00", timeString)
			bookingDateTime = parser.parse(f"{' '.join(self._dataElements['date'])} {timeString}")
		except:
			print("Error: Please enter a valid date and time.")
			return

		# Then attempt to convert the number of players to an integer
		try:
			numberOfPlayersString = self._dataElements["player"][0]
			if numberOfPlayersString.isnumeric():
				numberOfPlayers = int(numberOfPlayersString)
			else:
				numberOfPlayers = self._numbers[numberOfPlayersString.lower()]
		except:
			print("Error: Please enter a valid number of players")
			return

		# The name doesn't need error checking
		bookingName = " ".join(self._dataElements["name"])

		print()
		print("Your booking information is as follows:")
		print(f"Date: {bookingDateTime.date()}")
		print(f"Time: {bookingDateTime.time()}")
		print(f"Number of players: {numberOfPlayers}")
		print(f"Name: {bookingName}")

def main():
	print("------------------------------------------")
	print("This program implements automated bookings")
	print("------------------------------------------\n")

	# Initialize the booker
	booker = AutomatedBooker()
	booker.MakeBooking()

	# Wait for input to continue
	input("\nPress <RETURN> to continue")

if __name__ == "__main__":
	print("\n=============================================")
	print("62760858 - COS4861 - Assignment 4 - 2021 - Q9")
	print("=============================================\n")
	main()