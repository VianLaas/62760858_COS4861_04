import re

class BookingTokenizer():
	def __init__(self, query = "", sourceFileName = 'queries.txt'):
		# The tokenized source file will be stored in a list
		# containing separated words
		self._words = []

		# Abbrevations are to be expanded
		self._abbreviations = {
			"(?i)jan\.?(?!\w)" : "January",
			"(?i)feb\.?(?!\w)" : "February",
			"(?i)mar\.?(?!\w)" : "March",
			"(?i)apr\.?(?!\w)" : "April",
			"(?i)jun\.?(?!\w)" : "June",
			"(?i)jul\.?(?!\w)" : "July",
			"(?i)aug\.?(?!\w)" : "August",
			"(?i)sep\.?(?!\w)" : "September",
			"(?i)oct\.?(?!\w)" : "October",
			"(?i)nov\.?(?!\w)" : "November",
			"(?i)dec\.?(?!\w)" : "December",
		}

		# These punctuation characaters can simply be removed
		self._unambiguousPunctuation = "[?!()\[\],\"\'\|]"

		# These punctuation characters can only be removed if they
		# are not inside numbers (note the negative lookahead)
		self._ambiguousPunctuation = "[-\\\/\.:](?!\d)"

		# A pattern detecting am/pm
		self._timePattern = "(?i)([ap]m)(?!\w)"

		# A pattern detecting th/st (for dates)
		self._datePattern = "(?i)(?<=\d)th|st"

		# Redundant whitespace can be removed
		self._redundantWhitespace = "\s+"

		if not query:
			# Open the source file and read its contents into
			# _fileContents (automatically closes the file afterwards)
			with open(sourceFileName) as sourceFile:
				self._querySubmitted = sourceFile.read()
		else:
			self._querySubmitted = query

	def Tokenize(self):
		# First expand the abbreviations
		for pattern in self._abbreviations:
			self._querySubmitted = re.sub(pattern, self._abbreviations[pattern], self._querySubmitted)

		# Next, remove unambiguous punctuation
		self._querySubmitted = re.sub(self._unambiguousPunctuation, "", self._querySubmitted)

		# Remove ambiguous punctuation
		self._querySubmitted = re.sub(self._ambiguousPunctuation, "", self._querySubmitted)

		# Insert a (possibly redundant) space before am/pm
		self._querySubmitted = re.sub(self._timePattern, " \\1", self._querySubmitted)

		# Remove 'th' and 'st' after dates
		self._querySubmitted = re.sub(self._datePattern, "", self._querySubmitted)

		# Remove redundant whitespace
		self._querySubmitted = re.sub(self._redundantWhitespace, " ", self._querySubmitted)

		# Split into a list
		self._words = self._querySubmitted.split(" ")

		return self._words


def main():
	print("--------------------------------------")
	print("This program tokenizes words in a file")
	print("--------------------------------------\n")

	# Initialize the tokenizer
	tokenizer = BookingTokenizer()

	# Tokenize the contents of 'queries.txt'
	words = tokenizer.Tokenize()

	# Print each word on a new line
	for word in words:
		print(word)

	# Wait for input to continue
	input("\nPress <RETURN> to continue")

if __name__ == "__main__":
	print("\n=============================================")
	print("62760858 - COS4861 - Assignment 4 - 2021 - Q5")
	print("=============================================\n")
	main()