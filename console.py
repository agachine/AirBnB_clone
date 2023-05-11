#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Exit command to exit the program using EOF
        """
        print("")
        return True

    def emptyline(self):
        """
        Do nothing on empty line + ENTER
        """
        pass

    def help_help(self):
        """
        Print help information
        """
        print("List available commands with \"help\" or detailed help with \"help cmd\".")
        print("Quit with \"quit\" or \"EOF\".")

    def help_quit(self):
        """
        Print quit command information
        """
        print("Quit command to exit the program.")
        print("Usage: quit")

    def help_EOF(self):
        """
        Print EOF command information
        """
        print("Exit command to exit the program using EOF.")
        print("Usage: Ctrl-D")

if __name__ == "__main__":
    HBNBCommand().cmdloop()

