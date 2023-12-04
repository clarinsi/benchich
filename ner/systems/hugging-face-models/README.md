# Submisssion: Hugging Face models

In this submission, we evaluated the following Transformer-based language models that are available on the Hugging Face:
- 'csebert',
- 'xlm-r-base',
- 'xlm-r-large',
- 'bertic',
- 'xlm-r-bertic',
- 'xlm-r-slobertic'

We evaluated them on all four datasets.

We used the following code:
```
CUDA_VISIBLE_DEVICES=7 nohup python ner-classification.py > transformers_classification.log &
```