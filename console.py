#!/usr/bin/python3
"""contains entry point of the command interpreter
"""
import cmd
import datetime
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """command line interprete

    Args:
        cmd (_cmd_): _python module for CLI interpretion_
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel,
               "User": User,
               "Amenity": Amenity,
               "City": City,
               "Place": Place,
               "Review": Review,
               "State": State}

    def do_quit(self, args):
        """quit command exits out of the command interpreter

        Args:
            args (_str_): _any argument in cli_
        """
        quit()

    def do_EOF(self, args):
        """_EOF command exits out of the command interpreter_

        Args:
            args (_str_): _any argument in cli_
        """
        quit()

    def do_help(self, args):
        """_list all help details for each command_

        Args:
            args (_str_): _any argument in cli_
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """returns back to prompt when line is empty and enter is pressed
        """
        return

    def do_create(self, args):
        """creates a new instance of any class

        Args:
            args (_str_): _name of a class in AirBnB_
        """
        if not args:
            print("** class name missing **")
            return
        args = args.split(" ")
        if len(args) == 1 and args[0] in self.classes:
            new_instance = eval(f"{args[0]}()")
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """prints string representation of instance

        Args:
            args (_string_): 2 strings name and id separated with space
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1 and args[0] in self.classes:
            print("** instance id missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            instance_id = "{}.{}".format(args[0], args[1])
            if instance_id in instances:
                print(instances[instance_id])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """deletes instance

        Args:
            args (_str_): _2 name of class and id of instance_
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1 and args[0] in self.classes:
            print("** instance id missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            instance_id = "{}.{}".format(args[0], args[1])
            try:
                del instances[instance_id]
                storage.on_deletion(instances)
                storage.save()
            except Exception:
                print("** no instance found **")

    def do_all(self, args):
        """prints a string representation of all instances

        Args:
            args (_str_): _optional. name of class_
        """
        objects = storage.all()
        instances = []
        if not args:
            instances = [{k: str(v) for k, v in objects.items()}]
            print(instances)
            return
        tokens = args.split(" ")
        if tokens[0] in self.classes.keys():
            instance = [{k: str(v) for k, v in objects.items()
                         if k.startswith(tokens[0])}]
            print(instance)
            return
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """update instances

        Args:
            args (_str_): _4 strings class, id, attr, value_
        """
        tokens = args.split(" ")
        objects = storage.all()
        if len(tokens) >= 5:
            return
        if not args:
            print("** class name missing **")
            return
        elif len(tokens) == 1:
            if tokens[0] not in self.classes:
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return
        elif len(tokens) == 2:
            if tokens[0] not in self.classes:
                print("** class doesn't exist **")
                return
            name = f"{tokens[0]}.{tokens[1]}"
            if name not in objects:
                print("** no instance found **")
                return
            print("** attribute name missing **")
            return
        elif len(tokens) == 3:
            if tokens[0] not in self.classes:
                print("** class doesn't exist **")
                return
            name = f"{tokens[0]}.{tokens[1]}"
            if name not in objects:
                print("** no instance found **")
                return
            print("** value missing **")
            return
        else:
            if tokens[0] not in self.classes:
                print("** class doesn't exist **")
                return
            name = f"{tokens[0]}.{tokens[1]}"
            if name not in objects:
                print("** no instance found **")
                return
            else:
                obj = objects[name]
                not_to_change = ["id", "created_at", "updated_at"]
                if tokens[2] not in not_to_change:
                    obj = obj.to_dict()
                    obj.update({tokens[2]: tokens[3]})
                    obj.update({'updated_at': datetime.datetime.today()
                                .isoformat()})
                    obj = self.classes[tokens[0]](**obj)
                    objects.update({name: obj})
                    storage.on_deletion(objects)
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
