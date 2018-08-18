# -*- coding: utf-8 -*-

import os
import click
import logging
import re
import hashlib

from .log import setup_logging
from .exc import (
    InvalidTodoFile,
    InvalidTodoStatus
)
from .utils import(
    print_colorful,
    set_todo_file,
    get_todo_file,
)
from .consts import (
    PENDING,
    COMPLETE,
    STATUS_CODE,
    NO_TODOS_SHOW,
    DEFAULT_TODO_FILE,
    DEFAULT_TODO_DIR
)

logger = logging.getLogger(__name__)

class TodoList:
    def __init__(self, todo_dir=DEFAULT_TODO_DIR, name=DEFAULT_TODO_FILE):
        """init `todo` file
        if file exists, then initialization self.tasks
        and record current max index of tasks
        : when add a new todo, the `idx` via only `self.current_max_idx + 1`
        """
        self.name = name
        self.todo_dir = todo_dir
        self.path = os.path.join(os.path.expanduser(self.todo_dir), name)
        self.current_max_idx = 0
        self.tasks  = []
        counter = 0
        if os.path.isdir(self.path):
            raise InvalidTodoFile
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                lines = [tl.strip() for tl in f if tl]
                for line in lines:
                    counter = counter + 1 
                    self.tasks.append({'idx': counter, 'task': Todo(line)})
                self.current_max_idx = counter
        else:
            logger.warning('No todo files found, initialization a empty todo file')
            with open(self.path, 'w') as f:
                f.flush()

    def __getitem__(self, idx):
        self._show_tasks(idx=idx)
    
    def add_todo(self, text):
        idx = self.current_max_idx + 1
        self.tasks.append({'idx':idx, 'task':Todo(text.strip())})

    def edit_todo(self, idx, text):
        for todo in self.tasks:
            if todo['idx'] == int(idx):
                todo['task'] = Todo(text)

    def finish_todo(self, idxs):
        for idx in idxs:
            for todo in self.tasks:
                if todo['idx'] == int(idx):
                    if todo['task'].task_string.lower()[0] !='x':
                        todo['task'] = Todo('X ' + todo['task'].task_string) 

    def remove_todo(self, idxs):
        for idx in idxs:
            for todo in self.tasks:
                if todo['idx'] == int(idx):
                    self.tasks.remove(todo)

    def clear_all(self):
        """clear tasks
        """
        confirm = input('confirm ? (Y/N): ')
        if confirm in ['Y', 'y']:
            self.tasks = []

    def _show_tasks(self, todo):
        print_colorful(todo['idx'], todo['task'])

    def _show(self, status=None, idx=None):
        """show tasks after format
        :param status: what status's tasks wants to show.
        default is None, means show all
        """
        _tasks = []
        _tasks = list(filter(lambda x: 
            (idx is None or idx == x['idx']) 
            and (status is None or status == x['task'].completion) 
            , self.tasks))
        #_tasks = list(filter(lambda x: (True if idx is None or x['idx'] == idx) 
        #    and ( True if status is None or x['task'].completion == completion ) , self.tasks)) 
        for todo in _tasks:
            self._show_tasks(todo)

    def show_waiting_tasks(self):
        self._show(status=False)

    def show_done_tasks(self):
        self._show(status=True)

    def show_all_tasks(self):
        self._show()

    def write(self, delete_if_empty=False):
        self.write_txt()
        self.write_md()

    def write_txt(self, delete_if_empty=False):
        """flush tasks to file
        :param delete_if_empty: delete if todo is empty
        """
        with open(self.path, 'w') as f:
            if not self.tasks:
                f.flush()
            else:
                for todo in self.tasks:
                    f.write(todo['task'].task_string)
                    f.write('\n')

    def write_md(self, delete_if_empty=False):
        """flush tasks to file
        :param delete_if_empty: delete if todo is empty
        """
        filename = self.path +'.md'
        with open(filename, 'w') as f:
            if not self.tasks:
                f.flush()
            else:
                for todo in self.tasks:
                    task_string = todo['task'].task_string
                    md_string = ''
                    if task_string.lower()[0] == 'x':
                        md_string ='- [x]' + task_string[1:]
                    else:
                        md_string = '- [ ] ' + task_string
                    f.write(md_string)
                    f.write('\n')


class Todo:
    """ 
        Text Format:
        completion (priority) [completion_date]  [creation_date] description [+tags] [@context] [keyval]
    """
    pattern_tags = r'\+\w+'
    pattern_contexts = r'\@\w+'
    pattern_keyvals = r'\w+:\w+'
    pattern_priority = r'\(\w\)'
    pattern_priority = r'\(\w\)'
    pattern_dates = r'\d\d\d\d\-\d\d\-\d\d'
    
    def __init__(self, task_string):
        """Todo Base Class
        :param todo_string
        e.g. ..code python
            t = Todo()
        """
        self.task_string = task_string
        self.hashkey = hashlib.md5(task_string.encode(encoding='utf-8'))
        if task_string is not None and task_string.lower()[0] == 'x':
            self.completion = True
        else:
            self.completion = False
        self.priority = self.get_priority()
        self.tags = self.get_tags()
        self.contexts = self.get_contexts()
        self.keyvals = self.get_keyvals()
        dates = self.get_dates()
        if dates and len(dates)>0:
            completion_date = dates[0]
        else:
            completion_date = None
        if dates and len(dates)>1:
            creation_date = dates[1]
        else:
            creation_date = None
            
        #(self.completion, self.priority, self.completion_date, self.creation_date,
        #    self.description, self.tags, self.context, self.keyvals) = self.parse(task_string)

    def parse(self, pattern, task_string):
        matches = re.findall(pattern, task_string)
        return matches 

    def get_tags(self):
        tags = self.parse(self.pattern_tags, self.task_string)
        return tags

    def get_contexts(self):
        contexts = self.parse(self.pattern_contexts, self.task_string)
        return contexts

    def get_keyvals(self):
        keyvals = self.parse(self.pattern_keyvals, self.task_string)
        return keyvals

    def get_dates(self):
        dates = self.parse(self.pattern_dates, self.task_string)
        return dates

    def get_priority(self):
        matches = self.parse(self.pattern_priority, self.task_string)
        if matches:
            return matches[0][1]
        else:
            return None
    
    def __str__(self):
        return self.task_string
