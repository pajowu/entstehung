import json

with open("nouns.json") as f:
	nouns = json.load(f)

with open("blocklist.txt") as f:
	blocked = f.read().splitlines()

def check_word(word):
	for blocked_word in blocked:
		if blocked_word.lower() in word.lower():
			return False
	return True

filtered_nouns = []
for noun in nouns:
	if check_word(noun['lemma']):
		filtered_nouns.append(noun)
	else:
		print(noun['lemma'])

with open("filtered_nouns.json", "w") as f:
	json.dump(filtered_nouns, f, indent='\t')
