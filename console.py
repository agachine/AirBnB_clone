#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")
    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in storage._FileStorage__objects:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key in storage._FileStorage__objects:
            print(storage._FileStorage__objects[key])
        else:
            print("** no instance found **")


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        args = arg.split()
        if args and args[0] not in storage._FileStorage__classes:
            print("** class doesn't exist **")
        else:
            instances = [str(instance) for instance in storage.all().values()]
            print(instances)


    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                instance = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3].strip('"')
                if hasattr(instance, attr_name):
                    attr_type = type(getattr(instance, attr_name))
                    try:
                        setattr(instance, attr_name, attr_type(attr_value))
                        instance.save()
                    except ValueError:
                        print("** invalid value for attribute **")
                else:
                    print("** attribute doesn't exist **")
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
