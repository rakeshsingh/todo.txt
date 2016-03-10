# -*- coding: utf-8 -*-

##
# status for tods
##
WAITING = 'o'
COMPLETE = 'x'
NOTODOS = '!'
STATUS_CODE = {
    WAITING: 'waiting',
    COMPLETE: 'done',
    NOTODOS: 'no'}

##
# emoji for every status
##
EMOJI = {
    WAITING: ':heavy_multiplication_x:',
    COMPLETE: ':heavy_check_mark:',
    NOTODOS: ':x:'
}

DEFAULT_TODO_FILE = 'Todos.txt'
TODO_FILE_NAME = '/tmp/todo_file_name.txt'

NO_TODOS_SHOW = [-1, NOTODOS, 'No todos...']
