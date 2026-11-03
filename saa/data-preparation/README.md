# Data Preparation for Machine Learning

Before a model can learn anything, the data has to be understood and made usable: explored, checked, cleaned, encoded and scaled. This folder explains those steps one concept per notebook, so that you can come back to the one you need whenever a workflow of yours uses it. Most notebooks start from a table small enough to see whole, then move to a real dataset that has the problem.

Its path is a basic overview: four notebooks on the decisions that the data of almost every model needs (filling gaps, encoding categories, scaling numbers) and on where each of those steps belongs. They are part of the stage of supervised learning, and are best read after part 3 of [Supervised learning](../supervised-learning/README.md#path), whose pipelines they use. The deep dives go further, one concept each. The folder assumes the NumPy and pandas essentials (loading, selecting, grouping, the problems a table can have), and doesn't depend on any particular model: where a step belongs inside a model's pipeline, the notebook says so and shows why.

## Before you start

- **pandas:** [Python data essentials](../../pia/python-data-essentials/README.md). Its notebook *Finding the problems in a table* finds missing, duplicated and impossible values and fixes what a fixed rule can fix; this folder starts where it stops, with the decisions that depend on the data.
- **Data as arrays:** [Matrices and tensors in AI](https://github.com/avidaldo/compare-python-c-efficiency/blob/main/02_matrices_in_ai.ipynb): a row as a vector, a table as a matrix, an image as an array.
- **Pipelines:** the notebooks show each step inside a scikit-learn `Pipeline` when it has to be fitted on the training data. How pipelines work is explained in [California housing with pipelines](../supervised-learning/basic-workflows/california_with_pipelines.ipynb).

## Path

None of the four is a core item (★): where the core notebooks of Supervised learning use one of these steps, they say what you need of it. A section whose heading ends in *(deep dive)* is optional, like the deep dives below, and never asked.

| # | Notebook | Content | Applied in |
| --- | --- | --- | --- |
| 1 | [Missing values](missing_values.ipynb) | Why a value is missing changes what you can do about it; dropping, filling with a statistic, flagging, filling from similar rows or from the other columns, leaving it to the model; what each choice assumes | [California housing with pipelines](../supervised-learning/basic-workflows/california_with_pipelines.ipynb), [Pima diabetes](../supervised-learning/basic-workflows/pima_diabetes.ipynb), [Thyroid](https://github.com/avidaldo/thyroid/blob/master/01_data_preparation.ipynb) |
| 2 | [Encoding categories](categorical_encoding.ipynb) | Ordinal and one-hot encoding, and when each one is wrong; categories that appear only in new data; categories with many values: grouping the rare ones and target encoding | [California housing with pipelines](../supervised-learning/basic-workflows/california_with_pipelines.ipynb), [XGBoost](../supervised-learning/algorithms/tree-based/xgboost.ipynb) |
| 3 | [Scaling numerical features](feature_scaling.ipynb) | Which models need scaling and why (distances, gradients, penalties), and which don't (trees); min-max, standard, robust and max-abs scaling compared on the same column; scaling the target | [k-nearest neighbours](../supervised-learning/algorithms/neighbours/knn.ipynb), [Gradient descent](../supervised-learning/ml-fundamentals/gradient_descent.ipynb), [Support vector machines](../supervised-learning/deep-dives/svm.ipynb) |
| 4 | [Where data preparation ends and modelling begins](where_preparation_ends.ipynb) | Steps that learn nothing from the data can be done once, for everyone, in the data pipeline (ETL); steps that learn from it must be fitted on the training data only, inside the model's pipeline; a leak demonstrated on a column of pure noise | [Pima diabetes](../supervised-learning/basic-workflows/pima_diabetes.ipynb), [Data leakage](../supervised-learning/ml-fundamentals/data_leakage.ipynb) |

## Deep dives

Optional and never assessed. The path never depends on these.

| Notebook | Extends | Content | Applied in |
| --- | --- | --- | --- |
| [Kinds of features](deep-dives/kinds_of_features.ipynb) | 1–4 | What a row, a feature and a target are; numbers, categories (with and without an order), dates, text, identifiers; why the type pandas gives a column is not its kind; columns that must not be features | [Pima diabetes](../supervised-learning/basic-workflows/pima_diabetes.ipynb), [Diabetes progression](../supervised-learning/basic-workflows/deep-dives/diabetes_progression.ipynb) |
| [Exploring a dataset](deep-dives/exploring_a_dataset.ipynb) | 1–4 | The questions to ask a new table and the summary or plot that answers each one; what may be looked at before the split and what only on the training set; writing the findings down as decisions | [King County, EDA](https://github.com/avidaldo/king-county/blob/master/01-eda.ipynb), [Thyroid, data preparation](https://github.com/avidaldo/thyroid/blob/master/01_data_preparation.ipynb) |
| [Correlation and what it misses](deep-dives/correlation.ipynb) | *Exploring a dataset* | Pearson's coefficient, computed by hand and as a matrix; relationships it can't see; Spearman's coefficient; a correlation that reverses inside each group | [California housing, step by step](../supervised-learning/basic-workflows/california_by_hand.ipynb) |
| [Outliers and capped values](deep-dives/outliers.ipynb) | 1, 3 | An error, a rare case or a different population; rules for finding them and why the usual one is fooled by the outliers themselves; capped values, which are not outliers; keeping, clipping, transforming or flagging | [California housing, step by step](../supervised-learning/basic-workflows/california_by_hand.ipynb), [Thyroid](https://github.com/avidaldo/thyroid/blob/master/01_data_preparation.ipynb) |
| [Skewed distributions and the log transform](deep-dives/skewed_distributions.ipynb) | 3 | Long right tails and why they matter to some models and not to others; the logarithm, power and quantile transforms; taking the logarithm of the target, and what the model then predicts | [King County, preprocessing](https://github.com/avidaldo/king-county/blob/master/04a-preprocessing-step-by-step.ipynb), [Thyroid](https://github.com/avidaldo/thyroid/blob/master/01_data_preparation.ipynb) |
| [Creating features](deep-dives/creating_features.ipynb) | 2, 4 | Ratios, parts of a date, time elapsed, cyclic values, bins and products; features computed from each row alone, and features learned from the data | [California housing with pipelines](../supervised-learning/basic-workflows/california_with_pipelines.ipynb), [King County, preprocessing](https://github.com/avidaldo/king-county/blob/master/04a-preprocessing-step-by-step.ipynb) |
| [Scaling images](deep-dives/scaling_images.ipynb) | 3 | Why a table is scaled column by column and an image with one mean and deviation per colour channel; images flattened into rows | |

## From small workflows to a big one

The notebooks above explain one step each. To see the steps working together, follow complete workflows from the smallest to the largest:

1. The basic workflows of [Supervised learning](../supervised-learning/README.md#path): California housing step by step and with pipelines, Diabetes progression and Pima diabetes.
2. [King County house sales](https://github.com/avidaldo/king-county) and [Thyroid disease](https://github.com/avidaldo/thyroid): one real dataset each, with its own problems.
3. [California housing, end to end](https://github.com/avidaldo/california_e2e): a complete project, from framing the problem to a tuned model.

## Running the notebooks

Install the packages of the course repository's [`requirements.txt`](../../requirements.txt) in an environment of your choice (uv, venv or conda) and run each notebook from its own folder. The datasets are downloaded the first time a notebook needs them, into a `data/` folder next to it, which git ignores.

## Related

- [Supervised learning](../supervised-learning/README.md): the train/test split, pipelines and data leakage, which this folder applies without explaining again.
- Unsupervised learning *(coming)*: principal component analysis, clusters as features, and anomaly detection.
