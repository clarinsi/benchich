import pandas as pd
import json
from simpletransformers.ner import NERModel
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
import logging
import gc
import torch
import time
from knockknock import discord_sender

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

# Get all the datasets in the data/datasets directory
absolute_path = os.getcwd()
dataset_path = absolute_path[:-len("systems/hugging-face-models")] + "data/datasets/"

datasets = os.listdir(dataset_path)

# Add the path to the datasets
dataset_paths = [dataset_path + x for x in datasets]

dataset_dict = {x[0]:x[1] for x in list(zip(dataset_paths, datasets))}

# Let's redo only the experiment on hr500k
for dataset_path in dataset_paths[:1]:
    # Load the json file
    with open(dataset_path, "r") as file:
        json_dict = json.load(file)

    dataset_name = dataset_dict[dataset_path]

    # Open the train, eval and test dictionaries as DataFrames
    train_df = pd.DataFrame(json_dict["train"])
    test_df = pd.DataFrame(json_dict["test"])
    dev_df = pd.DataFrame(json_dict["dev"])

    # Drop original_id
    for df in [train_df, test_df, dev_df]:
        df.drop(columns=["original_id"], inplace=True)

    # Define the labels
    LABELS = json_dict["labels"]
    print(LABELS)

    print(train_df.shape, test_df.shape, dev_df.shape)
    print(train_df.head())

    # Get notified once the code ends
    webhook_url = open("/home/tajak/Parlamint-translation/discord_key.txt", "r").read()
    @discord_sender(webhook_url=webhook_url)
    def train_and_test(model, train_df, test_df, dataset_path, LABELS):

        # Define the model arguments - these arguments hold for all models,
        # we just change the epoch number based on hyperparameter search
        model_args = {"overwrite_output_dir": True,
                    "num_train_epochs": 5,
                    "labels_list": LABELS,
                    "learning_rate": 4e-05,
                    "train_batch_size": 32,
                    # Comment out no_cache and no_save if you want to save the model
                    "no_cache": True,
                    "no_save": True,
                    "max_seq_length": 256,
                    "save_steps": -1,
                    "silent": True,
                    }
        
        # Define the type of dataset we are using
        dataset_type = "standard_hr"

        if "reldi" in dataset_path:
            dataset_type = "non_standard"
        elif "set.sr" in dataset_path:
            dataset_type = "standard_sr"

        # Change no. of epochs based on the model and the dataset
        # For xlm-r-bertic and xlm-r-slobertic, we use the same no. of epochs as for the xlm-r-large
        if dataset_type == "standard_hr":
            if model == "xlm-r-base":
                model_args["num_train_epochs"] = 5
            elif model == "csebert":
                model_args["num_train_epochs"] = 4
            elif model == "xlm-r-large":
                model_args["num_train_epochs"] = 7
            elif model == "xlm-r-bertic":
                model_args["num_train_epochs"] = 7
            elif model == "xlm-r-slobertic":
                model_args["num_train_epochs"] = 7
            elif model == "bertic":
                model_args["num_train_epochs"] = 9
        elif dataset_type == "non_standard":
            if model == "xlm-r-base":
                model_args["num_train_epochs"] = 8
            elif model == "csebert":
                model_args["num_train_epochs"] = 7
            elif model == "xlm-r-large":
                model_args["num_train_epochs"] = 11
            elif model == "xlm-r-bertic":
                model_args["num_train_epochs"] = 11
            elif model == "xlm-r-slobertic":
                model_args["num_train_epochs"] = 11
            elif model == "bertic":
                model_args["num_train_epochs"] = 10
        elif dataset_type == "standard_sr":
            if model == "xlm-r-base":
                model_args["num_train_epochs"] = 6
            elif model == "csebert":
                model_args["num_train_epochs"] = 9
            elif model == "xlm-r-large":
                model_args["num_train_epochs"] = 13
            elif model == "xlm-r-bertic":
                model_args["num_train_epochs"] = 13
            elif model == "xlm-r-slobertic":
                model_args["num_train_epochs"] = 13
            elif model == "bertic":
                model_args["num_train_epochs"] = 10

        # Model type - a dictionary of type and model name.
        model_type_dict = {
            "csebert": ["bert", "EMBEDDIA/crosloengual-bert"],
            "xlm-r-base": ["xlmroberta", "xlm-roberta-base"],
            "xlm-r-large": ["xlmroberta", "xlm-roberta-large"],
            "bertic": ["electra", "classla/bcms-bertic"],
            "xlm-r-bertic": ["xlmroberta", "classla/xlm-r-bertic"],
            "xlm-r-slobertic": ["xlmroberta", "classla/xlm-r-slobertic"]
        }

        # Define the model
        current_model = NERModel(
        model_type_dict[model][0],
        model_type_dict[model][1],
        labels = LABELS,
        use_cuda=True,
        args = model_args)

        print("Training started. Current model: {}, no. of epochs: {}".format(model, model_args["num_train_epochs"]))
        start_time = time.time()

        # Fine-tune the model
        current_model.train_model(train_df)

        print("Training completed.")

        training_time = round((time.time() - start_time)/60,2)

        print("It took {} minutes for {} instances.".format(training_time, train_df.shape[0]))

        # Clean cache
        gc.collect()
        torch.cuda.empty_cache()

        start_evaluation_time = time.time()

        # Evaluate the model
        results = current_model.eval_model(test_df)

        print("Evaluation completed.")

        evaluation_time = round((time.time() - start_evaluation_time)/60,2)

        print("It took {} minutes for {} instances.".format(evaluation_time, test_df.shape[0]))

        # Get predictions
        preds = results[1]

        # Create a list with predictions
        preds_list = []

        for sentence in preds:
            for word in sentence:
                current_word = []
                for element in word:
                    # Find prediction with the highest value
                    highest_index = element.index(max(element))
                    # Transform the index to label
                    current_pred = current_model.config.id2label[highest_index]
                    # Append to the list
                    current_word.append(current_pred)
                # Segmentation can result in multiple predictions for one word - use the first prediction only
                preds_list.append(current_word[0])
        
        # Create a json with results
        results = {
            "system": model,
            "predictions": [
                {
                "train": "{} (train split)".format(dataset_name),
                "test": "{} (test split)".format(dataset_name),
                "predictions": preds_list,
                }
            ],
            "model": model_type_dict[model][1],
            "args": model_args,
            }
        
        return results

    #model_list = ['csebert', 'xlm-r-base', 'xlm-r-large', 'bertic', 'xlm-r-bertic', 'xlm-r-slobertic']
    # Redo only xlm-r-bertic
    model_list = ['xlm-r-bertic']

    for model in model_list:
        # Let's do only one run
        for run in [0]:
            current_results = train_and_test(model, train_df, test_df, dataset_path, LABELS)

            # Save the results as a new json
            with open("submissions/submission-{}-{}.json".format(model, dataset_name), "w") as file:
                json.dump(current_results, file)
        
            print("Run {} finished.".format(run))