#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import cmd
from models import BaseModel


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

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        """
        try:
            class_name, id = line.split()
            obj = BaseModel(class_name, id)
            obj.save()
            print(id)
        except ValueError:
            print("class name missing")
        except AttributeError:
            print("class doesn't exist")

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        try:
            class_name, id = line.split()
            obj = BaseModel.get(class_name, id)
            print(obj)
        except ValueError:
            print("class name missing")
        except AttributeError:
            print("class doesn't exist")
        except KeyError:
            print("no instance found")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        """
        try:
            class_name, id = line.split()
            BaseModel.destroy(class_name, id)
        except ValueError:
            print("class name missing")
        except AttributeError:
            print("class doesn't exist")
        except KeyError:
            print("no instance found")

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        try:
            class_name = line.strip()
            if class_name:
                instances = BaseModel.all(class_name)
            else:
                instances = BaseModel.all()
            for instance in instances:
                print(instance)
        except AttributeError:
            print("class doesn't exist")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
        """
        try:
            class_name, id, attribute, value = line.split()
            obj = BaseModel.get(class_name, id)
            setattr(obj, attribute, value)
            obj.save()
        except ValueError:
            print("class name missing")
        except AttributeError:
            print("class doesn't exist")
        except KeyError:
            print("no instance found")
        except AttributeError:
            print("attribute name missing")
        except TypeError:
            print("value missing")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
