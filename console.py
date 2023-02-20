#!/usr/bin/python3
"""
The program to launch the HBNB console
entry point of command interpreter
"""

import cmd
import sys
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage

classes = {"BaseModel": BaseModel,
           "User": User,
           "City": City,
           "Place": Place,
           "Review": Review,
           "State": State,
           "Amenity": Amenity}


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = '(hbnb)' if sys.__stdin__.isatty() else ''

    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.
        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == '}'\
                            and type(eval(pline)) == dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

# commands used on the console
    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """if EOF, exit"""
        print()
        return True

    def emptyline(self):
        """should do nothing"""
        pass

    def do_create(self, arg):
        """
        create a new instance of Basemodel
        save it to Json file then print id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in classes.keys():
            print("** class doesn't exist **")
        else:
            new = classes[arg]()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """print string representation of an instance
        based on class name and id
        Usage: show <class> <id> or <class>.show(<id>)"""

        split_args = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif split_args[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(split_args) == 1:
            print("** instance id missing **")
        else:
            user_key = split_args[0] + '.' + split_args[1]
            storage = FileStorage()
            storage.reload()
            objects = storage.all()
            if user_key in objects.keys():
                print(objects[user_key])
                return

            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Usage: destroy <class> <id> or <class>.destroy(<id>)
        delete an instance based on class name
        and id and save changes in Json file
        """
        args = arg.split(' ')
        if len(arg) <1:
            print("** class name missing **")
            return
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        user_name = args[0]
        user_id = args[1]
        user_key = "{}.{}".format(user_name, user_id)
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        if user_key in objects.keys():
            del objects[user_key]
            storage.save()
            return
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Usage: all or all <class> or <class>.all()
        print str representation of all instances
        based on or not on class name"""

        args = arg.split(" ")
        class_name = args[0]
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        if class_name:
            if class_name not in classes.keys():
                print("** class doesn't exist **")
                return
        else:
            for obj in objects.values():
                print([str(obj)])

        if class_name in classes:
            for key, obj in objects.items():
                if class_name in key:
                    print([str(obj)])

    def do_update(self, arg):
        """
        Usage: update <class> <id> <attribute_name> <attribute_value> or"
        " <class>.update(<id>, <attribute_name>, <attribute_value"
        ">) or <class>.update(<id>, <dictionary>)
        updates and instance based on class name and id
        by adding or updating attribute and save change  in json file
        """
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        found = False
        key = "{}.{}".format(class_name, instance_id)
        all_instances = models.storage.all()
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]

        for key, instance in all_instances.items():
            if instance_id in key:
                found = True
                if len(args) < 5:
                    setattr(instance,
                            attribute_name,
                            attribute_value.strip('"'))
                    models.storage.save()

        if not found:
            print("** no instance found **")
            return

    def do_count(self, args):
        """
        Usage: count <class> or <class>.count()
        print all objects stored
        """
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        count = 0
        # if not args:
        #     print(len([str(obj) for obj in objects.values()]))

        if args not in classes.keys():
            print("** class doesn't exist **")

        else:
            # print(len([str(obj) for key, obj in objects.items()
            #         if key.split('.')[0] == args]))
            for key, value in objects.items():
                if args[0] in key:
                    count += 1
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
