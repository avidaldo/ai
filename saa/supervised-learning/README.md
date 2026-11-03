# Supervised Learning

Learning from labelled examples: regression and classification with the classic algorithms, and how to tell whether a model will work on data it has not seen. Evaluation is not a final step here; it is taught alongside the models from the start.

## How this folder is organised

The notebooks are grouped by what they teach, so that each idea is explained in one place:

| Folder | What it teaches |
| --- | --- |
| [`algorithms/`](algorithms/) | How each model learns and predicts, for regression and for classification where it does both: [linear models](algorithms/linear-models/), [tree-based models](algorithms/tree-based/), [neighbours](algorithms/neighbours/) |
| [`ml-fundamentals/`](ml-fundamentals/) | The ideas that every model shares, whatever its algorithm: how it is fitted by minimising an error (gradient descent); on which data it is judged, and why (overfitting, the train/test split, validation, cross-validation, leakage); controlling complexity |
| [`evaluation/`](evaluation/) | What we measure and how we read the errors: regression errors, classifier metrics, rare classes, error analysis |
| [`basic-workflows/`](basic-workflows/) | Small end-to-end examples on different datasets. They apply the other folders without explaining them again, and link to where each step is explained |

The path below crosses the folders in the order the ideas are needed; follow it rather than the folders.

## Path

★ marks the core items: the minimum, if your week is short. A section whose heading ends in *(deep dive)* is optional, like the deep dives below, and never asked.

### Part 1 · Regression, end to end

