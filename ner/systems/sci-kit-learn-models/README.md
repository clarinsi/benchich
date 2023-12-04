# Classification with traditional models from the sci-kit learn library

We evaluated the following classifiers using the following hyperparameters:
- "Dummy": DummyClassifier(strategy="stratified"),
- "Naive Bayes": ComplementNB(),
- "Logistic Regression": LogisticRegression(penalty=None)

The `TfidfVectorizer(tokenizer=tokenizer,use_idf=True,min_df=0.005)`` was used to transform text into vectors.