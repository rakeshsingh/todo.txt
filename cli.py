# -*- coding: utf-8 -*-

import os
import click
import logging

from todo.log import setup_logging
from todo.todo import Todo, TodoList
from todo.utils import get_todo_file, set_todo_file


logger = logging.getLogger(__name__)

def check_ids(ctx, param, value):
    if not value:
        return []
    return value.split(',')


@click.command()
@click.version_option()
@click.option('-u', '--use', help='use `name` file to store your toodo list')
@click.option('-a', '--add', help='add a new todo task')
@click.option('-e', '--edit', nargs=2, type=str, help='edit todo by id'
                    ' - usage: tasks -e 2 ``text``')
@click.option('-r', '--remove', type=str, callback=check_ids, help='remove todo by id(s)')
@click.option('-p', '--priority', type=str, callback=check_ids, help='set priority')
@click.option('-c', '--complete', type=str, callback=check_ids, help='complete todo tasks by id(s)'
                    ' - usage: tasks -c 1,2')
@click.option('-l', '--list', is_flag=True, default=False, 
                help='''show all todo tasks in todo file. filter further by projects `+projectname` or contexts `@contextname` '''
                ' - usage: tasks -l +project1 @context1 ')
@click.option('-ld', '--done', is_flag=True, default=False, help='show all done tasks')
@click.option('-lp', '--pending', is_flag=True, default=False, help='show all pending tasks')
@click.option('-cl', '--clear', is_flag=True, default=False, help='clear all tasks, need confirmation.')
@click.argument('vals', nargs=-1)
def todo(use, done, pending,  add, complete, edit, remove, list, clear, priority, vals):
    setup_logging()
    if vals:
        pass
    else: 
        vals = None
    if use:
        set_todo_file(use)
        logger.info('Success set todo file to `{}`'.format(use))
    todo_file_name = get_todo_file()
    t = TodoList(name=todo_file_name)
    try:
        if clear:
            t.clear_all()
            t.write()
            return
        elif add:
            t.add_todo(add)
            t.write()
        elif edit:
            t.edit_todo(edit[0], edit[1])
            t.write()
        elif remove:
            t.remove_todo(remove)
            t.write()
        elif complete:
            t.finish_todo(complete)
            t.write()
        else:
            if list:
                t.show_all_tasks(status=None, vals=vals)
            elif done:
                t.show_all_tasks(status=True, vals=vals)
            else:
                t.show_all_tasks(status=False, vals=vals)
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    todo()
