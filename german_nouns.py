import csv
import json

nouns = []
with open('nouns.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['pos'] == "Substantiv":
			nouns.append({"lemma": row['lemma'], "genus": row['genus'], "pos": row['pos']})

with open("nouns.json", "w") as f:
	json.dump(nouns, f)
