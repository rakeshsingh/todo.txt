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

[Example todo text]

```
X (A) one more another task test  +project @context dfdadfd 2018-08-02 #2018-08-02 due:2018-08-20
(B) one more another task test  +project @context dfdadfd 2018-08-02 #2018-08-02 due:2018-08-20
(C) another task with lower priority +project
(D) 4 task with lower priority +project
(E) 5 task with lower priority +project

```

## Installation
`pip install todo.txt`

## Contributors
https://github.com/rakeshsingh/todo.txt/graphs/contributors

## TODO
1. code to write generate github compatible todo.txt file

