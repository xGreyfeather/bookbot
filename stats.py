def num(i):
	return i["count"]

def word_count(text):
	counter = 0
	words = text.split()
	return len(words)

def character_count(words):
	lowercase = words.lower()
	characters = {}
	for i in lowercase:
		if i in characters:
			characters[i] += 1
		else:
			characters[i] = 1
	return characters

def data_sorter(characters):
	char = []
	for i, count in characters.items():
		char.append({"character": i, "count": count})
	char.sort(reverse=True, key=num)
	return char
