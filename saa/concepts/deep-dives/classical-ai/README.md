# Classical AI: Intelligence Without Learning

Machine learning is one way to make a program [intelligent](../../background/what_is_ai.md): show it examples with their answers, and let it find the rules. For its first decades, AI meant the opposite way: write the knowledge down, and make the program reason with it. That is **symbolic** or **classical AI**, sometimes called *good old-fashioned AI* (GOFAI), together with its probabilistic successor, reasoning under uncertainty. It isn't *classical machine learning*, a name often given to the learning methods that aren't neural networks, such as decision trees: those learn from data.

Nothing in these notebooks is trained on data, until the last one shows where learning comes in; case-based reasoning, in notebook 4, comes closest, by accumulating cases. Each builds a small example in plain Python, one idea per cell, with nothing to install beyond Python itself.

## Path

| # | Notebook | Content |
| --- | --- | --- |
| 1 | [Search](search.ipynb) | Breadth-first, depth-first, uniform-cost and A\* search on road maps; admissible heuristics; searching against an opponent |
| 2 | [Local search and optimisation](local_search.ipynb) | Hill climbing, random restarts, simulated annealing and a genetic algorithm on the eight-queens problem; the link with gradient descent |
| 3 | [Constraint satisfaction](constraint_satisfaction.ipynb) | Backtracking with the minimum-remaining-values heuristic, on a map and a Sudoku |
| 4 | [Rules and expert systems](rules_and_expert_systems.ipynb) | Forward and backward chaining; MYCIN and XCON; why expert systems faded, and where rules live today; case-based reasoning, solving from past cases instead of rules |
| 5 | [Knowledge representation](knowledge_representation.ipynb) | Semantic networks with inheritance and exceptions; frames, and their descendants, classes |
| 6 | [Logic](logic.ipynb) | Propositional logic and entailment by model checking, with answers that can be *unknown*; first-order rules in Prolog, and the same rules as a recursive SQL query |
| 7 | [Planning](planning.ipynb) | STRIPS: states and actions described by facts; the blocks world and the Sussman anomaly; planning at scale |
| 8 | [Reasoning under uncertainty](uncertainty.ipynb) | A Bayesian network by hand, inference by enumeration, explaining away; and the same tables learned from data |

**Games** are search against an opponent: notebook 1 explains minimax, and [Python tic-tac-toe](https://github.com/avidaldo/python-tic-tac-toe/tree/master/02_minimax) implements it, with a player that never loses.

## Not covered here

- **Fuzzy logic** (Lotfi Zadeh, 1965): truth as a degree between 0 and 1 instead of true or false, used in control systems such as washing machines and train brakes.
- **Symbolic language processing:** grammars and pattern-matching programs such as ELIZA (Joseph Weizenbaum, 1966), the first chatbot.
- **Image processing without learning:** filters, edges and thresholds, in the first part of [computer vision](https://github.com/avidaldo/computer-vision).
- **Decisions over time:** utilities and Markov decision processes, the foundation of reinforcement learning (stage 15).

## Is any of it still used?

More than the name *classical* suggests, but unevenly. Search and optimisation are everywhere: route planners run descendants of Dijkstra's algorithm and A\*, and timetables, delivery routes and production schedules come from constraint solvers and local search. Rules survive in business rule engines and in the guardrails around language models, but expert systems built by hand are rare: where data exists, machine learning does better and is cheaper to build. Logic lives on in type checkers, formal verification and recursive SQL queries, while Prolog itself is a niche language. Bayesian networks are still used in diagnosis and risk assessment, increasingly with probabilities learned from data. And the most capable systems mix both worlds: AlphaGo searched with learned evaluations, and agents built on language models plan, call tools and check their results with code.

Historically, symbolic AI dominated from the Dartmouth workshop of 1956 until the late 1980s, when expert systems proved costly to build and brittle in use; machine learning then took over the problems whose rules can't be written down, such as vision, speech and language.
