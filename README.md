# Artificial Intelligence 2026/27



Materials for two modules of the specialisation course in Artificial Intelligence and Big Data, taught together as one path:

- **SAA · Machine Learning Systems**: how models learn from data, how they are trained, and how to tell whether they really work.
- **PIA · AI Programming**: building software with AI: Python and its tooling, language models, retrieval, agents, deployment and automation.

## How to work

1. **Follow the [roadmap](#roadmap)** by its estimated dates, from stage 1, which sets up your tools. Each stage has a topic: open its README and work through its path in order. Run `git pull` to get each topic as it is published.
2. **Plan about 10 hours a week** for both modules, the weekly session included; they alternate in blocks. With less time, do the core items (★) first, and follow the projects, building them or reading, running and changing the teacher's solution; come back to the rest when you can. Unmarked items are the rest of the path, and the quiz asks about them too. Deep dives are optional and never assessed.
3. **Practise.** Reading and running is not enough: build the projects below, and try the practice tasks that some topics and worked examples suggest. Practice is never graded, and it is the best preparation for the exams.

## The projects

Public repositories that you fork and build on through the year, step by step. More may be added as the year goes.

| Project | Module | What you build | Starts |
| --- | --- | --- | --- |
| [numpy-mnist](https://github.com/avidaldo/numpy-mnist) | PIA | Images as NumPy arrays, with Git, tests and continuous integration. Keep your solutions: they come back later in the year | Fork it in stage 1, and solve its exercises in stage 4 |
| [Regulations assistant](https://github.com/avidaldo/fp-regulations-assistant) | PIA | An assistant that helps a teacher answer students' questions about vocational-training regulations, citing the articles in force | Stage 4 |
| [Property valuation](https://github.com/avidaldo/idealista18-avm) | SAA | An estimate of the price of a home from real listings, and of how far each estimate can be trusted | Stage 6 |

The two larger projects are built by the whole group, one step at a time:

- **Each step is an issue** in the project's repository, with the check that shows it is done. Ask your questions there.
- **Work in your fork**, and open a pull request that links the step's issue ([how](pia/setup/git_github.md#contributing-with-a-pull-request)). It is your submission: it receives feedback and is never graded, though once accepted it counts as a contribution.
- **The teacher's solution comes with the next issue**, with the good pull requests merged into it or instead of it. Bring it into your fork before you start the next step ([how](pia/setup/git_github.md#keeping-your-fork-up-to-date)).

The practical part of each exam works on these repositories.

## Roadmap

The year in fifteen stages. The last column estimates when the group works on each one: follow those dates rather than the stage numbers, since stages of the two modules overlap. **The dates are estimates, not deadlines.** Only the exams are fixed, in the bold rows: the other dates move with how the group progresses, each week's work is presented in the weekly session, and every change is made on this page. Materials are usually published well before they are needed, and you can always go ahead. If an exercise takes you longer, as numpy-mnist may if you are new to programming, finish it with your AI coding assistant, make sure you understand every line it writes, and move on with the group: the next stage doesn't wait.

Each stage belongs to one module: if you take only one, follow its rows, plus two of the other's. PIA's stage 5 needs SAA's note [Language models from the outside](saa/concepts/background/language_models.md), from stage 2, and PIA's stage 11 needs SAA's stage 10. Items marked *(coming)* are being written, and are linked when they are ready.

### Term 1

| # | Stage | Module | Topic | Worked examples | Estimated dates |
| ---: | --- | --- | --- | --- | --- |
| 1 | Getting started | PIA | [Setting up](pia/setup/README.md): your tools, your fork of numpy-mnist, and your GitHub username in the aula virtual | | 14–25 Oct |
| 2 | What AI and machine learning are | SAA | [The map of the year](saa/concepts/README.md): each family of models, seen from the outside | | 19–25 Oct |
| 3 | Python for AI | PIA | [Why Python rules AI](pia/setup/why_python.md), although it is slow | [Tic-tac-toe](https://github.com/avidaldo/python-tic-tac-toe), on program structure, recommended | 19 Oct – 1 Nov |
| 4 | Working with data | PIA | [Python data essentials](pia/python-data-essentials/README.md): NumPy and pandas, the problems in a table, data from web APIs | The exercises of [numpy-mnist](https://github.com/avidaldo/numpy-mnist) | 26 Oct – 6 Dec |
| 5 | Building with language models | PIA | Local and remote models, prompts, structured output, testing a component that uses a model *(coming)* | [A chatbot with guardrails](https://github.com/avidaldo/ai-chat-guardrails) | 7 Dec – 17 Jan |
| 6 | Supervised learning | SAA | [Supervised learning](saa/supervised-learning/README.md): regression, classification, and how to tell whether a model really works; [Data preparation](saa/data-preparation/README.md) after its part 3 | [King County house sales](https://github.com/avidaldo/king-county), [California housing](https://github.com/avidaldo/california_e2e), [thyroid disease](https://github.com/avidaldo/thyroid) | 9 Nov – 31 Jan |
| 7 | Serving models | PIA | A model behind a web API and a demo, in a container, deployed *(coming)* | [An image classifier served with FastAPI](https://github.com/avidaldo/cifar-10-fastapi), and [the same as a Gradio app](https://huggingface.co/spaces/avidaldo/cifar-10-fastapi-gradio) | 18–31 Jan |
| | **Exams on term 1** | SAA, PIA | Stages 1–7. Compulsory, and it can raise your grade, never lower it | | **Fixed: SAA Tue 2 Feb, PIA Thu 4 Feb** |

### Term 2

| # | Stage | Module | Topic | Worked examples | Estimated dates |
| ---: | --- | --- | --- | --- | --- |
| 8 | Neural networks | SAA | How a network learns, networks for tables, convolutional networks, reusing a pretrained network *(coming)* | | 1–28 Feb |
| 9 | Agents and MCP | PIA | Tool calling, agents that use tools safely, and MCP, a standard way to connect models to tools *(coming)* | | 1 Feb – 21 Mar |
| 10 | How language models work | SAA | From words as counts to embeddings, attention and transformers *(coming)* | | 15 Mar – 4 Apr |
| 11 | Retrieval-augmented generation (RAG) | PIA | A model's answers grounded in your own documents, citing their sources *(coming)* | | 30 Mar – 18 Apr |
| 12 | Automation and business | PIA | AI systems that run on their own, and whether they are worth it *(coming)* | | 19 Apr – 2 May |
| 13 | Unsupervised learning | SAA | Clustering, dimensionality reduction and anomaly detection *(coming)* | | 26 Apr – 16 May |
| 14 | Vision and voice with pretrained models | PIA | [Computer vision](https://github.com/avidaldo/computer-vision): OpenCV, YOLO, CLIP embeddings and a face-authentication app. Voice: speech to text and text to speech *(coming)* | | 10–23 May |
| 15 | Reinforcement learning | SAA | [Learning from rewards](saa/reinforcement-learning/README.md): agents, environments and Q-learning | [Tic-tac-toe with Q-learning](https://github.com/avidaldo/tictactoe-qlearning) | 10–23 May |
| | **Exams on the whole year** | SAA, PIA | Stages 1–15. May gives your grade, and June is a second chance | | **Fixed: May, SAA Mon 24 and PIA Wed 26; June, SAA Thu 10 and PIA Mon 14** |

## Exams and your grade

Each module is graded on its own, from in-person exams. February covers term 1: it is a compulsory rehearsal, and it can raise your grade, never lower it. May covers the whole year and gives your grade, and June is a second chance. Each exam has a quiz and a practical part on the projects. Accepted contributions can add up to 2 points to a module you have passed. Dates and rules: [How you are assessed](course/assessment.md).

## Improving the materials

If you find an error or something unclear, open an issue; if you can fix it, send a pull request. How, and how contributions count: [Improving the course materials](CONTRIBUTING.md).
