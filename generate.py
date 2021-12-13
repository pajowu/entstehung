import random

from german_nouns import nouns


def get_random_noun():
	while True:
		noun = random.choice(nouns)
		if noun['pos'] == 'Substantiv':
			return noun

first_articles = {"n": "ein", "f": "eine", "m": "einen"}
second_articles = {"n": "kein einziges neues", "f": "keine einzige neue", "m": "kein einziger neuer"}
def get_random_with_article(articles):
	noun = get_random_noun()
	while noun['genus'] not in articles:
		noun = get_random_noun()
	return f"{articles[noun['genus']]} {noun['lemma']}"

def get_sentence():
	return f"Durch {get_random_with_article(first_articles)} entsteht {get_random_with_article(second_articles)}."

if __name__ == '__main__':
	print(get_sentence())
