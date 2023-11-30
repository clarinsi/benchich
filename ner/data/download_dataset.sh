#!/bin/bash

# Iterate through all wanted datasets

# Define the Python dictionary as a string
dictionary_json='{
    "s_Croatian": {
        "name": "Croatian linguistic training corpus hr500k 2.0",
        "path":"https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1792/hr500k.conllup"},
    "ns_Croatian": {
        "name": "Croatian Twitter training corpus ReLDI-NormTagNER-hr 3.0",
        "path":"https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1793/reldi-normtagner-hr.conllup"},
    "s_Serbian": {
        "name": "Serbian linguistic training corpus SETimes.SR 2.0",
        "path":"https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1843/set.sr.plus.conllup"},
    "ns_Serbian": {
        "name": "Serbian Twitter training corpus ReLDI-NormTagNER-sr 3.0",
        "path":"https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1794/reldi-normtagner-sr.conllup"}
    }'

# Iterate over items in the dataset list
for dataset in "$@"; do
    echo "Processing dataset: $dataset"
    
    # Get the argument provided for "dataset" and extract the path
    path=$(echo "$dictionary_json" | python3 -c "import sys, json; print(json.load(sys.stdin).get('$dataset', {}).get('path', ''))")

    # Get the argument for the name of the dataset
    name=$(echo "$dictionary_json" | python3 -c "import sys, json; print(json.load(sys.stdin).get('$dataset', {}).get('name', ''))")

    # Get the argument for zipped folder (if it exists)
    downloaded_file=$(echo "$dictionary_json" | python3 -c "import sys, json; print(json.load(sys.stdin).get('$dataset', {}).get('downloaded_file', ''))")

    #Create folder datasets if it does not exist yet
    if [ ! -d 'datasets' ]; then
        # Create the folder
        mkdir datasets
    fi

    cd datasets

    # Perform wget operation if the path is not empty
    [ -n "$path" ] && curl -s --remote-name-all "$path" || echo "Invalid argument provided. You can choose from s_Slovene, ns_Slovene, s_Croatian, ns_Croatian, s_Serbian and ns_Serbian."

    # Check if the download was successful
    if [ -f "$downloaded_file" ]; then
        # Extract the downloaded zip file to the specified folder
        unzip -q "$downloaded_file"
        echo "Downloaded and extracted '$name' successfully."
        # Optionally, remove the downloaded zip file
        rm "$downloaded_file"
    else
        echo "Downloaded '$name' successfully."
    fi

    cd ..
done

