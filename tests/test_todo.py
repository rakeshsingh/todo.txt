import unittest
import os

from todo.todo import Todo
from todo.constants import DEFAULT_TODO_FILE

class TestTodo(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.td = Todo('x (A) 2018-08-20 2018-08-01 this is a test task +project1 @context1 author:rakesh')
        self.td1 = Todo('x (A) 2018-08-20 2018-08-01 this is a test task  @context1 author:rakesh')

    def test_init(self):
        self.assertEqual(os.path.exists(DEFAULT_TODO_FILE), True)
    
    def test_parse(self):
        testtags = ['+project1']
        self.assertEqual(self.td.parse(r'\+\w+', self.td.task_string), testtags)

    def test_get_tags(self):
        testtags = ['+project1']
        self.assertEqual(self.td.parse(self.td.pattern_tags, self.td.task_string), testtags)
    
    def test_get_tags_1(self):
        self.assertEqual(len(self.td.parse(self.td1.pattern_tags, self.td1.task_string)),0)
    
    def test_get_contexts(self):
        testcontexts = ['@context1']
        self.assertEqual(self.td.parse(self.td.pattern_contexts, self.td.task_string), testcontexts)

    def test_get_keyvals(self):
        keyvals = ['author:rakesh']
        self.assertEqual(self.td.parse(self.td.pattern_keyvals, self.td.task_string), keyvals)

    def test_true(self):
        self.assertEqual('foo'.upper(), 'FOO')
