# Data Preparation for Machine Learning

Before a model can learn anything, the data has to be understood and made usable: explored, checked, cleaned, encoded and scaled. Each notebook explains one step, starting from a table small enough to see whole and moving to a real dataset that has the problem, so that you can come back to the one you need.

The path is a basic overview of the steps that almost every model needs, read after part 3 of [Supervised learning](../supervised-learning/README.md#path), whose pipelines it uses. It starts where the pandas of [Python data essentials](../../pia/python-data-essentials/README.md) stops, with the decisions that depend on the data.

## Path

| # | Tier | Item | Content |
| --- | --- | --- | --- |
| 1 | standard | [Missing values](missing_values.ipynb) | Why a value is missing changes what you can do about it; dropping, filling with a statistic, flagging, filling from similar rows or from the other columns, leaving it to the model; what each choice assumes |
| 2 | standard | [Encoding categories](categorical_encoding.ipynb) | Ordinal and one-hot encoding, and when each one is wrong; categories that appear only in new data; categories with many values: grouping the rare ones and target encoding |
| 3 | standard | [Scaling numerical features](feature_scaling.ipynb) | Which models need scaling and why (distances, gradients, penalties), and which don't (trees); min-max, standard, robust and max-abs scaling compared on the same column; scaling the target |
| | deep dive | [Outliers and capped values](complementary/outliers.ipynb) | An error, a rare case or a different population; rules for finding them and why the usual one is fooled by the outliers themselves; capped values, which are not outliers; keeping, clipping, transforming or flagging |
| | deep dive | [Skewed distributions and the log transform](complementary/skewed_distributions.ipynb) | Long right tails and why they matter to some models and not to others; the logarithm, power and quantile transforms; taking the logarithm of the target, and what the model then predicts |
| | deep dive | [Scaling images](complementary/scaling_images.ipynb) | Why a table is scaled column by column and an image with one mean and deviation per colour channel; images flattened into rows |
| 4 | standard | [Where data preparation ends and modelling begins](where_preparation_ends.ipynb) | Steps that learn nothing from the data can be done once, for everyone, in the data pipeline (ETL); steps that learn from it must be fitted on the training data only, inside the model's pipeline; a leak demonstrated on a column of pure noise |
| | deep dive | [Kinds of features](complementary/kinds_of_features.ipynb) | What a row, a feature and a target are; numbers, categories (with and without an order), dates, text, identifiers; why the type pandas gives a column is not its kind; columns that must not be features |
| | deep dive | [Exploring a dataset](complementary/exploring_a_dataset.ipynb) | The questions to ask a new table and the summary or plot that answers each one; what may be looked at before the split and what only on the training set; writing the findings down as decisions |
| | deep dive | [Correlation and what it misses](complementary/correlation.ipynb) | Pearson's coefficient, computed by hand and as a matrix; relationships it can't see; Spearman's coefficient; a correlation that reverses inside each group |
| | deep dive | [Creating features](complementary/creating_features.ipynb) | Ratios, parts of a date, time elapsed, cyclic values, bins and products; features computed from each row alone, and features learned from the data |

Next: back to [Supervised learning, part 4](../supervised-learning/README.md#part-4--classification).
