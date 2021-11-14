#!/usr/bin/python3
"""module for the entry point of my cmd interpreter"""

import cmd
from shlex import split

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


def check_args(args):
    """checks if args is valid
    Args:
        args (str): the string containing the arguments passed to a command
    Returns:
        Error message if args is None or not a valid class, else the arguments
    """
    arg_list = split(args)

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in CLASSES:
        print("** class doesn't exist **")
    else:
        return arg_list

class HBNBCommand(cmd.Cmd):
    """class for cmd interpreter"""
    prompt = "(hbnb)"
    __classes = {
                "BaseMode",
                "Amenity",
                "City",
                "Place",
                "Review",
                "State",
                "User"
    }

    def emptyline(self):
        "The interpreter does nothing when it gets an empty line"
        pass

    def default(self, args):
        pass

    def do_create(self, arg):
        """
        Creates a new instance of the base model,
        saves it to JSON file,
        then prints its id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, argv):
        pass

    def do_destroy(self, argv):
        pass

    def do_all(self, argv):
        pass

    def do_update(self, argv):
        pass

    def do_EOF(self, line):
        """End of file"""
        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit the program"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
