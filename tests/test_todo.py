# -*- coding: utf-8 -*-

import pytest
from click.testing import CliRunner

from Todos.todo import todos


@pytest.fixture
def runner(request):
    return CliRunner()


def test_list_waiting_todos(runner, monkeypatch):
    res = runner.invoke(todos)
    assert res.exit_code == 0
    assert res.output.decode('utf-8') == ''
