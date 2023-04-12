# char_ngram_baseline

This method served as a baseline in the time of writing the article about discriminating between closely related languages. The [script](char_ngram_baseline.py) loads the Twitter and SETimes datasets and runs a char-3-gram tokenizer and a LinearSVC model to train on SETimes, Twitter, and Twitter3 data (the latter being the subset of only `hr`, `sr`, and `bs` tweets).

When running the script, the classification reports are output for evaluation, and the predictions are stored in a json file, compatible with other results.

We discovered the performance to be quite good in-domain, while out-of-domain were less promissing.