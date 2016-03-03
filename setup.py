# -*- coding: utf-8 -*-

import os
import re
from setuptools import setup, find_packages


def _get_version():
    v_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'Todos', '__init__.py')
    ver_info_str = re.compile(r".*version_info = \((.*?)\)", re.S). \
        match(open(v_file_path).read()).group(1)
    return re.sub(r'(\'|"|\s+)', '', ver_info_str).replace(',', '.')

entry_points = [
    # todo
    "todos = Todos.todo:todos"
]

setup(
    name="todos",
    version=_get_version(),
    description="Command line lightweight todo tool with readable storage ,\
            written in Py",
    long_description=open("README.md").read(),
    author="kiven",
    author_email="kiven.mr@gmail.com",
    packages=find_packages(),
    url="https://github.com/MrKiven/Todo.py",
    entry_points={"console_scripts": entry_points},
    install_requires=[
        'click==5.1',
        'emoji==0.3.9'
    ],

)
