# -*- coding: utf-8 -*-

import emoji

##
# status for tods
##
WAITING = 0
DONE = 1

##
# emoji for every status
##
EMOJI = {
    WAITING: ':heavy_multiplication_x:',
    DONE: ':heavy_check_mark:'
}


##
# mock data for test
##
mock_data = {
    'Test Todo': WAITING,
    'Coding': DONE
}


class InvalidTodoFile(Exception):
    pass


class UnknowTodo(Exception):
    def __init__(self, prefix):
        super(UnknowTodo, self).__init__()
        self.prefix = prefix


def format_print(idx, status, text):
    e = EMOJI.get(status, None)
    if e is None:
        raise
    print emoji.emojize('{}. {}  {}'.format(idx, e, text), use_aliases=True)


class Todo(object):

    def __init__(self, todo_dir='.', name='Todos.txt'):
        self.todos = mock_data
        self.name = name
        self.todo_dir = todo_dir
        self.init()

    def __getitem__(self, idx):
        pass

    def init(self):
        pass

    def add_todo(self, text, status=WAITING):
        self.todos.update({text: status})

    def edit_todo(self, idx, text):
        pass

    def finish_todo(self, idx):
        if idx > len(self.todos):
            raise
        _idx = 1
        for todo in self.todos:
            if idx == _idx:
                self.todos[todo] = DONE
            _idx += 1

    def remove_todo(self, idx):
        pass

    def show_todos(self):
        idx = 1
        for todo in self.todos:
            format_print(idx, mock_data[todo], todo)
            idx += 1

    def write(self, delete_if_empty=False):
        pass

if __name__ == '__main__':
    t = Todo()
    t.show_todos()
    print 'add a todo `{}`'.format('Kiven')
    t.add_todo('Kiven')
    t.show_todos()
    print 'finish 2 todo'
    t.finish_todo(2)
    t.show_todos()
