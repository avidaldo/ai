# The Life of a Machine Learning Project

Training a model is a small part of a machine learning project. Most of the work goes into framing the problem, getting the data right and checking that the model really works. The steps form a loop, because what you learn at one step often sends you back to an earlier one:

```text
frame the problem → get and explore the data → prepare the data → train and tune → evaluate → deploy and monitor
```

## The Steps

### Frame the Problem

- **What exactly is predicted,** for whom, and which decision the prediction changes.
- **How success is measured:** a measure that matters to the people who use the model, such as fewer unpaid loans, and a model metric that follows it, chosen before any model is trained.
- **A baseline:** the simplest possible answer, such as the mean price of all the houses, or the most frequent class. A model is only worth its cost if it clearly beats it.
- **Whether machine learning is needed at all:** if a few clear rules solve the problem, write the rules ([rules and expert systems](../deep-dives/classical-ai/rules_and_expert_systems.ipynb)).

### Get and Explore the Data

- Where the data comes from, what each column means and how it was measured, and how much there is.
- **Exploration** (*exploratory data analysis*, EDA): the distribution of each column, the relations between columns, and the problems: missing values, errors, duplicates, extreme values. The tools are those of [Python data essentials](../../../pia/python-data-essentials/README.md).
- *Garbage in, garbage out*: no model can find an answer that the data doesn't contain.

### Prepare the Data

- **Set the test set aside first,** before deciding anything from the data (see [generalisation](#generalisation-the-central-problem) below).
- Clean the data, encode categories as numbers, scale, and create the features that help the model (*feature engineering*), deciding each step on the training data only. [Data preparation](../../data-preparation/README.md) goes through each of them.

### Train and Tune

- Choose a few candidate algorithms that suit the task and the data ([choosing the right algorithm](ml_algorithms_history.md#choosing-the-right-algorithm)).
- Train each one, and tune its hyperparameters on validation data, never on the test set.

### Evaluate

- Measure the chosen model on the test set, once, with the metric chosen at the start, and compare it with the baseline.
- Read the errors: which examples fail, and why. Check that the model works equally well for the different groups of people it affects.
- If it isn't good enough, go back: more or better data, other features, another model.

### Deploy and Monitor

- **Put the model where it is used:** predictions in batches (every night, for every customer), on demand behind a web API (each time a form is sent), or on a device such as a phone. This is the topic on serving models *(coming)*.
- **Watch it in use.** The world changes, and a model trained on last year's data slowly gets worse: this is called *drift*. Track its performance, and retrain it on recent data when it drops.

## Generalisation: the Central Problem

The goal is not to fit the training data, but to predict well for examples the model has never seen: to **generalise**. A model can be perfect on its training data by memorising it and still fail on new data, so its score on the training data proves nothing. Three models that predict the price of a house from its area:

| Model | Error on its training data | Error on new data | Diagnosis |
| --- | --- | --- | --- |
| A straight line, when the price grows faster than the area | High | High | **Underfitting:** too simple to capture the pattern |
| A model of the right complexity | Low | Low, a little higher | A good fit |
| A tree grown until each leaf holds a single house | Almost zero | High | **Overfitting:** it learned the noise of its examples, not only the pattern |

That is why the data is split into three sets:

- the **training set**, to fit the model's parameters;
- the **validation set**, to choose between models and hyperparameters; *cross-validation* does the same by taking turns with parts of the training set;
- the **test set**, kept apart and used once, at the end. A test set that has been used to choose a model no longer measures new data, and gives an optimistic score.

**Data leakage** is the same mistake in disguise: information the model won't have when it predicts gets into its training. Two examples: scaling the data with the mean of all of it, test set included; or predicting whether a loan will be repaid with a feature that is only known afterwards, such as the date it was written off. A score that looks too good to be true usually is.

How to measure all this, and how to avoid these mistakes, is the core of [supervised learning](../../supervised-learning/README.md).
