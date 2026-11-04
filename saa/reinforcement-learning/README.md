# Reinforcement Learning: Q-learning

Learning from rewards instead of labels: an agent acts in an environment, receives rewards, and learns which action is worth taking in each situation.

## Path

★ marks the core items: the minimum, if your week is short.

| # | Notebook | Content |
| --- | --- | --- |
| ★ 1 | [Reinforcement learning and Q-learning](qlearning.ipynb) | Agent, environment, reward and policy; an intuitive view of Q-learning, trained from scratch on a small grid world |
| 2 | [The Bellman equation](bellman_equation.ipynb) | Where Q-learning's update rule comes from, computed by hand step by step and then in code |
| 3 | [Q-learning on FrozenLake](frozen_lake.ipynb) | Training and evaluating a Q-learning agent in a [Gymnasium](https://gymnasium.farama.org/) environment |

## Worked example

[Tic-tac-toe with Q-learning](https://github.com/avidaldo/tictactoe-qlearning) is a repository of its own: it improves an agent step by step, from the simplest version to one that never loses against a perfect player. Its README suggests further experiments, and its notebooks have exercises: board symmetries, a curriculum, a tournament.

## Practice

**Make the lake slippery.** In [Q-learning on FrozenLake](frozen_lake.ipynb), create the environment with `is_slippery=True`: each move now goes in the intended direction only one time in three, and slips to one side or the other otherwise.

1. Evaluate over 1,000 episodes instead of 100, and train three or four times, re-creating the Q-table before each run (otherwise training continues from the last table). How often does the agent reach the goal, and how much does that change from one run to the next?
2. No policy reaches the goal every time on this lake: the best possible one does it about 74% of the time within the 99-step limit. Change the learning rate, gamma and the number of episodes, first one at a time and then together, until every run gets close to 74%. Which changes matter, and why do they matter here when they didn't on the deterministic lake?
3. Look at the action your best agent chooses at the start state. Why that one?

A [solution](practice/slippery_lake_solution.ipynb), to read once you have tried.

## References

- Notebook 3 is adapted from Unit 2 of the [Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course/unit2/introduction) (Apache 2.0 licence), which goes on to deep Q-learning and policy-gradient methods.
- Richard S. Sutton and Andrew G. Barto, [*Reinforcement Learning: An Introduction*](http://incompleteideas.net/book/the-book-2nd.html), 2nd edition (2018), free online: the standard textbook. Chapter 6 introduces Q-learning.
