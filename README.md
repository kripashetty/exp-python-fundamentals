# Python Fundamentals

Explorations and exercises covering Python fundamentals — decorators, pydantic, asyncio, and more.

## Setup

### Interactive REPL — bpython

This project uses [bpython](https://bpython-interpreter.org/) instead of the standard `python3` REPL.

```bash
uv add bpython   # install
bpython          # launch
```

**Why bpython over python3:**

- **Syntax highlighting** — code is colored as you type, making it easier to spot errors
- **Autocomplete** — tab-completion for attributes, methods, and keywords, with a live suggestion box
- **Inline documentation** — shows the docstring for any function or class as you type its arguments
- **Rewind** — undo the last line of input and re-enter it without restarting the session
- **Paste mode** — cleanly handles indented blocks pasted from an editor without misfire
- **`reload()` shortcut** — reload an imported module without restarting the REPL

