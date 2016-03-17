# Todo.py
Command line lightweight todo tool with readable storage , written in Py.

## Usage
see `todos --help`

    todos --help
    Usage: todos [OPTIONS]

    Options:
      --version                Show the version and exit.
      --what                   show current use todo file's name
      --use TEXT               use `name` file to store your todos
      --done                   show all done todos
      -n, --new TEXT           new todo
      -c, --complete_ids TEXT  complete todo by id(s) - usage: todos -c 1,2
      -e, --edit TEXT...       edit todo by id - usage: todos -e 2 ``text``
      -r, --remove TEXT        remove todo by id(s)
      --all                    show all todos
      --clear                  clear all todos, need confirm!!
      --help                   Show this message and exit.

## Storage
`todos` will always use `./Todos.txt`, if doesn't exist, `todos` will new an
empty file in `./Todos.txt`.

If you excute `todos --use your_file_name`, then the file will change to ``your_file_name``, after then
every your todos will storage to this file.
Want to change back, just execute `todos --use your_file_name`. So easy!!

So you don't care about this file, `todos` will operate it.
The storage format is readbale, is ths `GitHub Flavored Markdown Task list`

    1. [o] A Done todo
    2. [x] A Waiting todo

## Installation
`pip install todos`

## Contributors
https://github.com/MrKiven/Todo.py/graphs/contributors

## TODO
take apart sub commands
