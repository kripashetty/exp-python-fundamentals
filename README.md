# Python Fundamentals

Explorations and exercises covering Python fundamentals — decorators, pydantic, asyncio, and more.

## Setup


### 1. Python package manager 
 https://docs.astral.sh/uv/

If you're working with modern Python projects, **`uv` is worth knowing**. It's a fast Python project/package manager from Astral that can cover much of what you might otherwise use `pip`, `venv`, `pip-tools`, and Python-version-management tooling for. 

A useful mental model is:

> **`uv` manages your Python version + virtual environment + dependencies + lockfile + running commands.**

### Commands I'd memorize

| Command | What it does | Typical use |
|---|---|---|
| `uv init` | Initialize a Python project | Starting a project |
| `uv add pandas` | Add dependency | Instead of `pip install pandas` |
| `uv remove pandas` | Remove dependency | Remove package |
| `uv run main.py` | Run Python inside project env | Run your code |
| `uv run pytest` | Run command inside project env | Tests/tools |
| `uv sync` | Make environment match project | After cloning a repo |
| `uv lock` | Update/create `uv.lock` | Lock exact dependency versions |
| `uv tree` | Show dependency tree | Debug dependencies |
| `uv python install 3.12` | Install Python | Manage Python versions |
| `uv venv` | Manually create `.venv` | Lower-level workflows |
| `uvx ruff check .` | Run a tool temporarily | One-off CLI tools |
| `uv --help` | Help | When you forget something |

These are the core project commands documented by uv. 

### A normal workflow

Say you're starting a small data-analysis project:

```bash
uv init my-project
cd my-project
```

That creates a project including `pyproject.toml`. 

Add dependencies:

```bash
uv add pandas
uv add numpy
uv add requests
```

Your `pyproject.toml` will track those dependencies, and uv will also manage a `uv.lock` containing the resolved versions. 

Then run your code:

```bash
uv run main.py
```

or:

```bash
uv run python main.py
```

`uv run` is particularly convenient because it ensures the project's environment and dependencies are up to date before executing the command. 

### The big difference from the traditional workflow

You may have learned something like:

```bash
python -m venv .venv
source .venv/bin/activate

pip install pandas
pip install numpy

python main.py
```

With uv, you can usually think:

```bash
uv init
uv add pandas numpy
uv run main.py
```

You generally **don't need to activate the virtual environment** when using `uv run`; uv manages the project's `.venv` for you. 

### `uv add` vs `uv pip install`

This distinction is important.

For a uv-managed **project**, prefer:

```bash
uv add pandas
```

This declares `pandas` as a project dependency and updates the project environment/lockfile. 

You *can* do:

```bash
uv pip install pandas
```

but `uv pip` is the lower-level, pip-compatible interface. The uv docs specifically recommend `uv add` for project dependencies rather than manually modifying the project environment with `uv pip install`. 

So memorize:

```text
Working on a uv project?
        ↓
    uv add X

Managing an environment manually / legacy pip workflow?
        ↓
    uv pip install X
```

### `uv sync` is especially important at work

Suppose you clone an existing repository:

```bash
git clone ...
cd project
```

and it contains:

```text
project/
├── pyproject.toml
├── uv.lock
├── src/
└── ...
```

Run:

```bash
uv sync
```

uv creates `.venv` if necessary and installs the project's locked dependencies into it. 

Then:

```bash
uv run python src/main.py
```

or:

```bash
uv run pytest
```

So a very common workflow is simply:

```bash
git clone ...
cd project

uv sync
uv run pytest
```

### `uvx` is another great command

`uvx` lets you run a Python CLI tool without permanently installing it into your project. It's an alias for `uv tool run`. 

For example:

```bash
uvx ruff check .
```

or:

```bash
uvx black .
```

Think of the difference as:

```text
uv add
│
├── My application DEPENDS on this package
│
└── uv add requests


uvx
│
├── I just want to RUN this tool
│
└── uvx ruff check .
```

If you use a tool constantly and want it installed user-wide, there's also:

```bash
uv tool install ruff
```

### The files you should recognize

A uv project will commonly contain:

```text
my-project/
│
├── pyproject.toml
├── uv.lock
├── .python-version
├── .venv/
└── main.py
```

Think of them as:

| File | Meaning |
|---|---|
| `pyproject.toml` | **What my project needs** |
| `uv.lock` | **Exact resolved dependency versions** |
| `.python-version` | **Python version associated with project** |
| `.venv/` | **Actual installed environment** |

Don't commit `.venv/` to Git; uv's documentation explicitly recommends excluding it from version control. 

### If you only memorize 6 things

```bash
# Start project
uv init

# Add package
uv add pandas

# Remove package
uv remove pandas

# Run something
uv run main.py

# Install/sync project dependencies
uv sync

# Run a one-off CLI tool
uvx ruff check .
```

Then remember this workflow:

```text
Create project
     ↓
   uv init
     ↓
Add dependencies
     ↓
 uv add ...
     ↓
  Write code
     ↓
uv run ...
     ↓
Someone else clones repo
     ↓
   uv sync
     ↓
uv run ...
```

That covers probably **90% of what you initially need from uv**. The next things I'd learn after that are `pyproject.toml`, `uv.lock`, dependency groups/dev dependencies, and how uv handles Python versions.


### 2. Interactive REPL — bpython

This project uses [bpython](https://bpython-interpreter.org/) instead of the standard `python3` REPL.

```bash
uv add bpython   # install
uv run --with bpython   bpython       # launch the REPL with the awareness of all the packages that uv has installed
```

**Why bpython over python3:**

- **Syntax highlighting** — code is colored as you type, making it easier to spot errors
- **Autocomplete** — tab-completion for attributes, methods, and keywords, with a live suggestion box
- **Inline documentation** — shows the docstring for any function or class as you type its arguments
- **Rewind** — undo the last line of input and re-enter it without restarting the session
- **Paste mode** — cleanly handles indented blocks pasted from an editor without misfire
- **`reload()` shortcut** — reload an imported module without restarting the REPL
