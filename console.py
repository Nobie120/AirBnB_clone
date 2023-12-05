#!/usr/bin/python3
""" The CLI module """
import re
import cmd


class HBNBCommand(cmd.Cmd):
    """ The Clasas for perfoming CLI
    operatinons """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """ command for exiting the CLI """
        return True

    def do_EOF(self, line):
        """ command for quitting """
        return True

    def emptyline(self):
        """ Handle cases when the user
        doesn't type any command """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
