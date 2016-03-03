# -*- coding: utf-8 -*-


class NoTodoFileFoundError(Exception):
    pass


class InvalidTodoStatus(Exception):
    pass


class InvalidTodoFile(Exception):
    pass


class UnknowTodo(Exception):
    def __init__(self, prefix):
        super(UnknowTodo, self).__init__()
        self.prefix = prefix
