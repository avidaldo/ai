# Naive Bayes, from the theorem to a spam filter

For two classes, naive Bayes is a classifier of the same form as [logistic regression](../../algorithms/linear-models/logistic_regression.ipynb), but it sets its weights by counting the words of each class instead of by minimising an error.

A spam filter built three times, each time with less code and more understanding: first Bayes' theorem on a single word, counted by hand; then a complete naive Bayes classifier in a few lines of Python, checked against scikit-learn's; finally the filter as a scikit-learn pipeline, compared with logistic regression, tuned for what each mistake costs, and examined message by message.

The data is the SMS Spam Collection: 5,574 real text messages labelled spam or ham (legitimate), downloaded on first use from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)); it isn't stored with the notebooks.

## Notebooks

| # | Notebook | Content |
| --- | --- | --- |
| 1 | [Bayes' theorem, one word at a time](one_word.ipynb) | Prior, likelihoods and posterior, counted on the messages for one word; why the posterior equals direct counting, and why the prior matters as much as the word |
| 2 | [A naive Bayes classifier by hand](naive_bayes_by_hand.ipynb) | Why repeated messages are removed before splitting; the naive assumption, measured; word counts per class; smoothing for words a class has never seen; logarithms against underflow; the classifier as a class with scikit-learn's conventions, identical to `MultinomialNB` |
| 3 | [The spam filter with scikit-learn](spam_filter_scikit_learn.ipynb) | Counts, presence, TF-IDF and word pairs, against a logistic regression, by cross-validation; a threshold for what each mistake costs; the messages it gets wrong; the words that weigh most, and what they reveal about how the data was collected; where naive Bayes stands today |

The notebooks explain the probability they use; the derivation of the theorem is in the deep dive [Probability and Bayes' theorem](../../../concepts/deep-dives/probability/README.md). Notebook 3 uses the pipelines, cross-validation and classification metrics of Supervised learning's path.

## Setup

The packages are those of the course repository's `requirements.txt`. Open the notebooks from this folder, so that `from sms_spam import load_sms_spam` finds the loader; the first run downloads the data (about 200 KB) into `data/`.

## Going further

- Replace the `&lt;#&gt;` and `&lt;URL&gt;` placeholders, and the colloquial forms that only one class uses, before vectorising, and measure how much of the filter's accuracy came from them.
- Train the filter on part of the messages and update it with the rest using `MultinomialNB.partial_fit`, one batch at a time, as a filter on a phone would. `partial_fit` can't learn words it has never seen, so the vocabulary has to be fixed in advance: `HashingVectorizer(alternate_sign=False)` instead of `CountVectorizer`.
- Calibrate the probabilities with `CalibratedClassifierCV` and compare their histogram with the one in *The spam filter with scikit-learn*.

## Source of the data

Almeida, T. A., Gómez Hidalgo, J. M. and Yamakami, A. (2011). Contributions to the study of SMS spam filtering: new collection and results. *Proceedings of the 11th ACM Symposium on Document Engineering*, 259–262. The collection is in the [UCI Machine Learning Repository](https://doi.org/10.24432/C5CC84) and on [its authors' page](http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/).
