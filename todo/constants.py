# -*- coding: utf-8 -*-

##
# status for todo
##
PENDING = 'o'
COMPLETE = 'x'
NOTODOS = '!'
STATUS_CODE = {
    PENDING: 'waiting',
    COMPLETE: 'done',
    NOTODOS: 'no'
    }

##
# emoji for every status
##
EMOJI = {
    PENDING: ':heavy_multiplication_x:',
    COMPLETE: ':heavy_check_mark:',
    NOTODOS: ':x:'
}

DEFAULT_TODO_DIR = '.'
DEFAULT_TODO_FILE = 'todo.txt'
TODO_FILE_NAME = '/tmp/todo_file_name.txt'

NO_TODOS_SHOW = [-1, NOTODOS, 'No todos...']
