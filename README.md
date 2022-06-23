---
title: Next_Word_Prediction
emoji: 🐢
colorFrom: indigo
colorTo: gray
sdk: gradio
sdk_version: 2.9.1
app_file: app.py
pinned: false
---
Check out the Space at https://huggingface.co/spaces/Shruhrid/Next_Word_Prediction

# Probabilistic approach to Next Word Prediction #
The task of predicting the next word using an n-gram model is equivalent to the
probability of getting a specific word at the nth place given the previous n-1 words. The
probability of the same is given by the Bayesformula,P(w |w₁,.....,w ₋₁)

# Key Aspects #

### Laplace Smoothing ###
Laplace smoothing is a technique that helps when the dataset remains limited for a plrobabilistic approach. Essentially it helps to avoid the problem of zero probability.
For a bigram approach:

![image](https://user-images.githubusercontent.com/76119205/175379976-33345bac-83fc-42dd-bed0-8090ebbe1296.png)

| Keyword  | Meaning |
| ------------- | ------------- |
| P*   | Probability of the Laplace Smoothed N-grams  |
| Wi  | i’th word |
| 𝑐(Wi,Wi-1)| count of word sequence Wi-1,Wi) |
|V | total number of words in vocabulary |


### Perplexity ###

Being confused ain't as bad as you may think! Perplexity is a measure of how certain the model was while making the predictions. It is the inverse of the probability of predicting the test set normalized by the number of words.


