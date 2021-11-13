#!/usr/bin/python3
"""module for the entry point of my cmd interpreter"""

import cmd
class HBNBCommand(cmd.Cmd):
    """class for cmd interpreter"""
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """End of file"""
        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit the program"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
