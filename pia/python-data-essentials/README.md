# Python Data Essentials: NumPy and pandas

The two libraries that almost every AI project in Python stands on: NumPy for numerical arrays and pandas for tables. This folder covers what you need to load, inspect, select, reshape and combine the data of your projects.

## Path

★ marks the core items: the minimum, if your week is short.

| # | Notebook | Content |
| --- | --- | --- |
| ★ 1 | [NumPy](numpy/numpy1.ipynb) | Arrays and their data types, creating arrays, indexing and slicing, reshaping, random numbers |
| 2 | [NumPy for algebraic operations](numpy/numpy2_algebra.ipynb) | Identity and transpose matrices, matrix operations, `@` and `np.dot` |
| ★ 3 | [pandas: Series and DataFrame](pandas/pandas_structures.ipynb) | The two pandas structures and how they relate to NumPy arrays |
| ★ 4 | [DataFrame operations](pandas/pandas_dataframe_op.ipynb) | Managing columns and rows, selecting and slicing, filtering, sorting, basic aggregations |
| ★ 5 | [DataFrame transformations and reshaping](pandas/pandas_transformations.ipynb) | `map`, `apply` and `transform`, grouping, `assign`, reshaping with `melt` and `pivot` |

## Exercises

[numpy-mnist](https://github.com/avidaldo/numpy-mnist), the repository you forked in stage 1: two dozen exercises on handwritten digits as a 60,000×28×28 array, with tests that check your answers. If a 7×7 image as a matrix is new to you, start with [Matrices and tensors in AI](https://github.com/avidaldo/compare-python-c-efficiency/blob/main/02_matrices_in_ai.ipynb) (complementary: support).

## Complementary

Optional and never assessed: **support** reinforces the basics, and a **deep dive** goes further. The path never depends on these.

| Item | Kind | Extends | Content |
| --- | --- | --- | --- |
| [Lists vs NumPy arrays: exercises](numpy/complementary/lists_nd_arrays_examples.ipynb) | support | 1 | Small functions solved with plain lists and with NumPy |
| [Fancy indexing, step by step](numpy/complementary/fancy_indexing_step_by_step.ipynb) | support | 1 | Indexing with arrays of indices, and broadcasting, on arrays small enough to print, up to three index arrays that cut a different window from each image |
| [A DataFrame from different structures](pandas/complementary/df_from_structures.ipynb) | support | 3 | Building one DataFrame from lists, dictionaries and arrays |
| [Shifting every image without a loop](https://github.com/avidaldo/numpy-mnist/blob/main/vectorised_shift.ipynb), in numpy-mnist | deep dive | Exercises | Exercise 22's shift vectorised, checked against the loop and timed part by part |
| [Data preparation's complementary notebooks](../../saa/data-preparation/README.md#complementary) | deep dive | 3–5 | One step of preparing data for a model per notebook: exploring a dataset, correlation, outliers, skewed distributions… The path of Data preparation comes later, with supervised learning |

## References

- [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [pandas cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) (official)
