#!/usr/bin/python3
"""module for the entry point of my cmd interpreter"""

import cmd
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
class HBNBCommand(cmd.Cmd):
    """class for cmd interpreter"""
    prompt = "(hbnb)"
    class_list = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

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
                    try:                 
                        my_key = ("{}.{}".format(Args[0], Args[1]))
                        print(models.storage.all()[my_key])
                    except:
                        print("** no instance found **")

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
                    try:
                        my_key = ("{}.{}".format(Args[0], Args[1]))
                        del models.storage.all()[my_key]
                        models.storage.save()
                        models.storage.reload()
                    except:
                        print("** no instance found **")

    def do_all(self, line):
            """Prints all string representation of all instances
            based or not on the class name.
            Ex: $ all BaseModel or $ all"""
            Args = line.split()
            my_dict = models.storage.all()
            my_list = []
            if len(line) ==  0:
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
        my_dict = models.storage.all()
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
