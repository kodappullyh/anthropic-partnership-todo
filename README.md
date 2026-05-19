# Todo CLI

A minimal command-line todo app, created to demonstrate Claude Code git workflows (branch, commit, push, PR).

Each todo supports a **priority level** (`low`, `medium`, `high`) so you can focus on what matters most.

## Usage

```bash
# Add a todo (default priority: medium)
python todo.py add "Buy milk"

# Add with explicit priority
python todo.py add "Fix critical bug" --priority high
python todo.py add "Update docs" --priority low

# List all todos (shows priority next to each item)
python todo.py list

# Mark done
python todo.py done 1

# Delete
python todo.py delete 1
```

## Run tests

```bash
pip install pytest
pytest test_todo.py -v
```
