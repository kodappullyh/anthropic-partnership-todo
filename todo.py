#!/usr/bin/env python3
"""Simple command-line todo app."""

import json
import sys
from pathlib import Path

TODOS_FILE = Path("todos.json")


def load() -> list[dict]:
    if not TODOS_FILE.exists():
        return []
    return json.loads(TODOS_FILE.read_text())


def save(todos: list[dict]) -> None:
    TODOS_FILE.write_text(json.dumps(todos, indent=2))


PRIORITIES = {"low", "medium", "high"}


def add(title: str, priority: str = "medium") -> None:
    if priority not in PRIORITIES:
        print(f"Priority must be one of: {', '.join(sorted(PRIORITIES))}")
        return
    todos = load()
    todos.append({"id": len(todos) + 1, "title": title, "priority": priority, "done": False})
    save(todos)
    print(f"Added [{priority}]: {title}")


def list_todos() -> None:
    todos = load()
    if not todos:
        print("No todos yet.")
        return
    for t in todos:
        status = "x" if t["done"] else " "
        priority = t.get("priority", "medium")
        print(f"[{status}] {t['id']}. {t['title']}  ({priority})")


def complete(todo_id: int) -> None:
    todos = load()
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = True
            save(todos)
            print(f"Completed: {t['title']}")
            return
    print(f"No todo with id {todo_id}")


def delete(todo_id: int) -> None:
    todos = load()
    remaining = [t for t in todos if t["id"] != todo_id]
    if len(remaining) == len(todos):
        print(f"No todo with id {todo_id}")
        return
    save(remaining)
    print(f"Deleted todo {todo_id}")


USAGE = """Usage:
  python todo.py add <title> [--priority low|medium|high]
  python todo.py list
  python todo.py done <id>
  python todo.py delete <id>
"""

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(USAGE)
        sys.exit(1)

    cmd, *rest = args
    if cmd == "add" and rest:
        priority = "medium"
        if "--priority" in rest:
            idx = rest.index("--priority")
            if idx + 1 < len(rest):
                priority = rest[idx + 1]
                rest = rest[:idx] + rest[idx + 2:]
        add(" ".join(rest), priority)
    elif cmd == "list":
        list_todos()
    elif cmd == "done" and rest:
        complete(int(rest[0]))
    elif cmd == "delete" and rest:
        delete(int(rest[0]))
    else:
        print(USAGE)
        sys.exit(1)
