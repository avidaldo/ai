# Python Data Essentials: NumPy and pandas

The two libraries that almost every AI project in Python stands on: NumPy for numerical arrays and pandas for tables. This folder covers what you need to load, inspect, select, reshape and combine the data of your projects, to find the problems a table has, and to get data from the web.

## Path

★ marks the core items: the minimum, if your week is short.

| # | Notebook | Content |
| --- | --- | --- |
| ★ 1 | [NumPy](numpy/numpy1.ipynb) | Arrays and their data types, creating arrays, indexing and slicing, reshaping, random numbers |
| 2 | [NumPy for algebraic operations](numpy/numpy2_algebra.ipynb) | Identity and transpose matrices, matrix operations, `@` and `np.dot` |
| ★ 3 | [pandas: Series and DataFrame](pandas/pandas_structures.ipynb) | The two pandas structures and how they relate to NumPy arrays |
| ★ 4 | [DataFrame operations](pandas/pandas_dataframe_op.ipynb) | Managing columns and rows, selecting and slicing, filtering, sorting, basic aggregations |
| ★ 5 | [DataFrame transformations and reshaping](pandas/pandas_transformations.ipynb) | `map`, `apply` and `transform`, grouping, `assign`, reshaping with `melt` and `pivot` |
| ★ 6 | Finding the problems in a table *(coming)* | Missing values of two kinds (empty and placeholder), duplicates, impossible values, wrong types, the same thing written two ways; inspecting before deciding, and writing the decision down |
| ★ 7 | Text and dates *(coming)* | The `.str` methods, regular expressions for the common cases, accents and broken encodings, timestamps written in two formats, time zones |
| ★ 8 | Data from the web: APIs, JSON and XML *(coming)* | Calling a web API with parameters and pages, saving the raw answers, being polite to the server; JSON and JSON Lines into a DataFrame; reading XML with the standard library |

## Exercises

[numpy-mnist](https://github.com/avidaldo/numpy-mnist), the repository you forked in stage 1: two dozen exercises on handwritten digits as a 60,000×28×28 array, with tests that check your answers. If a 7×7 image as a matrix is new to you, start with [Matrices and tensors in AI](https://github.com/avidaldo/compare-python-c-efficiency/blob/main/02_matrices_in_ai.ipynb).

## Deep dives

Optional and never assessed. The path never depends on these.

| Notebook | Extends | Content |
| --- | --- | --- |
| [Lists vs NumPy arrays: exercises](numpy/deep-dives/lists_nd_arrays_examples.ipynb) | 1 | Small functions solved with plain lists and with NumPy |
| [A DataFrame from different structures](pandas/deep-dives/df_from_structures.ipynb) | 3 | Building one DataFrame from lists, dictionaries and arrays |
| [Data preparation's deep dives](../../saa/data-preparation/README.md#deep-dives) | 6 | One step of preparing data for a model per notebook: exploring a dataset, correlation, outliers, skewed distributions… The path of Data preparation comes later, with supervised learning |

## References

- [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [pandas cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) (official)
