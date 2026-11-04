# Essential Tools for AI Programming

## Your First Week

1. Create a [GitHub](https://github.com) account.
2. Install [Git](https://git-scm.com/downloads), and the [GitHub CLI](https://cli.github.com/) to log in from the terminal with `gh auth login` ([Git and GitHub](git_github.md)).
3. Install [uv](uv_tutorial.md) or, if you prefer conda, [Miniforge](conda_tutorial.md). Both install Python itself: you don't need to install it separately.
4. Install an editor: [VS Code](https://code.visualstudio.com/) with its *Python* and *Jupyter* extensions, or PyCharm.
5. Choose an AI coding assistant ([Working with an AI coding assistant](ai_assisted_development.md)).
6. Clone this repository and install its `requirements.txt` in an environment ([how](#virtual-environments)). Then fork and set up [numpy-mnist](https://github.com/avidaldo/numpy-mnist), up to step 4 of its README.
7. [Register your GitHub username in the aula virtual](https://fpadistancia.edu.xunta.gal/mod/feedback/view.php?id=2318916), so that your work can be found and your contributions counted.

The rest of this note explains each tool.

## Programming Languages

### Python

Python is the **predominant programming language for machine learning**. It is the language we use throughout both modules. Python is an interpreted, high-level, general-purpose programming language. It is versatile and easy to learn, and has a **vast collection of libraries and frameworks for AI**, machine learning and deep learning ([why](why_python.md)).

Python programming courses:
- https://edube.org/study/pe1
- https://edube.org/study/pe2


### Other Relevant Programming Languages in AI

- R: Primarily used in statistics and data analysis.
- C/C++: Many of the libraries accessed from Python are implemented in C/C++ since they are low-level languages and much faster than Python. C++ remains the reference when performance is critical.
- CUDA: NVIDIA's extension of C++ for programming GPUs, on which most deep learning runs.
- Rust: fast and memory-safe, and increasingly the language of Python's tools: uv, the Ruff linter, the Polars dataframe library and Hugging Face's tokenizers are written in it.
- Julia: High-performance programming language designed for scientific and technical computing.
- Mojo: Aims to achieve Python's usability with performance similar to C.


## Git and Git Forges

Git is a distributed version control system that allows us to keep a record of changes in a project's source code. Git forges are services that allow us to host our Git repositories online, such as GitHub, GitLab, Codeberg and Bitbucket. Both modules work the way most software teams do: on public repositories, through issues and pull requests. You fork a repository, work in your fork, and propose your changes in a pull request, which is also how you submit your work for feedback.

- [Git and GitHub: From Commits to Pull Requests](git_github.md)
- [Git and GitHub for AI Programming](https://www.youtube.com/watch?v=T1tYBbiWTbc) (video)


## IDEs (Integrated Development Environment)

For working with Python for machine learning and deep learning, some of the most popular IDEs are:

### [Visual Studio Code (VS Code)](https://code.visualstudio.com/)

Visual Studio Code is a source code editor developed by Microsoft. It is cross-platform and supports multiple programming languages. It is one of the most popular editors among software developers.

- [VISUAL STUDIO CODE: Beginner's Tutorial](https://www.youtube.com/watch?v=CxF3ykWP1H4)

### [Cursor](https://www.cursor.com/)

Cursor is a [fork](https://en.wikipedia.org/wiki/Fork_(software_development)) of VS Code focused on using LLMs for programming.

### [PyCharm](https://www.jetbrains.com/pycharm/)

PyCharm is an IDE developed by JetBrains. It is one of the most popular IDEs for Python and is used by many software developers. It also covers notebooks and data exploration: JetBrains stopped selling DataSpell, its data-science IDE, in May 2026, and moved its users to PyCharm.

### AI coding assistants

Most of these editors integrate AI coding assistants, such as GitHub Copilot, Claude Code or OpenAI Codex, and some assistants also run on their own in the terminal. You will use one throughout the year: see [Working with an AI Coding Assistant](ai_assisted_development.md).

## Jupyter Notebooks

Jupyter is an application that allows us to create notebooks (documents that combine code, rich text, equations, visualisations, etc.) in the browser. These notebooks are files with the `.ipynb` extension (when using the Python language) that can be exported in different static formats, such as HTML or PDF. The `.ipynb` files are internally JSON.

Editors such as VS Code and PyCharm open notebooks directly. A notebook runs on a **kernel**, the Python of an environment: choose your project's environment as the kernel (*Select Kernel* in VS Code). The environment needs the `ipykernel` package, which `jupyter` includes.

## Virtual Environments

**Virtual environments** allow us to isolate a project's **dependencies** from those of the operating system. This enables us to have different versions of the same **libraries** in different projects without conflicts between them.

Every repository of these modules lists its dependencies in a `requirements.txt` file, which both of these tools install. Choose one:

- **uv**, recommended: a modern, fast tool that manages Python projects, their virtual environments and their dependencies, and installs Python itself. [uv Tutorial: Python Projects, Environments and Packages](uv_tutorial.md); [UV for Python… (Almost) All Batteries Included](https://www.youtube.com/watch?v=qh98qOND6MI) (video).
- **conda**, the alternative: a good choice if you already use it, or if you need programs that aren't Python packages, such as ffmpeg. [Conda Tutorial: Environment and Package Management](conda_tutorial.md).

Everything in these modules runs on Windows, macOS and Linux. On Windows, when a tool or a tutorial expects Linux, [WSL](https://learn.microsoft.com/windows/wsl/install) (Windows Subsystem for Linux) runs a full Linux inside Windows.

How these tools relate to pip, venv and Poetry: [Dependency and Virtual Environment Management in Python](py_dependencies.md); [Introduction to pip, conda, and virtual environments](https://www.youtube.com/watch?v=7Rd-Gj8o-6Q) (video).


## [Google Colab](https://colab.research.google.com/)

Google Colab is a free Google service that allows us to run Jupyter notebooks in the cloud. Colab allows us to execute code in Python, R, and other programming languages, and provides access to hardware resources such as GPUs and TPUs. It is a good fallback when your computer is too slow for a notebook, as can happen with the neural networks of term 2.

