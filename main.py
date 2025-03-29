import sys

def get_book_text(filepath):
	return filepath.read()

from stats import num
from stats import word_count
from stats import character_count
from stats import data_sorter

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	with open(sys.argv[1]) as f:
		text = get_book_text(f)
	with open(sys.argv[1]) as f:
		words = f.read()
		characters = character_count(words)
		sorted = data_sorter(characters)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count(words)} total words")
	print("--------- Character Count -------")

	for char in sorted:
		alpha = char["character"]
		counter = char["count"]
		if alpha.isalpha():
			print(f"{alpha}: {counter}")
	print("============= END ===============")

main()
