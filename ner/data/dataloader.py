import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("scenario", help="Possible arguments: s_Croatian, ns_Croatian, s_Serbian, ns_Serbian")
	args = parser.parse_args()

# Define the scenario
scenario = args.scenario


def extract_ner_dataset(scenario):
	"""
	Extract a NER dataset that can be used for NER evaluation with simple transformers.
	Args:
		- scenario: s_Croatian, ns_Croatian, s_Serbian, ns_Serbian
	"""
	from conllu import parse
	import pandas as pd
	import numpy as np
	import json

	datasets = {
	"s_Croatian": {
		"name": "Croatian linguistic training corpus hr500k 2.0",
		"path":"https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1792/hr500k.conllup",
		"dataset": ["hr500k.conllup"]},
	"ns_Croatian": {
		"name": "Croatian Twitter training corpus ReLDI-NormTagNER-hr 3.0",
		"path":"https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1793/reldi-normtagner-hr.conllup",
		"dataset": ["reldi-normtagner-hr.conllup"]},
	"s_Serbian": {
		"name": "Serbian linguistic training corpus SETimes.SR 2.0",
		"path":"https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1843/set.sr.plus.conllup",
		"dataset": ["set.sr.plus.conllup"]},
	"ns_Serbian": {
		"name": "Serbian Twitter training corpus ReLDI-NormTagNER-sr 3.0",
		"path":"https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1794/reldi-normtagner-sr.conllup",
		"dataset": ["reldi-normtagner-sr.conllup"]}
	}

	# Loop through all the datasets if there are multiple datasets for one scenario
	for i in range(len(datasets[scenario]["dataset"])):
		dataset = datasets[scenario]["dataset"][i]
		doc = "datasets/{}".format(dataset)

		# Open the dataset
		data = open("{}".format(doc), "r").read()

		# Parse conllu file
		sentences = parse(data)

		word_list = []
		sent_id_list = []
		NER_list = []
		split_list = []

		# Collect all important information from the dataset
		for sentence in sentences:
			current_sent_id = sentence.metadata["sent_id"]
			if sentence.metadata.get("contained_in_datasets", None) != None:
				current_dataset = sentence.metadata["contained_in_datasets"]
			if "train" in current_dataset:
				current_split = "train"
			elif "dev" in current_dataset:
				current_split = "dev"
			elif "test" in current_dataset:
				current_split = "test"
			for token in sentence:
				current_word = token["form"]
				current_ner = token["reldi:ne"]

				word_list.append(current_word)
				sent_id_list.append(current_sent_id)
				NER_list.append(current_ner)
				split_list.append(current_split)

		# Create a dictionary for all words and all needed information
		data_dict = {"sentence_id": sent_id_list, "words": word_list, "labels": NER_list, "split": split_list}

		# Create a pandas df out of the dictionary
		df = pd.DataFrame(data_dict)

		# Add integer ids, needed for classification
		df["id"] = list(range(len(sent_id_list)))

		LABELS = list(df.labels.unique())

		# If * is used, change * to O, because this causes errors
		if "*" in LABELS:
			LABELS[LABELS.index("*")] = "O"

			df["labels"] = np.where(df["labels"] == "*", "O", df["labels"])
		
		if "B-*" in LABELS:
			# Change also B-* and I-*
			LABELS[LABELS.index("B-*")] = "B-O"

			df["labels"] = np.where(df["labels"] == "B-*", "B-O", df["labels"])
		
		if "I-*" in LABELS:
			LABELS[LABELS.index("I-*")] = "I-O"

			df["labels"] = np.where(df["labels"] == "I-*", "I-O", df["labels"])
			
		# Show the df
		print(df.head())
		print("\n")
		print(df.describe(include="all"))
		print("\n")
		print(df.split.value_counts())
		print("\n")
		print(df.labels.value_counts())
		print("\n")
		print(df.labels.value_counts(normalize=True))
		print("\n")

		# Save the information in a format that will be used by simpletransformers

		json_dict = {
			"labels": LABELS,
			"train": df[df["split"] == "train"].drop(columns="split").to_dict(),
			"dev": df[df["split"] == "dev"].drop(columns="split").to_dict(),
			"test": df[df["split"] == "test"].drop(columns="split").to_dict()
		}

	# Save json as file

	# Remove the suffix from the dataset name
	dataset_name = dataset[:-len(".conllup")]

	with open("datasets/{}.json".format(dataset_name), "w") as end_file:
		json.dump(json_dict, end_file, indent=2)

	print("\n\nExtracted dataset saved as datasets/{}.json".format(dataset_name))

extract_ner_dataset(scenario)