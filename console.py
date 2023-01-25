#!/usr/bin/python3
"""
entry point of command interpreter
"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = '(hbnb)'
    classes = ['BaseModel']

    def do_quit(self, line):
        """ if quit is used exit"""
        return True

    def do_EOF(self, line):
        """if EOF, exit"""
        print()
        return True

    def emptyline(self):
        """should do nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()