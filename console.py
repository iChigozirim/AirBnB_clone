#!/usr/bin/python3
"""Defines the AirBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the AirBnB command interpreter."""
    prompt = "hbnb "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """On receiving end-of-file signal, exit the program"""
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
