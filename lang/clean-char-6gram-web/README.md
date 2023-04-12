# clean-char-6gram-web

This method exploits MaCoCu web data for training a character 6-gram SGD classifier
from the scikit-learn package. For its training it selects 80 thousand sequences
per language. Each sequence is supposed to consist of letters and spaces
only, and be more than 100 characters long. As the gold label we use the
national top-level-domain information the text was published on, .ba for
Bosnian, .hr for Croatian, .me for Montenegrin and .rs for Serbian. We
transliterate all text into the Latin script.

We prepare the classifier in two flavours, for three languages (bs, hr, sr)
and four languages (bs, hr, me, sr), so that we can evaluate it on all three
evaluation datasets.

The results show stellar performance on the Twitter dataset, and acceptable
performance on the SETimes dataset. Our hypothesis is that our training data
clean-up (taking only sequences of letters and spaces) performed a feature
selection that seems to be very much needed on the Twitter dataset. We argue
that other approaches might be as efficient on the Twitter dataset if they
took up a heavier data clean-up.
