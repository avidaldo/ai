# Python Data Essentials: NumPy and pandas

The two libraries that almost every AI project in Python stands on: NumPy for numerical arrays and pandas for tables. This folder covers what you need to load, inspect, select, reshape and combine the data of your projects.

## Path

| # | Tier | Item | Content |
| --- | --- | --- | --- |
| 1 | ★ core | [NumPy](numpy/numpy1.ipynb) | Arrays and their data types, creating arrays, indexing and slicing, reshaping, random numbers |
| | support | [Lists vs NumPy arrays: exercises](numpy/complementary/lists_nd_arrays_examples.ipynb) | Small functions solved with plain lists and with NumPy |
| 2 | standard | [NumPy for algebraic operations](numpy/numpy2_algebra.ipynb) | Identity and transpose matrices, matrix operations, `@` and `np.dot` |
| | support | [Matrices and tensors in AI](https://github.com/avidaldo/compare-python-c-efficiency/blob/main/02_matrices_in_ai.ipynb) | From single numbers to tensors; the dot product and matrix multiplication, and why AI is mostly that. Before the exercises, if a 7×7 image as a matrix is new to you |
| | project | [numpy-mnist](https://github.com/avidaldo/numpy-mnist), the repository you forked in stage 1 | Two dozen exercises on handwritten digits as a 60,000×28×28 array, with tests that check your answers |
| | support | [Fancy indexing, step by step](numpy/complementary/fancy_indexing_step_by_step.ipynb) | Indexing with arrays of indices, and broadcasting, on arrays small enough to print, up to three index arrays that cut a different window from each image |
| | deep dive | [Shifting every image without a loop](https://github.com/avidaldo/numpy-mnist/blob/main/vectorised_shift.ipynb), in numpy-mnist | Exercise 22's shift vectorised, checked against the loop and timed part by part |
| 3 | ★ core | [pandas: Series and DataFrame](pandas/pandas_structures.ipynb) | The two pandas structures and how they relate to NumPy arrays |
| | support | [A DataFrame from different structures](pandas/complementary/df_from_structures.ipynb) | Building one DataFrame from lists, dictionaries and arrays |
| 4 | ★ core | [DataFrame operations](pandas/pandas_dataframe_op.ipynb) | Managing columns and rows, selecting and slicing, filtering, sorting, basic aggregations |
| 5 | ★ core | [DataFrame transformations and reshaping](pandas/pandas_transformations.ipynb) | `map`, `apply` and `transform`, grouping, `assign`, reshaping with `melt` and `pivot` |
| | project | [Regulations assistant](https://github.com/avidaldo/fp-regulations-assistant), the project of PIA | Fork it and read its README. From the end of this stage, the group improves it step by step through the year, each step announced in the forum |
| | deep dive | The deep dives of [Data preparation](../../saa/data-preparation/README.md#path) | One step of preparing data for a model per notebook: exploring a dataset, correlation, outliers, skewed distributions…, each in that path after the step it extends. The path of Data preparation itself comes later, with supervised learning |

## References

- [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [pandas cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) (official)
