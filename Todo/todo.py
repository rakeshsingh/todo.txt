# -*- coding: utf-8 -*-

import os
import re
import emoji

##
# status for tods
##
WAITING = 'o'
COMPLETE = 'x'
STATUS_CODE = [WAITING, COMPLETE]

##
# emoji for every status
##
EMOJI = {
    WAITING: ':heavy_multiplication_x:',
    COMPLETE: ':heavy_check_mark:'
}


class InvalidTodoStatus(Exception):
    pass


class InvalidTodoFile(Exception):
    pass


class UnknowTodo(Exception):
    def __init__(self, prefix):
        super(UnknowTodo, self).__init__()
        self.prefix = prefix


def _todo_from_file(line):
    _one_todo = line.split()
    idx, status, text = _one_todo[0], _one_todo[1], ' '.join(_one_todo[2:])
    idx = re.sub('\.', '', idx)
    status = re.sub('\[|\]', '', status)
    return {
        'idx': int(idx),
        'status': status,
        'text': text
    }


def format_print(idx, status, text):
    e = EMOJI.get(status, None)
    if e is None:
        raise
    print emoji.emojize('{}. {}  {}'.format(idx, e, text), use_aliases=True)


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
        pass

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
        if idx > len(self.todos):
            raise
        _idx = 1
        for todo in self.todos:
            if idx == _idx:
                self.todos[todo] = COMPLETE
            _idx += 1

    def remove_todo(self, idx):
        pass

    def _show_todos(self, status=None):
        """show todos after format
        :param status: what status's todos wants to show.
        default is None, means show all
        """
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
        self._show_todos(WAITING)

    def show_done_todos(self):
        self._show_todos(COMPLETE)

    def show_all_todos(self):
        self._show_todos()

    def write(self, delete_if_empty=False):
        """flush todos to file
        :param delete_if_empty: delete if todo is empty
        """
        pass

if __name__ == '__main__':
    t = Todo()
    t.show_all_todos()
    print
    t.add_todo('kiven\'s test')
    t.show_all_todos()
    print
    t.show_waiting_todos()
    print
    t.show_done_todos()
