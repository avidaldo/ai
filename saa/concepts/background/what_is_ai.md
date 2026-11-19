# What is Artificial Intelligence? A Historical and Conceptual Introduction

## Defining Intelligence: The Quest to Emulate the Human Mind

Artificial Intelligence (AI) is a broad and ambitious field of computer science dedicated to creating systems capable of performing tasks that typically require human intelligence. These tasks include reasoning, learning, problem-solving, perception, understanding language, and even creativity.

Some researchers aim at machines that think, learn and adapt as well as people do, or better. Most AI work has narrower goals: a system that does one task, such as recognising speech or recommending a film, well enough to be useful.

### The Turing Test: A Benchmark for Intelligence

In 1950, Alan Turing proposed a simple but powerful test to measure a machine's ability to exhibit intelligent behaviour equivalent to, or indistinguishable from, that of a human. In the **Turing Test**, a human evaluator engages in a natural language conversation with both a human and a machine. If the evaluator cannot reliably tell the machine from the human, the machine is said to have passed the test.

In 2025, a study at UC San Diego ran the three-party test with five-minute text conversations: GPT-4.5, told to play a human persona, was judged to be the human 73% of the time, more often than the real people ([Jones and Bergen, 2025](https://arxiv.org/abs/2503.23674)). The result says more about the test than about intelligence: it measures how convincingly a system imitates a person in conversation, not whether it understands or reasons.


## A Brief History of AI

The dream of creating artificial beings is ancient, but the scientific journey of AI began in the mid-20th century.

- **1956: The Dartmouth Workshop - The Birth of a Field**: John McCarthy coined the term "Artificial Intelligence" in the 1955 proposal for a summer workshop at Dartmouth College, held in 1956. The workshop brought together the founders of the field and laid out its vision. The initial optimism was immense, with pioneers predicting that machines with human-level intelligence were just a few decades away.

- **1956–1980s: Symbolic AI**: For its first decades, AI meant programs that reason with knowledge written by people: searching through possibilities, applying rules and drawing logical conclusions. In the 1980s, **expert systems** turned this into products, with knowledge bases of hundreds or thousands of if-then rules written with human experts. The [classical AI deep dive](../complementary/classical-ai/README.md) builds a small example of each of these ideas.

- **The "AI Winters": Cycles of Hype and Disillusionment**: The history of AI has been marked by periods of intense funding and excitement ("AI summers") followed by "AI winters," where progress stalled and funding dried up: the first in the mid-1970s, the second from the late 1980s, when the expert-systems market collapsed. These cycles were often caused by:
    - **Overblown Promises**: Early researchers underestimated the profound difficulty of tasks like computer vision and natural language understanding.
    - **Computational Limits**: The hardware of the time was insufficient to handle the complexity of the proposed models.
    - **The Combinatorial Explosion**: Many early AI approaches were based on exploring vast search spaces of possibilities, which quickly became computationally intractable.

- **2012-Present: The Deep Learning Revolution**: The current "AI summer" was ignited by the convergence of three key factors:
    1.  **Big Data**: The availability of massive datasets to train complex models.
    2.  **Powerful Hardware**: The rise of GPUs (Graphics Processing Units) provided the parallel computing power needed for deep learning.
    3.  **Algorithmic Improvements**: Backpropagation, the method that trains neural networks, dates from the 1980s; what changed around 2012 were practical improvements such as the ReLU activation and dropout, which let much deeper networks train well. AlexNet, a deep convolutional network trained on GPUs, won the ImageNet image-recognition competition of 2012 by a wide margin.

- **2017-Present: Generative AI**: The **transformer** architecture (2017) made it possible to train language models on enormous amounts of text. Scaled up and then trained to follow instructions, they became the chat assistants that reached the public with ChatGPT in November 2022, and the same ideas now generate images, audio and code.

Machine learning had already displaced rule-based systems for most problems from the 1990s; deep learning made it dominant, with systems that learn directly from data.

## Machine Learning vs. Artificial Intelligence

While often used interchangeably, **Machine Learning (ML)** is a subfield of AI that is easier to define. It focuses on building systems that can **learn from data**, identify patterns, and make decisions with minimal human intervention.

<img src="img/ai_hierarchy.png" width="200" style="margin: 20px;">

Instead of being explicitly programmed with rules to solve a problem, a machine learning model is **fitted to data**: a learning algorithm adjusts the model's parameters until it captures the patterns that link inputs to outputs. More and better data usually gives a better model, up to the limits of the model itself and of the data's quality.

A couple of classic definitions are:

> [Machine learning is the] field of study that gives computers the ability to learn without being explicitly programmed.
>
> — Usually attributed to Arthur Samuel, who popularised the term *machine learning* in 1959; the sentence is a later paraphrase of his work

> A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P if its performance at tasks in T, as measured by P, improves with experience E.
>
> — Tom Mitchell, 1997

### Deep Learning

**Deep Learning** is a specialised subfield of machine learning that uses **artificial neural networks** with many layers (hence "deep"). By leveraging deep architectures, these models can learn complex, hierarchical patterns from vast amounts of data. This has led to breakthroughs in fields like computer vision and natural language processing.

## The Spectrum of AI: From Narrow to General Intelligence

AI systems are often classified by how **general** their abilities are. A different distinction, between **weak** and **strong** AI, is about whether a machine has a mind; the two are often mixed up.

### Narrow AI

**Artificial Narrow Intelligence (ANI)** refers to AI systems designed and trained to perform a **specific, well-defined task**. This is the form of AI that surrounds us today.

- **Characteristics**:
    - **Task-Specific**: Excels at one job (e.g., playing chess, recognising faces, filtering spam), and can't transfer what it does to another.
    - **Data-Driven**: In machine learning systems, performance depends directly on the quality and quantity of the training data.

- **Examples**:
    - **Recommendation Engines**: Algorithms on Netflix or Amazon that suggest content based on your viewing history.
    - **Spam filters and face recognition**: one task each, often done better than people do it.
    - **Self-Driving Cars**: Highly complex systems, but still focused on the task of driving.

### General AI (AGI)

**Artificial General Intelligence (AGI)** is the hypothetical intelligence of a machine that can understand, learn and apply its intelligence to **any intellectual task that a human being can**: reasoning, planning, learning from experience, and transferring what it knows from one domain to another without being reprogrammed.

Large language models blur the line. One model writes, translates, summarises, answers questions and programs, so it is far more general than a spam filter; but it still fails at tasks a person finds easy, and whether today's models are a step towards AGI is an open, much-debated question. By most definitions, **AGI does not exist yet**.

### Weak and Strong AI

The philosopher John Searle (1980) distinguished **weak AI**, machines that *simulate* thinking, from **strong AI**, the claim that a suitably programmed machine would really *have* a mind and understand. His *Chinese room* argument holds that running a program, however well it imitates understanding, is not enough for understanding. The question is about minds, not abilities, which is why narrow/general and weak/strong are better kept apart.

### Artificial Superintelligence (ASI)

**Artificial Superintelligence (ASI)** is a hypothetical form of AI that surpasses human intelligence in virtually every domain, including scientific creativity, general wisdom, and social skills. The development of ASI raises profound ethical and existential questions for the future of humanity.

