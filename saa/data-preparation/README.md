# Data Preparation for Machine Learning

Before a model can learn anything, the data has to be understood and made usable: explored, checked, cleaned, encoded and scaled. Each notebook explains one step, starting from a table small enough to see whole and moving to a real dataset that has the problem, so that you can come back to the one you need.

The path is a basic overview of the steps that almost every model needs, read after part 3 of [Supervised learning](../supervised-learning/README.md#path), whose pipelines it uses. It starts where the pandas of [Python data essentials](../../pia/python-data-essentials/README.md) stops, with the decisions that depend on the data. The deep dives go further, one step each.

## Path

None of the four is a core item (★): where a core notebook of Supervised learning uses one of these steps, it says what you need of it. A section whose heading ends in *(deep dive)* is optional, like the deep dives below, and never asked.

| # | Notebook | Content |
| --- | --- | --- |
| 1 | [Missing values](missing_values.ipynb) | Why a value is missing changes what you can do about it; dropping, filling with a statistic, flagging, filling from similar rows or from the other columns, leaving it to the model; what each choice assumes |
| 2 | [Encoding categories](categorical_encoding.ipynb) | Ordinal and one-hot encoding, and when each one is wrong; categories that appear only in new data; categories with many values: grouping the rare ones and target encoding |
| 3 | [Scaling numerical features](feature_scaling.ipynb) | Which models need scaling and why (distances, gradients, penalties), and which don't (trees); min-max, standard, robust and max-abs scaling compared on the same column; scaling the target |
| 4 | [Where data preparation ends and modelling begins](where_preparation_ends.ipynb) | Steps that learn nothing from the data can be done once, for everyone, in the data pipeline (ETL); steps that learn from it must be fitted on the training data only, inside the model's pipeline; a leak demonstrated on a column of pure noise |

## Deep dives

Optional and never assessed. The path never depends on these.

| Deep dive | Extends | Content |
| --- | --- | --- |
| [Kinds of features](deep-dives/kinds_of_features.ipynb) | 1–4 | What a row, a feature and a target are; numbers, categories (with and without an order), dates, text, identifiers; why the type pandas gives a column is not its kind; columns that must not be features |
| [Exploring a dataset](deep-dives/exploring_a_dataset.ipynb) | 1–4 | The questions to ask a new table and the summary or plot that answers each one; what may be looked at before the split and what only on the training set; writing the findings down as decisions |
| [Correlation and what it misses](deep-dives/correlation.ipynb) | *Exploring a dataset* | Pearson's coefficient, computed by hand and as a matrix; relationships it can't see; Spearman's coefficient; a correlation that reverses inside each group |
| [Outliers and capped values](deep-dives/outliers.ipynb) | 1, 3 | An error, a rare case or a different population; rules for finding them and why the usual one is fooled by the outliers themselves; capped values, which are not outliers; keeping, clipping, transforming or flagging |
| [Skewed distributions and the log transform](deep-dives/skewed_distributions.ipynb) | 3 | Long right tails and why they matter to some models and not to others; the logarithm, power and quantile transforms; taking the logarithm of the target, and what the model then predicts |
| [Creating features](deep-dives/creating_features.ipynb) | 2, 4 | Ratios, parts of a date, time elapsed, cyclic values, bins and products; features computed from each row alone, and features learned from the data |
| [Scaling images](deep-dives/scaling_images.ipynb) | 3 | Why a table is scaled column by column and an image with one mean and deviation per colour channel; images flattened into rows |