| # | Notebook | Content |
| --- | --- | --- |
| ★ 1 | [Linear regression](algorithms/linear-models/linear_regression.ipynb) | A first model: fitting a line by minimising an error, prediction, multiple regression |
| ★ 2 | [Decision trees](algorithms/tree-based/decision_trees.ipynb) | Trees for classification and regression; a model flexible enough to fit its training data too well |
| ★ 3 | [Overfitting and the train/test split](ml-fundamentals/overfitting_and_the_split.ipynb) | Why a model must be judged on data it did not see; underfitting and overfitting; random and stratified splits; the test set stands for the data the model will meet in production |
| ★ 4 | [California housing, step by step](basic-workflows/california_by_hand.ipynb) | A first complete workflow, each step written by hand: split, scale, train, predict, evaluate; estimators, transformers and predictors |
| 5 | [Random forests](algorithms/tree-based/random_forests.ipynb) | Ensembles: averaging many trees that each see different data |
| ★ 6 | [Gradient boosting](algorithms/tree-based/gradient_boosting.ipynb) | Trees added one at a time, each correcting the errors of the ones before; learning rate and number of trees; why it is the usual first strong model on a table |
| ★ 7 | [XGBoost](algorithms/tree-based/xgboost.ipynb) | The library most teams use for gradient boosting: a regularised objective, missing values handled natively, early stopping on a validation set; LightGBM and CatBoost |
| ★ 8 | [Measuring a regression model's error](evaluation/regression_metrics.ipynb) | MAE, RMSE, R², percentage errors (MAPE) and the share of predictions within 10%; a baseline to compare with; which measure answers which question |

Then, on real data: ★ [Splitting by time](https://github.com/avidaldo/king-county/blob/master/03-temporal_leakage.ipynb), in the King County worked example. On house sales that span a year and a half, a random split lets the model learn from sales later than the ones it is tested on; splitting by date measures what it will really do.

### Part 2 · Neighbours and errors

| # | Notebook | Content |
| --- | --- | --- |
| ★ 9 | [k-nearest neighbours](algorithms/neighbours/knn.ipynb) | A model that stores examples instead of learning parameters, and predicts from the most similar ones; why scaling matters; choosing *k* |
| ★ 10 | [Error analysis: where a model fails](evaluation/error_analysis.ipynb) | Looking at errors instead of their average: by group, on a map, over time, in each direction; turning what you find into the next feature or model |

### Part 3 · Choosing a model honestly

| # | Notebook | Content |
| --- | --- | --- |
| ★ 11 | [Validation and model selection](ml-fundamentals/validation_and_model_selection.ipynb) | Why choosing on the test set is a leak; a three-way split; comparing models on the validation set and testing once |
| ★ 12 | [California housing with pipelines](basic-workflows/california_with_pipelines.ipynb) | The workflow of 4 on the raw data, as a pipeline: `Pipeline`, `ColumnTransformer`, `FunctionTransformer`; preprocessing fitted on the training data only; four models compared on a validation set |
| 13 | [Controlling complexity: regularisation](ml-fundamentals/regularization.ipynb) | Tree depth, *k* and a penalty as the same kind of setting; Ridge (L2) and Lasso (L1) against an overfitted curve |
| ★ 14 | [Cross-validation and hyperparameter search](ml-fundamentals/cross_validation_and_search.ipynb) | k-fold and time-ordered cross-validation; grid and random search; why the final test is still run once |
| ★ 15 | [Data leakage](ml-fundamentals/data_leakage.ipynb) | Four short demonstrations of a better score for a worse evaluation: preprocessing before the split, a feature that contains the target, the same example on both sides, information from the future |

Then, the path of [Data preparation](../data-preparation/README.md#path): four notebooks on missing values, encoding categories, scaling, and where data preparation ends and modelling begins, each step inside the pipelines of this part.

And if you have the time: [California housing, end to end](https://github.com/avidaldo/california_e2e), a complete project that goes through parts 1 and 3 on one dataset ([Worked examples](#worked-examples) says how it relates to the two California notebooks above).

### Part 4 · Classification

| # | Notebook | Content |
| --- | --- | --- |
| ★ 16 | [Gradient descent](ml-fundamentals/gradient_descent.ipynb) | Fitting a model by walking downhill on its error: the learning rate, why scaling matters, batch, stochastic and mini-batch steps; checked against the exact answer of linear regression, then needed for logistic regression, which has none, and for every neural network |
| ★ 17 | [Logistic regression](algorithms/linear-models/logistic_regression.ipynb) | Classification as a probability: the sigmoid, one and several variables, the decision boundary, more than two classes |
| ★ 18 | [Evaluating a classifier](evaluation/classification_metrics.ipynb) | Accuracy, precision, recall, F1, the confusion matrix, ROC and AUC; choosing a metric |
| 19 | [When one class is rare](evaluation/imbalanced_classes.ipynb) | Regions of mammograms, 2% of them with a calcification: the accuracy that a model predicting "no" always gets, a baseline, precision–recall curves, moving the threshold, class weights |
| 20 | [Pima diabetes](basic-workflows/pima_diabetes.ipynb) | A classification workflow on real data: zeros that stand for missing values, filled inside the pipeline; a threshold chosen for screening; why a dataset must be read before a pipeline is written |

Then, on real data: [Thyroid disease](https://github.com/avidaldo/thyroid), a worked example of classification with three imbalanced classes: metrics, baselines and boosting.

## Worked examples

Longer projects that apply this topic to real data, each in a repository of its own. The path above says when to read each one.

- [King County house sales](https://github.com/avidaldo/king-county): duplicates and temporal leakage. Its notebook on splitting by time is core, after part 1; the rest of the repository is optional, and the notebook to come back to for any data that changes over time.
- [California housing](https://github.com/avidaldo/california_e2e): an end-to-end regression project, from framing the problem to a tuned model, optional. It uses the same 20,640 districts as the two California notebooks of the path, in the version of [California housing with pipelines](basic-workflows/california_with_pipelines.ipynb), which keeps the counts of each district and a text column, with some values missing. Those two notebooks rehearse its steps on a small scale, each step explained in this folder; the repository is the whole project, and its `notes/` folder explains every step again, so that it can be read without this folder.
- [Thyroid disease](https://github.com/avidaldo/thyroid): classification with imbalanced classes, metrics, baselines and boosting, after part 4.

## Practice

Optional, and never graded.

**Does it survive a shift?** Train a classifier, such as [k-nearest neighbours](algorithms/neighbours/knn.ipynb) or [logistic regression](algorithms/linear-models/logistic_regression.ipynb), on 10,000 flattened MNIST training images. Measure its accuracy on the test set, and then on the same test images shifted 3 pixels with the `shift_image` you wrote in [numpy-mnist](https://github.com/avidaldo/numpy-mnist). Train again with shifted copies added to the training set, and measure again. What does the gap say about test sets and real conditions?

## Deep dives

Optional and never assessed. The path never depends on these.

| Deep dive | Extends | Content |
| --- | --- | --- |
| [Ensembles beyond trees](algorithms/tree-based/deep-dives/ensembles_beyond_trees.ipynb) | 5, 6 | Voting, stacking, and bagging any model, on the validation set of part 3: best read after it |
| [Uniform and distance weights](algorithms/neighbours/deep-dives/knn_weights.ipynb) | 9 | How weighting the neighbours by their distance changes the decision boundary, and why it makes the training accuracy meaningless |
| [Naive Bayes, from the theorem to a spam filter](deep-dives/naive-bayes/README.md) | 17 | A classifier that learns by counting, of the same form as logistic regression, in three notebooks: Bayes' theorem on one word, counted by hand; a naive Bayes classifier written in a few lines, identical to scikit-learn's; a spam filter compared with logistic regression, with a threshold for what each mistake costs |
| [A classifier in depth (MNIST)](evaluation/deep-dives/mnist_classifier_in_depth.ipynb) | 18 | A digit detector trained by stochastic gradient descent, measured with cross-validation; one classifier for ten classes: one-vs-rest against one-vs-one |
| [Support vector machines](deep-dives/svm.ipynb) | 9, 17 | The widest margin between classes, support vectors, soft margins and `C`; kernels for boundaries that aren't straight; SVMs for regression |
| [Diabetes progression](basic-workflows/deep-dives/diabetes_progression.ipynb) | 12, 14 | A regression workflow on scikit-learn's diabetes data: what the documentation says about features that arrive already scaled |
| [Iris: a multiclass workflow](basic-workflows/deep-dives/iris_multiclass.ipynb) | 17, 18 | A classification workflow with three classes: four classifiers compared by cross-validation, the chosen one tested once; the confusion matrix and report for three classes; what a small, easy dataset can't show |
| scikit-learn from scratch *(coming)* | 12 | Build a small copy of scikit-learn, one design principle at a time, to see why its API looks the way it does: estimators, transformers, `get_params` and `clone`, `Pipeline`, grid search |

## Related topics

- [Data preparation](../data-preparation/README.md): its path, after part 3, covers missing values, encoding, scaling, and where data preparation ends and modelling begins; its deep dives go further, one notebook per step (kinds of features, exploring, correlation, outliers, skewed distributions, new features); the basic workflows link the step they apply
