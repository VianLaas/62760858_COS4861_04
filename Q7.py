from Q5 import BookingTokenizer

class RedundantTokenRemover():
	def __init__(self, tokenizedQueries = [], stopwordsFileName = 'stopwords.txt'):
		# Read the contents of our stopwords corpus into a list
		with open(stopwordsFileName) as stopwordsFile:
			self._stopwords = stopwordsFile.read()
		
		# We'll need to modify the tokenized queries as we remove the
		# redundant ones
		self._words = tokenizedQueries

	def RemoveRedundantTokens(self):
		# Start with an empty list
		tempWords = []

		# And then add each word in self._words
		# if it is not a stopword
		for word in self._words:
			if not word.lower() in self._stopwords:
				tempWords.append(word)

		self._words = tempWords

		return self._words

def main():
	print("-------------------------------------")
	print("This program removes redundant tokens")
	print("-------------------------------------\n")

	# Initialize the tokenizer
	tokenizer = BookingTokenizer()

	# Tokenize the contents of 'queries.txt'
	words = tokenizer.Tokenize()

	# Initialize the redundancy remover
	remover = RedundantTokenRemover(words)

	# Remove the redundant tokens
	words = remover.RemoveRedundantTokens()

	# Print each word on a new line
	for word in words:
		print(word)

	# Wait for input to continue
	input("\nPress <RETURN> to continue")

if __name__ == "__main__":
	print("\n=============================================")
	print("62760858 - COS4861 - Assignment 4 - 2021 - Q7")
	print("=============================================\n")
	main()