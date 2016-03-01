# -*- coding: utf-8 -*-


class InvalidTodoFile(Exception):
    pass


class UnknowTodo(Exception):
    def __init__(self, prefix):
        super(UnknowTodo, self).__init__()
        self.prefix = prefix


class Todo(object):

    def __init__(self, todo_dir='.', name='Todos.txt'):
        self.todos = {}
        self.done = {}
        self.name = name
        self.todo_dir = todo_dir

    def __getitem__(self, prefix):
        pass

    def add_todo(self, text):
        pass

    def edit_todo(self, prefix, text):
        pass

    def finish_todo(self, prefix):
        pass

    def remove_todo(self, prefix):
        pass

    def show_todos(self, kind='todos', verbose=False, quiet=False, grep=''):
        pass

    def write(self, delete_if_empty=False):
        pass

if __name__ == '__main__':
    pass
