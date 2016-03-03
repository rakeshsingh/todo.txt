# -*- coding: utf-8 -*-

import os
import click
import logging

from .log import setup_logging
from .exc import (
    InvalidTodoFile,
    InvalidTodoStatus
)
from .utils import(
    _todo_from_file,
    format_print
)
from .consts import (
    WAITING,
    COMPLETE,
    STATUS_CODE
)

logger = logging.getLogger(__name__)


class Todo(object):

    def __init__(self, todo_dir='.', name='Todos.txt'):
        """Todo Base Class
        :param todo_dir: file path to store todos
        :param name: file name

        e.g. ..code python
            t = Todo()
            t.add_todo('contents', status)
            t.show_all_todos()
            t.write()
        """
        self.todos = None
        self.name = name
        self.todo_dir = todo_dir
        self.path = os.path.join(os.path.expanduser(self.todo_dir), name)
        self.current_max_idx = 1
        self.init()

    def __getitem__(self, idx):
        self._show_todos(idx=idx)

    def init(self):
        """init `todo` file
        if file exists, then initialization self.todos
        and record current max index of todos
        : when add a new todo, the `idx` via only `self.current_max_idx + 1`
        """
        if os.path.isdir(self.path):
            raise InvalidTodoFile
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                tls = [tl.strip() for tl in f if tl]
                todos = map(_todo_from_file, tls)
                self.todos = todos
                for todo in todos:
                    if self.current_max_idx< todo['idx']:
                        self.current_max_idx = todo['idx']
        else:
            logger.warning('No todo files found, initialization a empty todo file')
            with open(self.path ,'w') as f:
                f.flush()

    def add_todo(self, text, status=WAITING):
        idx = self.current_max_idx + 1
        self.todos.append({
            'idx': idx,
            'status': status,
            'text': text
        })

    def edit_todo(self, idx, text):
        pass

    def finish_todo(self, idx):
        for todo in self.todos:
            if todo['idx'] == idx:
                todo['status'] = COMPLETE

    def remove_todo(self, idx):
        pass

    def _show_todos(self, status=None, idx=None):
        """show todos after format
        :param status: what status's todos wants to show.
        default is None, means show all
        """
        if self.todos is None:
            return
        if idx is not None:
            for todo in self.todos:
                if todo['idx'] == idx:
                    format_print(todo['idx'], todo['status'], todo['text'])
            return
        if status is not None:
            if status not in STATUS_CODE:
                raise InvalidTodoStatus
            for todo in self.todos:
                if todo['status'] == status:
                    format_print(todo['idx'], todo['status'], todo['text'])
            return
        for todo in self.todos:
            format_print(todo['idx'], todo['status'], todo['text'])

    def show_waiting_todos(self):
        self._show_todos(status=WAITING)

    def show_done_todos(self):
        self._show_todos(status=COMPLETE)

    def show_all_todos(self):
        self._show_todos()

    def write(self, delete_if_empty=False):
        """flush todos to file
        :param delete_if_empty: delete if todo is empty
        """
        pass


@click.command()
@click.version_option()
def todos():
    setup_logging()
    t = Todo()
    t.show_all_todos()
