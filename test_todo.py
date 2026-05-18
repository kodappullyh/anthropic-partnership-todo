"""Tests for todo.py."""

import json
import pytest
from pathlib import Path
from unittest.mock import patch
import todo


@pytest.fixture(autouse=True)
def tmp_todos(tmp_path, monkeypatch):
    monkeypatch.setattr(todo, "TODOS_FILE", tmp_path / "todos.json")


def test_add_creates_todo():
    todo.add("Buy milk")
    todos = todo.load()
    assert len(todos) == 1
    assert todos[0]["title"] == "Buy milk"
    assert todos[0]["done"] is False


def test_list_empty(capsys):
    todo.list_todos()
    assert "No todos yet" in capsys.readouterr().out


def test_complete():
    todo.add("Write tests")
    todo.complete(1)
    todos = todo.load()
    assert todos[0]["done"] is True


def test_delete():
    todo.add("Delete me")
    todo.delete(1)
    assert todo.load() == []


def test_complete_missing_id(capsys):
    todo.complete(99)
    assert "No todo with id 99" in capsys.readouterr().out
