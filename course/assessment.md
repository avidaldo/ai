# How You Are Assessed

SAA and PIA each give their own grade, and both are assessed the same way: **your grade comes from in-person exams**, and accepted contributions to the course repositories can add up to 2 points.

## The exams

| Exam | SAA | PIA | What it covers |
| --- | --- | --- | --- |
| February | Tue 2 Feb | Thu 4 Feb | Term 1 (stages 1–7). **It is the rehearsal for May:** compulsory and graded, and it can raise your grade (below) |
| May | Mon 24 May | Wed 26 May | **The whole year.** It gives your grade |
| June | Thu 10 Jun | Mon 14 Jun | The same as May, as a second chance: the better result counts |

The two topics that start term 2 in the week of the February exams (neural networks part 1, and tool calling) are not in the February exam.

The exams run in person, without network and without any AI tool: not even a local model may be installed in your account. You can use any material on the computer, including the class material. Each exam has two parts with the same weight:

| Part | What it asks |
| --- | --- |
| 1. Quiz | Multiple-choice questions on Moodle, on every stage the exam covers, including those without project work: concepts; cases (a described problem: which approach, which split, which metric); numbers (read a confusion matrix, estimate a cost or a reliability); and design choices (which architecture fits a budget, which test would catch a bug, which instruction to an AI agent is better) |
| 2. The projects | Written answers on repositories you have worked on during the year, installed offline, with a change made for that sitting (a planted bug, a new requirement, another dataset, a different target): predict the effect of a change, then run the code to check it; diagnose a problem; write the instructions you would give an AI agent for a change, and the test that would show it is done; critique the evaluation. You will not be asked to write code from scratch |

## Your grade

Each exam, February, May and June, is the mean of its two parts:

$$E = \frac{\text{quiz} + \text{projects}}{2}$$

Each part must reach 4: with a part below 4, the exam counts at most 4. An exam you don't sit counts 0.

May gives your grade, and February can raise it, never lower it: May counts on its own or averaged with February, whichever is higher. June works the same way, as a second chance:

$$G_\text{May} = \max\left(E_\text{May},\ \frac{E_\text{Feb} + E_\text{May}}{2}\right) \qquad G_\text{June} = \max\left(E_\text{June},\ \frac{E_\text{Feb} + E_\text{June}}{2}\right)$$

The average with February counts only when both parts of that exam reach 4; otherwise its $G$ is its $E$, at most 4.

The better of May and June counts, and you pass with a 5. Once you have passed, accepted contributions add $C$, from 0 to 2 points ([below](#contributions)), never above 10:

$$\text{grade} = \min\left(10,\ \max(G_\text{May},\ G_\text{June}) + C\right)$$

The grade is rounded to the nearest whole number, halves up; a grade below 5 is never rounded up to a pass.

## The projects

The practical part of each exam works on some of [the projects](../README.md#the-projects), and possibly on the worked examples. It asks you to work on their code, so the best preparation is to have built them, or at least to have followed them closely. **Which repositories, and the version (tag) of each to study, are announced at least two weeks before the exam.** Each version is the repository as it stood a week before the exam or earlier: only what had been published by then is examined, never the complementary material in a repository's `docs/`. The questions are about a change you haven't seen, so reciting the code won't help; understanding it will. Everything runs offline, without a language model.

**You are expected to use AI tools.** What is assessed is your understanding: AI tools can write most of the code for you, but they can't understand it for you, and that is what the exam checks. Make sure you can explain, test and change the projects' code, and that you could direct an AI agent to change it well.

## Contributions

Contributions are voluntary, and you can get a 10 without them. Useful issues (a problem well identified, even without a fix) and pull requests to any course repository, once accepted, can add up to 2 points to the grade of a module whose exam you have passed, never above 10. How they are valued is described in the programación. Register your GitHub username in the aula virtual so that they can be counted. How to take part: [Improving the course materials](../CONTRIBUTING.md).

## What each kind of material counts for

- **Core items** (★ in each topic's README) are the minimum path. The project part of each exam needs only them and the repositories it uses, and about two thirds of the quiz is about them; the rest of the quiz is about the **standard** items: the rest of the path and the worked examples.
- **Deep dives** are never assessed.
- **Worked examples** (the repositories that apply each stage to real data) are studied, and the quiz can ask about them. Some topics, such as classification, are practised only there.
- **Practice tasks** (suggested by the topics and the worked examples) are never graded. They are the best preparation for the exam, and you can ask for feedback on any of them.
