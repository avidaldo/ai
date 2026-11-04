# Bayes' Theorem

Bayes' theorem says how to update the probability of a hypothesis when new evidence arrives.

## The Theorem

For a hypothesis A and evidence B, with P(B) > 0:

$$ P(A|B) = \frac{P(B|A) \times P(A)}{P(B)} $$

Each term has a name:

- **P(A)**, the **prior**: how probable the hypothesis was before the evidence.
- **P(B|A)**, the **likelihood**: how probable the evidence is if the hypothesis is true.
- **P(B)**, the **evidence**: how probable the evidence is overall, whether the hypothesis is true or not. The [law of total probability](probability.md#the-law-of-total-probability) computes it as P(B|A) × P(A) + P(B|¬A) × P(¬A).
- **P(A|B)**, the **posterior**: how probable the hypothesis is after the evidence.

In words: the posterior is the prior multiplied by P(B|A) / P(B), how many times more probable the evidence is if the hypothesis is true than it is overall. Evidence that is much more likely under the hypothesis raises its probability; evidence that is just as likely either way leaves it unchanged.

## Where It Comes From

The theorem follows in two lines from the definition of [conditional probability](probability.md#conditional-probability). The probability that both A and B happen can be written in two ways:

$$ P(A \cap B) = P(A|B) \times P(B) \qquad P(A \cap B) = P(B|A) \times P(A) $$

Both right-hand sides are equal, so dividing by P(B):

$$ P(A|B) \times P(B) = P(B|A) \times P(A) \quad\Rightarrow\quad P(A|B) = \frac{P(B|A) \times P(A)}{P(B)} $$

A worked example with numbers: [a diagnostic test](diagnostic_test.md).

## Bayes' Theorem in Artificial Intelligence

The theorem is the basis of two ideas in AI, which differ in where the probabilities come from:

- **Bayesian networks** reason with probabilities that an expert writes down, and update them with the theorem as evidence arrives: for example, the probability of a burglary when an alarm goes off. A complete example: [reasoning under uncertainty](../classical-ai/uncertainty.ipynb).
- The **naive Bayes** classifier estimates those probabilities by counting in labelled data, so it is supervised learning. Its classic application is the spam filter: the probability that an email is spam given the words it contains. It is [a deep dive of supervised learning](../../../supervised-learning/deep-dives/naive-bayes/README.md).

## Further Resources

- [3Blue1Brown: Bayes' theorem, the geometry of changing beliefs](https://www.youtube.com/watch?v=HZGCoVF3YvM)
- [Jesús Conde: probability theory and Bayes' theorem for machine learning](https://www.youtube.com/watch?v=foBVe1MuT5s) (in Spanish)
- [Matemáticas profe Alex: Bayes' theorem](https://www.youtube.com/watch?v=bDfCURXoKkU&list=PLeySRPnY35dH7Pnamtm2xxaCuT6jxt1vn&index=28) (in Spanish)
