#!/usr/bin/python3
"""
A program that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    __classes = {
            "BaseModel" : BaseModel,
            "User" : User,
            "City" : City,
            "State" : State,
            "Place" : Place,
            "Review" : Review,
            "Amenity" : Amenity
    }

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


    def do_count(self, arg):
        """ Counts the number of instances of a specific class """

        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            __classes = arg[0]
            count = len([key for key in storage.all().keys() if key.split('.')[0] == __classes])
            print(count)


    def do_show_instance(self, arg):
            """ Show an instance by class name and id using <class name>.show(<id>) """
            if not arg:
                print("** class name missing **")
                return

            args = arg.split('.')
            if len(args) < 2:
                print("** instance id missing **")
                return

            __classes = args[0]
            instance_id = args[1]
            key = __classes + "." + instance_id

            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")


    def do_destrpy_instance(self, arg):
        """ Destroy an instance by class name and id using <class name>.destroy(<id>) """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(".")
        if len(args) < 2:
            print("** instance id missing **")
            return

        __classes = args[0]
        instance_id = args[1]
        key = __classes + "." + instance_id

        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")
            return

    def do_update_instance(self, arg):
        """ Update an instance by class name and id using <class name>.update(<id>, <dictionary representation>) """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(".")
        if len(args) < 2:
            print("** instance id missing **")
            return

        __classes = args[0]
        instance_id = args[1]
        key = __classes + "." + instance_id

        if key not in storage.all():
            print("** no instance found **")
            return

        args = arg.split(",", 1)
        if len(args) < 2:
            print("** dictionary representation missing **")
            return


        try:
            update_dict = eval(args[1])
            if not isinstance(update_dict, dict):
                print("** invalid dictionary representation **")
                return

            obj = storage.all()[key]
            for key, value in update_dict.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
                else:
                    print("** attribute {} doesn't exist **".format(key))
                    obj.save()
        except SyntaxError:
            print("** invalid dictionary representation **")




if __name__ == '__main__':
    HBNBCommand().cmdloop()
