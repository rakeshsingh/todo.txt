# -*- coding: utf-8 -*-

import re
from .constants import DEFAULT_TODO_FILE, TODO_FILE_NAME
from .colorizer import make_colorizer


def print_colorful(idx, todo):
    fun = make_colorizer('white')
    if todo.completion:
        fun= make_colorizer('darkgreen')
    else:
        if todo.priority =='A':
            fun= make_colorizer('brown')
        elif todo.priority =='B':
            fun= make_colorizer('darkgreen')
        elif todo.priority =='C':
            fun= make_colorizer('teal')
        elif todo.priority =='D':
            fun= make_colorizer('darkblue')
        else:
            fun = make_colorizer('white')
    print(fun('{:02d} {}'.format(idx,todo.task_string)))

def set_todo_file(name):
    with open(TODO_FILE_NAME, 'w') as f:
        f.write(name)
    return True


def get_todo_file():
    todo_file_name = None
    try:
        with open(TODO_FILE_NAME, 'r') as f:
            todo_file_name = f.read().strip()
    except Exception:
        todo_file_name = DEFAULT_TODO_FILE
    finally:
        return todo_file_name
