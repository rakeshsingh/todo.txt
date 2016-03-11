# -*- coding: utf-8 -*-

import pytest
from click.testing import CliRunner

from Todos.todo import todos


@pytest.fixture
def runner(request):
    return CliRunner()


def test_list_waiting_todos(runner, monkeypatch):
    res = runner.invoke(todos, [])
    assert not res.exception
    assert res.exit_code == 0


def test_list_all_todos(runner, monkeypatch):
    res = runner.invoke(todos, ['--all'])
    assert not res.exception
    assert res.exit_code == 0
