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
    format_show,
    _todo_to_file,
    set_todo_file,
    get_todo_file,
    _show
)
from .consts import (
    WAITING,
    COMPLETE,
    STATUS_CODE,
    NO_TODOS_SHOW,
    DEFAULT_TODO_FILE
)

logger = logging.getLogger(__name__)


class Todo(object):

    def __init__(self, todo_dir='.', name=DEFAULT_TODO_FILE):
        """Todo Base Class
        :param todo_dir: file path to store todos
        :param name: file name

        e.g. ..code python
            t = Todo()
            t.add_todo('contents', status)
            t.show_all_todos()
            t.write()
        """
        self.todos = []
        self.name = name
        self.todo_dir = todo_dir
        self.path = os.path.join(os.path.expanduser(self.todo_dir), name)
        self.current_max_idx = 0
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
                    if self.current_max_idx < todo['idx']:
                        self.current_max_idx = todo['idx']
        else:
            logger.warning('No todo files found, initialization a empty todo file')
            with open(self.path, 'w') as f:
                f.flush()

    def add_todo(self, text, status=WAITING):
        idx = self.current_max_idx + 1
        self.todos.append({
            'idx': idx,
            'status': status,
            'text': text
        })

    def edit_todo(self, idx, text):
        for todo in self.todos:
            if todo['idx'] == int(idx):
                todo['text'] = text

    def finish_todo(self, idxs):
        for idx in idxs:
            for todo in self.todos:
                if todo['idx'] == int(idx):
                    todo['status'] = COMPLETE

    def remove_todo(self, idxs):
        for idx in idxs:
            for todo in self.todos:
                if todo['idx'] == int(idx):
                    self.todos.remove(todo)

    def clear_all(self):
        """clear todos
        """
        confirm = raw_input('confirm ? (Y/N): ')
        if confirm in ['Y', 'y']:
            self.todos = []

    def _show_no_todos(self, text_fix=None):
        format_show(
            NO_TODOS_SHOW[0],
            NO_TODOS_SHOW[1],
            text_fix or NO_TODOS_SHOW[2])

    def _show_todos(self, todo):
        format_show(todo['idx'], todo['status'], todo['text'])

    def _show(self, status=None, idx=None):
        """show todos after format
        :param status: what status's todos wants to show.
        default is None, means show all
        """
        _show('', 50)
        if not self.todos:
            self._show_no_todos()
        elif idx is not None:
            for todo in self.todos:
                if todo['idx'] == idx:
                    self._show_todos(todo)
        elif status is not None:
            if status not in STATUS_CODE:
                raise InvalidTodoStatus
            _todos = []
            for todo in self.todos:
                if todo['status'] == status:
                    _todos.append(todo)
            if not _todos:
                self._show_no_todos(text_fix='No {} todos...'.format(
                                    STATUS_CODE.get(status), None))
            else:
                for todo in _todos:
                    self._show_todos(todo)
        else:
            for todo in self.todos:
                self._show_todos(todo)
        _show('', 50)

    def show_waiting_todos(self):
        self._show(status=WAITING)

    def show_done_todos(self):
        self._show(status=COMPLETE)

    def show_all_todos(self):
        self._show()

    def write(self, delete_if_empty=False):
        """flush todos to file
        :param delete_if_empty: delete if todo is empty
        """
        with open(self.path, 'w') as f:
            if not self.todos:
                f.flush()
            else:
                for todo in _todo_to_file(self.todos):
                    f.write(todo)


def check_ids(ctx, param, value):
    if not value:
        return []
    return value.split(',')


@click.command()
@click.version_option()
@click.option('--what', is_flag=True, default=False,
              help='show current use todo file\'s name')
@click.option('--use', help='use `name` file to store your todos')
@click.option('--done', is_flag=True, default=False,
              help='show all done todos')
@click.option('-n', '--new', help='new todo')
@click.option('-c', '--complete_ids', type=str, callback=check_ids,
              help='complete todo by id(s)'
                    ' - usage: todos -c 1,2')
@click.option('-e', '--edit', nargs=2, type=str,
              help='edit todo by id'
                   ' - usage: todos -e 2 ``text``')
@click.option('-r', '--remove', type=str, callback=check_ids,
              help='remove todo by id(s)')
@click.option('--all', is_flag=True, default=False,
              help='show all todos')
@click.option('--clear', is_flag=True, default=False,
              help='clear all todos, need confirm!!')
def todos(what, use, done, new, complete_ids, edit, remove, all, clear):
    setup_logging()
    if use:
        set_todo_file(use)
        logger.info('Success set todo file to `{}`'.format(use))
    todo_file_name = get_todo_file()
    if what:
        logger.info('current todo file\'name is `{}`'.format(todo_file_name))
        return
    t = Todo(name=todo_file_name)
    try:
        if clear:
            t.clear_all()
            t.write()
            return
        elif new:
            t.add_todo(new)
            t.write()
        elif complete_ids:
            t.finish_todo(complete_ids)
            t.write()
        elif edit:
            t.edit_todo(edit[0], edit[1])
            t.write()
        elif remove:
            t.remove_todo(remove)
            t.write()
        else:
            if all:
                t.show_all_todos()
            elif done:
                t.show_done_todos()
            else:
                t.show_waiting_todos()
    except Exception as e:
        logger.error(e)
    finally:
        pass
