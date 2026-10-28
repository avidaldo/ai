# Artificial Intelligence 2026/27

Materials for two modules of the specialisation course in Artificial Intelligence and Big Data, taught together as one path:

- **SAA · Machine Learning Systems**: how models learn from data, how they are trained, and how to tell whether they really work.
- **PIA · AI Programming**: building software with AI: Python and its tooling, language models, retrieval, agents, deployment and automation.

## [Spanish translation of this repository](https://github.com/NainIglesias/ai/tree/traduccion-es) (maintained by [NainIglesias](https://github.com/NainIglesias))

## Start here

1. **[Working plan](course/working-plan.md)**: how to work through the year, the three tiers of each topic, the projects you fork and build on, and how to practise.
2. **[How you are assessed](course/assessment.md)**: the exams, how your grade is calculated, and how contributions count.
3. **[Improving the materials](CONTRIBUTING.md)**: report errors, ask for clearer explanations, or fix things yourself.

## Roadmap

The year in fifteen stages, in the order we work through them; it adapts as the year goes. Each stage belongs to one module: if you take only one, follow its rows. Two stages build on the other module: building with language models (5, PIA) builds on the note on language models of stage 2 (SAA), and RAG (11, PIA) needs how language models work (10, SAA).

Each topic's README gives its path, with the core items marked ★. The worked examples, and the software you build and run, are repositories of their own. Items marked *(coming)* are being written, and are linked when they are ready.

### Term 1

| # | Stage | Module | Topic | Worked examples and deep dives |
| ---: | --- | --- | --- | --- |
| 1 | Getting started | PIA | [Setting up](pia/setup/README.md): Python, uv or conda, Git and GitHub, working with an AI coding assistant | First task: [numpy-mnist](https://github.com/avidaldo/numpy-mnist), forked in week 1. Deep dives: [a specs-driven Copilot workflow in VS Code](https://github.com/avidaldo/tutorial-SSD-customizations-VSCode/blob/main/tutorial.md), [Copilot customizations](https://github.com/avidaldo/vccode-customizations-AI-intro) |
| 2 | What AI and machine learning are | SAA | [The map of the year](saa/concepts/README.md): what AI and machine learning are, and each family of models seen from the outside | Deep dives: [classical AI, intelligence without learning](saa/concepts/deep-dives/classical-ai/README.md), [probability and Bayes' theorem](saa/concepts/deep-dives/probability/README.md) |
| 3 | Python for AI | PIA | [Why Python rules AI](pia/setup/why_python.md) although it is slow; program structure, with [tic-tac-toe](https://github.com/avidaldo/python-tic-tac-toe), recommended | Deep dive: [compare-python-c-efficiency](https://github.com/avidaldo/compare-python-c-efficiency), to measure it yourself |
| 4 | Working with data | PIA | [Python data essentials](pia/python-data-essentials/README.md): NumPy and pandas to load, inspect, reshape and combine data, find the problems in a table, and get data from web APIs | Exercises: [numpy-mnist](https://github.com/avidaldo/numpy-mnist) |
| 5 | Building with language models | PIA | Calling models locally and through an API, prompts, structured output, testing and measuring a component that uses a model *(coming)*. Builds on the stage-2 note [Language models from the outside](saa/concepts/background/language_models.md) | Worked example: [a chatbot with guardrails](https://github.com/avidaldo/ai-chat-guardrails), on a local or a remote model |
| 6 | Supervised learning | SAA | Regression and classification, and how to tell whether a model really works *(coming)*. Builds on the stage-2 note [The life of a machine learning project](saa/concepts/background/ml_project_lifecycle.md) | Worked examples: [California housing](https://github.com/avidaldo/california_e2e), [King County house sales](https://github.com/avidaldo/king-county), [thyroid disease](https://github.com/avidaldo/thyroid). Deep dive: data preparation, from exploration to encoding and scaling *(coming)* |
| 7 | Serving models | PIA | A model behind a web API and a demo, in a container, deployed *(coming)* | Worked examples: [an image classifier served with FastAPI](https://github.com/avidaldo/cifar-10-fastapi), and [the same classifier as a Gradio app](https://huggingface.co/spaces/avidaldo/cifar-10-fastapi-gradio) |

### Term 2

| # | Stage | Module | Topic | Worked examples and deep dives |
| ---: | --- | --- | --- | --- |
| 8 | Neural networks | SAA | How a network learns, networks for tables, convolutional networks, reusing a pretrained network *(coming)*. Builds on the stage-2 note [Neural networks from the outside](saa/concepts/background/neural_networks.md) | |
| 9 | Agents and MCP | PIA | Tool calling, agents that use tools safely, and MCP, a standard protocol to connect models to tools *(coming)* | |
| 10 | How language models work | SAA | From words as counts to embeddings, attention and transformers *(coming)*. Builds on the stage-2 note [Language models from the outside](saa/concepts/background/language_models.md) | |
| 11 | Retrieval-augmented generation (RAG) | PIA | Grounding a model's answers in your own documents, with answers that cite their sources *(coming)* | |
| 12 | Automation and business | PIA | Making AI systems run on their own, and deciding whether they are worth it *(coming)* | |
| 13 | Unsupervised learning | SAA | Clustering, dimensionality reduction and anomaly detection *(coming)* | |
| 14 | Vision and voice with pretrained models | PIA | [Computer vision](https://github.com/avidaldo/computer-vision) with OpenCV, YOLO object detection, CLIP embeddings and a face-authentication app. Voice with pretrained models: speech to text and text to speech *(coming)* | |
| 15 | Reinforcement learning | SAA | [Learning from rewards](saa/reinforcement-learning/README.md): agents, environments and Q-learning | Worked example: [tic-tac-toe with Q-learning](https://github.com/avidaldo/tictactoe-qlearning), from the simplest version to an agent that never loses |

The February exam covers term 1, and the May exam the whole year: see [how you are assessed](course/assessment.md).

