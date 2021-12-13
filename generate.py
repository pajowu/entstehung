import random

from german_nouns.lookup import Nouns

nouns = Nouns()

def get_random_noun():
	while True:
		noun = random.choice(nouns)[0]
		if noun['pos'] == ['Substantiv']:
			return noun

first_articles = {"n": "ein", "f": "eine", "m": "einen"}
second_articles = {"n": "kein einziges", "f": "eine einzige", "m": "kein einziger"}
def get_random_with_article(articles):
	noun = get_random_noun()
	return f"{articles[noun['genus']]} {noun['lemma']}"

def get_sentence():
	return f"Durch {get_random_with_article(first_articles)} entsteht {get_random_with_article(second_articles)}."
