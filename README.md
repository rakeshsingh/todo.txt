# todo.txt
Command line lightweight todo tool with readable storage , written in python.

## Usage
```

python cli.py --help
Usage: cli.py [OPTIONS]

Options:
  --version            Show the version and exit.
  -u, --use TEXT       use `name` file to store your toodo list
  -a, --add TEXT       add a new todo task
  -e, --edit TEXT...   edit todo by id - usage: tasks -e 2 ``text``
  -r, --remove TEXT    remove todo by id(s)
  -c, --complete TEXT  complete todo tasks by id(s) - usage: tasks -c 1,2
  -l, --list           show all tasks
  -ld, --done          show all done tasks
  -cl, --clear         clear all tasks, need confirm!!
  --help               Show this message and exit.
```
## Storage
`todos` uses `./todo.txt`, if doesn't exist, `todos` will create a empty file in `./todo.txt`.

If you excute `todos --use your_file_name`, then the file will change to ``your_file_name``, after then
every your todos will storage to this file.
Want to change back, just execute `todos --use your_file_name`. So easy!!

So you don't care about this file, `todos` will operate it.
The storage format is readbale, is ths `GitHub Flavored Markdown Task list`

    1. [o] A Done todo
    2. [x] A Waiting todo

[Example todo text]
```

```

## Installation
`pip install todo.txt`

## Contributors
https://github.com/MrKiven/Todo.py/graphs/contributors

## TODO
take apart sub commands
