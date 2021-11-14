#!/usr/bin/python3
"""module for the entry point of my cmd interpreter"""

import cmd
<<<<<<< HEAD
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
class HBNBCommand(cmd.Cmd):
    """class for cmd interpreter"""
    prompt = "(hbnb)"
    class_list = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
=======
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
>>>>>>> d2207433ceec622b21b04e06da5d8b55c3e0f77f

    def do_EOF(self, line):
        """End of file"""
        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel"""
        Args = line.split()
        if len(line) <= 0:
            print("** class name missing **")
        else:
            if Args[0] not in self.class_list:
                print("** class doesn't exist **")
            else:
                my_object = eval(Args[0])()
                my_object.save()
                print(my_object.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234."""
        Args = line.split()
        if len(line) <= 0:
            print("** class name missing **")
        else:
            if len(Args) == 1:
                if Args[0] not in self.class_list:
                    print("** class dosen't exist **")
                else:
                    print("** instance id missing **")
            else:
                if Args[0] not in self.class_list:
                    print("** class dosen't exist **")
                else:
                    my_key = ("{}.{]".format(Args[0], Args[1]))
                    if my_key not in storage.all():
                        print("** no instance found **")
                    else:
                        print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234."""
        Args = line.split()

        if len(line) <= 0:
            print("** class name missing **")
        else:
            if len(Args) == 1:
                if Args[0] not in self.class_list:
                    print("** class dosen't exist **")
                else:
                    print("** instance id missing **")
            else:
                if Args[0] not in self.class_list:
                    print("** class dosen't exist **")
                else:
                    my_key = ("{}.{]".format(Args[0], Args[1]))
                    if my_key not in storage.all():
                        print("** no instance found **")
                    else:
                        del storage.all()[key]
                        storage.save()
                        storage.reload()

    def do_all(self, line):
            """Prints all string representation of all instances
            based or not on the class name.
            Ex: $ all BaseModel or $ all"""
            Args = line.split()
            my_dict = models.storage.all()
            my_list = []
            if Args[0] == None or Args[0] == "":
                for key in my_dict.keys():
                    my_list.append(str(my_dict[key]))
                print(my_list)
            else:
                if Args[0] not in self.class_list:
                    print("** class doesn't exist **")
                else:
                    for k, v in my_dict.items():
                        if k.split(".")[0] == Args[0]:
                            my_list.append(str(v))
                            print(my_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        Usage: update <class name> <id> <attribute name> "<attribute value>"""
        Args = line.split()
        my_dict = model.storage.all()
        if len(line) <= 0:
            print("** class name missing **")
        else:
            if len(Args) == 1:
                if Args[0] not in self.class_list:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            elif len(Args) == 2:
                if Args[0] not in self.class_list:
                    print("** class doesn't exist **")
                else:
                    if Args[0]+"."+Args[1] not in my_dict.keys():
                        print("** no instance found **")
                    else:
                        if Args[2] == None or Args[2] == "":
                            print("** attribute name missing **")
                        else:
                            if Args[3] == None or Args[3] == "":
                                print("** value missing **")
                            else:
                                my_instance = Args[0]
                                _id = Args[1]
                                attr_name = Args[2]
                                attr_value =Args[3]
                                if hasattr(eval(my_instance, attr_name)):
                                    my_attr = getattr(eval(my_instance, attr_name))
                                    my_type = eval(type(my_attr).__name__)
                                    if my_type == int:
                                        attr_value = int(float(attr_value))
                                    key = my_instance+"."+_id
                                    setattr(my_dict[key], attr_name, my_type(attr_value))
                                else:
                                    key = my_instance+"."+_id
                                    setattr(my_dict[key], attr_name, attr_value)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
