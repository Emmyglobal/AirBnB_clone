#!/usr/bin/python3
"""
A program that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    __classes = ["BaseModel", "User"]

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel
        """
        args = arg.split()

        if len(args) == 0:
            """Prints if class is missing
            """
            print("** class name missinng **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")

        else:
            new_object = eval(f"{args[0]}")()
            print(new_object.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based ont the class name
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])
    
    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name
        """
        args = arg.split()

        if len(args) == 0:
            print([str(value) for val in storage.all().values()])
        elif args[0] not in sel.__classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in storage.all().items() if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute
        """

        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
