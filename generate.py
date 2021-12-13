import random

from german_nouns import nouns


def get_random_noun():
    while True:
        noun = random.choice(nouns)
        if noun["pos"] == "Substantiv":
            return noun


first_articles = {"n": ["ein"], "f": ["eine"], "m": ["einen"]}
second_articles = {
    "n": [
        "kein einziges neues",
        "ein einziges neues",
        "ein neues",
        "ein einziges",
        "kein einziges",
        "kein neues",
    ],
    "f": [
        "keine einzige neue",
        "eine einzige neue",
        "eine neue",
        "eine einzige",
        "keine einzige",
        "keine neue",
    ],
    "m": [
        "kein einziger neuer",
        "ein einziger neuer",
        "ein neuer",
        "ein einziger",
        "kein einziger",
        "kein neuer",
    ],
}


def get_random_with_article(articles):
    noun = get_random_noun()
    while noun["genus"] not in articles:
        noun = get_random_noun()

    article = random.choice(articles[noun["genus"]])
    return f"{article} {noun['lemma']}"


def get_sentence():
    return f"Durch {get_random_with_article(first_articles)} entsteht {get_random_with_article(second_articles)}."


if __name__ == "__main__":
    print(get_sentence())
