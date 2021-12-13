import csv
import json
import os.path

if os.path.exists("nouns.json"):
	with open("nouns.json") as f:
		nouns = json.load(f)
else:
	nouns = []
	with open('nouns.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if row['pos'] == "Substantiv":
				nouns.append({"lemma": row['lemma'], "genus": row['genus'], "pos": row['pos']})

	with open("nouns.json", "w") as f:
		json.dump(nouns, f)
