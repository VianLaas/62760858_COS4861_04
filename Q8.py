from Q5 import BookingTokenizer
from Q7 import RedundantTokenRemover
import re

class QueryTagger():
	def __init__(self, queries = []):
		# Declare our Regular Expressions to extract dates, times, and the numbers of players
		# (note the case insensitivity: (?i))
		self._datePattern = "(?i)(\d{1,2}\s+(January|February|March|April|May|June|July|August|September|October|November|December)(\s+\d{4})?)|\d{4}[\\/\-\.:_]\d{2}[\\/\-\.:_]\d{2}|\d{2}[\\/\-\.:_]\d{2}[\\/\-\.:_]\d{4}"
		self._timePattern = "(?i)\\b([0-9]|[0-1][0-9]|[2][0-3])[\.:h]([0-5][0-9])([\.:]([0-5][0-9]))?(\s+[ap]m)?|\\b(noon|midnight|midday)\\b|\\b([0-9]|[01][0-2])\s+(morning|afternoon)\\b"
		self._playersPattern = "(?i)((one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|eighteen|nineteen)|(twenty|thirty|fourty|fifty|sixty|seventy|eighty|ninety)\-?(one|two|three|four|five|six|seven|eight|nine)?|([1-9]\d*))\s+players?"

		# The tagged query will be stored in this list
		self._bookingInformation = []

		# Combine the words in queries into a string separated by spaces
		self._queries = " ".join(queries)

	def Tag(self):
		# Extract the date
		try:
			date = re.search(self._datePattern, self._queries).group()
		except AttributeError:
			date = ""

		# Remove the extracted date from the input
		self._queries = self._queries.replace(date, "")

		# Split the date on whitespace
		date = date.split()

		if len(date) == 1:
			self._bookingInformation.append(f"{date[0]}/date")
		else:
			i = 1
			for w in date:
				self._bookingInformation.append(f"{w}/date{i}")
				i += 1

		# Extract the time
		try:
			time = re.search(self._timePattern, self._queries).group()
		except AttributeError:
			time = ""

		# Remove the extracted time from the input
		self._queries = self._queries.replace(time, "")

		# Split the time on whitespace
		time = time.split()

		if len(time) == 1:
			self._bookingInformation.append(f"{time[0]}/time")
		else:
			i = 1
			for w in time:
				self._bookingInformation.append(f"{w}/time{i}")
				i += 1
		
		# Extract the number of players
		try:
			players = re.search(self._playersPattern, self._queries).group()
		except AttributeError:
			players = ""

		# Remove the extracted number of players from the input
		self._queries = self._queries.replace(players, "")

		# Split the number of players on whitespace
		players = players.split()

		i = 1
		for w in players:
			self._bookingInformation.append(f"{w}/player{i}")
			i += 1

		name = self._queries.strip().split()

		i = 1
		for w in name:
			self._bookingInformation.append(f"{w}/name{i}")
			i += 1

		return self._bookingInformation

def main():
	print("----------------------------------")
	print("This program tags words in a query")
	print("----------------------------------\n")

	query = input("Please enter the booking information: \n")

	# Initialize the tokenizer
	tokenizer = BookingTokenizer(query)

	# Tokenize the contents of the query
	words = tokenizer.Tokenize()

	# Initialize the redundancy remover
	remover = RedundantTokenRemover(words)

	# Remove the redundant tokens
	words = remover.RemoveRedundantTokens()

	# Initialise the tagger
	tagger = QueryTagger(words)

	words = tagger.Tag()

	# Print each word on a new line
	print("\nThe tagged words are:\n")
	for word in words:
		print(word)

	# Wait for input to continue
	input("\nPress <RETURN> to continue")

if __name__ == "__main__":
	print("\n=============================================")
	print("62760858 - COS4861 - Assignment 4 - 2021 - Q7")
	print("=============================================\n")
	main()