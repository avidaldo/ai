# Supervised Learning

Learning from labelled examples: regression and classification with the classic algorithms, and how to tell whether a model will work on data it has not seen. Evaluation is not a final step here; it is taught alongside the models from the start.

The notebooks are grouped by what they teach: `algorithms/` (how each model learns), `ml-fundamentals/` (what every model shares: fitting, judging, controlling complexity), `evaluation/` (metrics and errors) and `basic-workflows/` (small end-to-end examples). The path crosses the folders in the order the ideas are needed: follow it rather than the folders.

## Path

★ marks the core items: the minimum, if your week is short. A section whose heading ends in *(deep dive)* is optional, like the deep dives below, and never asked.

### Part 1 · Regression, end to end

| # | Notebook | Content |
| --- | --- | --- |
| ★ 1 | [Linear regression](algorithms/linear-models/linear_regression.ipynb) | A first model: fitting a line by minimising an error, prediction, multiple regression |
| ★ 2 | [Decision trees](algorithms/tree-based/decision_trees.ipynb) | Trees for classification and regression; a model flexible enough to fit its training data too well |
| ★ 3 | [Overfitting and the train/test split](ml-fundamentals/overfitting_and_the_split.ipynb) | Why a model must be judged on data it did not see; underfitting and overfitting; random and stratified splits; the test set stands for the data the model will meet in production |
| ★ 4 | [California housing, step by step](basic-workflows/california_by_hand.ipynb) | A first complete workflow, each step written by hand: split, scale, train, predict, evaluate; estimators, transformers and predictors |
| ★ 5 | [Random forests](algorithms/tree-based/random_forests.ipynb) | Ensembles: averaging many trees that each see different data |
| ★ 6 | [Gradient boosting](algorithms/tree-based/gradient_boosting.ipynb) | Trees added one at a time, each correcting the errors of the ones before; learning rate and number of trees; why it is the usual first strong model on a table |
| ★ 7 | [XGBoost](algorithms/tree-based/xgboost.ipynb) | The library most teams use for gradient boosting: a regularised objective, missing values handled natively, early stopping on a validation set; LightGBM and CatBoost |
| ★ 8 | [Measuring a regression model's error](evaluation/regression_metrics.ipynb) | MAE, RMSE, R², percentage errors (MAPE) and the share of predictions within 10%; a baseline to compare with; which measure answers which question |

Then, on real data: ★ [Splitting by time](https://github.com/avidaldo/king-county/blob/master/03-temporal_leakage.ipynb), in the King County worked example. On house sales that span a year and a half, a random split lets the model learn from sales later than the ones it is tested on; splitting by date measures what it will really do. The rest of [that repository](https://github.com/avidaldo/king-county) is optional.

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

And if you have the time: [California housing, end to end](https://github.com/avidaldo/california_e2e), a complete project on the districts of notebooks 4 and 12, from framing the problem to a tuned model. Its `notes/` folder explains every step again, so it can be read on its own.

### Part 4 · Classification

| # | Notebook | Content |
| --- | --- | --- |
| ★ 16 | [Gradient descent](ml-fundamentals/gradient_descent.ipynb) | Fitting a model by walking downhill on its error: the learning rate, why scaling matters, batch, stochastic and mini-batch steps; the idea behind fitting logistic regression and every neural network, which have no exact answer |
| ★ 17 | [Logistic regression](algorithms/linear-models/logistic_regression.ipynb) | Classification as a probability: the sigmoid, one and several variables, the decision boundary, more than two classes |
| ★ 18 | [Evaluating a classifier](evaluation/classification_metrics.ipynb) | Accuracy, precision, recall, F1, the confusion matrix, ROC and AUC; choosing a metric |
| 19 | [When one class is rare](evaluation/imbalanced_classes.ipynb) | Regions of mammograms, 2% of them with a calcification: the accuracy that a model predicting "no" always gets, a baseline, precision–recall curves, moving the threshold, class weights |
| 20 | [Pima diabetes](basic-workflows/pima_diabetes.ipynb) | A classification workflow on real data: zeros that stand for missing values, filled inside the pipeline; a threshold chosen for screening; why a dataset must be read before a pipeline is written |

Then, on real data: [Thyroid disease](https://github.com/avidaldo/thyroid), a worked example of classification with three imbalanced classes: metrics, baselines and boosting.

## Worked examples

Longer projects that apply this topic to real data, each in a repository of its own. The path above says when to read each one.

- [California housing](https://github.com/avidaldo/california_e2e): an end-to-end regression project, from framing the problem to a tuned model, optional. It uses the same 20,640 districts as the two California notebooks.
- [King County house sales](https://github.com/avidaldo/king-county): duplicates and temporal leakage.
- [Thyroid disease](https://github.com/avidaldo/thyroid): classification with imbalanced classes, metrics, baselines and boosting.

## Practice

Optional, and never graded.

**Does it survive a shift?** Train a classifier, such as [k-nearest neighbours](algorithms/neighbours/knn.ipynb) or [logistic regression](algorithms/linear-models/logistic_regression.ipynb), on 10,000 flattened MNIST training images. Measure its accuracy on the test set, and then on the same test images shifted 3 pixels with the `shift_image` you wrote in [numpy-mnist](https://github.com/avidaldo/numpy-mnist). Train again with shifted copies added to the training set, and measure again. How far can you trust that last number, and what does the gap say about test sets and real conditions?

A [solution](practice/shift_solution.ipynb), to read once you have tried.

## Deep dives

Optional and never assessed. The path never depends on these.

| Deep dive | Extends | Content |
| --- | --- | --- |
| [Ensembles beyond trees](algorithms/tree-based/deep-dives/ensembles_beyond_trees.ipynb) | 5, 6 | Voting, stacking, and bagging any model, on the validation set of part 3: best read after it |
| [Uniform and distance weights](algorithms/neighbours/deep-dives/knn_weights.ipynb) | 9 | How weighting the neighbours by their distance changes the decision boundary, and why it makes the training accuracy meaningless |
| [Naive Bayes, from the theorem to a spam filter](deep-dives/naive-bayes/README.md) | 17 | A classifier that learns by counting, in three notebooks: Bayes' theorem on one word; a classifier written by hand, identical to scikit-learn's; a spam filter compared with logistic regression |
| [A classifier in depth (MNIST)](evaluation/deep-dives/mnist_classifier_in_depth.ipynb) | 18 | A digit detector trained by stochastic gradient descent, measured with cross-validation; one classifier for ten classes: one-vs-rest against one-vs-one |
| [Support vector machines](deep-dives/svm.ipynb) | 9, 17 | The widest margin between classes, support vectors, soft margins and `C`; kernels for boundaries that aren't straight; SVMs for regression |
| [Diabetes progression](basic-workflows/deep-dives/diabetes_progression.ipynb) | 12, 14 | A regression workflow on scikit-learn's diabetes data: what the documentation says about features that arrive already scaled |
| [Iris: a multiclass workflow](basic-workflows/deep-dives/iris_multiclass.ipynb) | 17, 18 | A classification workflow with three classes: four classifiers compared by cross-validation, the chosen one tested once; the confusion matrix and report for three classes; what a small, easy dataset can't show |
| scikit-learn from scratch *(coming)* | 12 | Build a small copy of scikit-learn, one design principle at a time, to see why its API looks the way it does: estimators, transformers, `get_params` and `clone`, `Pipeline`, grid search |
