# -*- coding: utf-8 -*-

##
# status for tods
##
WAITING = 'o'
COMPLETE = 'x'
NOTODOS = '!'
STATUS_CODE = [WAITING, COMPLETE, NOTODOS]

##
# emoji for every status
##
EMOJI = {
    WAITING: ':heavy_multiplication_x:',
    COMPLETE: ':heavy_check_mark:',
    NOTODOS: ':x:'
}

DEFAULT_TODO_FILE = 'Todos.txt'

NO_TODOS_SHOW = [-1, NOTODOS, 'No todos...']
