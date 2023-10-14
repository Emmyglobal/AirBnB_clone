#!/usr/bin/python3
"""
A program that contains the entry point of the command interpreter
"""
import cmd

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program
        """
        return True

    def emptyline(self):
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
