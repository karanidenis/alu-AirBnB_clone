#!/usr/bin/python3
"""
The program to launch the HBNB console
entry point of command interpreter
"""

import cmd
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
    prompt = '(hbnb)'

# #dot notation commands
#     def default(self, line):
#         """default method for commands not in the cmd module.
#         For this application it handles the dot notation commands."""

#         if "." in line:

#             command = line.split(".")
#             if command[1] == "all()":
#                 self.do_all(command[0])

#             elif command[1] == "count()":
#                 self.do_count(command[0])

#             elif command[1].startswith("show("):
#                 self.do_show(command[0] + " " + command[1][6:-2])

#             elif command[1].startswith("destroy("):
#                 self.do_destroy(command[0] + " " + command[1][9:-2])

#             elif command[1].startswith("update("):

#                 # remove the model name, and get the rest of the string
#                 command_pattern = re.compile("update\\((.+)\\)")
#                 command_result = command_pattern.search(line).group()

#                 # get Id from the string
#                 id_pattern = re.compile(
#                     "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}"
#                     "-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
#                 )

#                 id = id_pattern.search(command_result)
#                 if id is not None:
#                     id = id.group()
#                 # check if attributes and values are provided in dict format
#                 dict_repr_pattern = re.compile(r"{.+}")
#                 dict_repr = dict_repr_pattern.search(line)

#                 # if it is dict format, execute update for each key value pair
#                 if dict_repr:

#                     # get dict representation
#                     dict_repr = dict_repr.group()
#                     dict_repr = eval(dict_repr)

#                     # excute the update with each key value pair
#                     for key, value in dict_repr.items():
#                         param_to_pass = command[0] + ' ' + \
#                             str(id) + ' ' + key + ' ' + str(value)
#                         self.do_update(param_to_pass)

#                 # if dict format is not provided, it means the attributes
#                 #  and values are provided as parameters
#                 else:

#                     # get the parameters from the string
#                     # and remove the first and last brackets
#                     # the format of parms variable is as follows:
#                     # ex: params:  "b1d6-eaaddf0e76c1", "first_name", "John"
#                     # on the above line id value is trimmed for convenience.
#                     params = command_result[7:-1]
#                     # print("params: ", params)

#                     # the following for loop is to check if user entered
#                     # values with spaces after comma(,).
#                     # If the user did not enter spaces after comma(,)
#                     # it will create a problem while slicing the string to
#                     # get the values, specifically value parameter is extracted
#                     # without error given space is provided after comma(,).
#                     index_counter = 0
#                     for param in params.split(","):

#                         if index_counter >= 1 and not param.startswith(" "):
#                             print(
#                                 "Insert spaces after comma(,) "
#                                 "to divide parameters"
#                             )
#                             return
#                         index_counter += 1

#                     # get the id, attribute and value from the string
#                     attr = params.split(",")[1][2:-1]
#                     value = params.split(",")[2][1:]

#                     # incase the value of variable value is int pass it on eval
#                     # to convert it to int, if it is not int, it will throw an
#                     # exception, in that case we will not pass it on eval.
#                     try:
#                         eval(value)
#                         value = eval(value)
#                     except Exception as e:
#                         pass

#                     # create the parameter string to pass on to do_update
#                     param_to_pass = command[0] + ' ' + \
#                         str(id) + ' ' + attr + ' ' + str(value)
#                     self.do_update(param_to_pass)
#             else:
#                 print("*** Unknown syntax: {}".format(line))
#         else:
#             print("*** Unknown syntax: {}".format(line))

#commands used on the console
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
        based on class name and id"""

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
        delete an instance based on class name
        and id and save changes in Json file
        """
        args = arg.split(' ')
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")

        user_key = args[0] + '.' + args[1]
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
        """print str representation of all instances
        based on or not on class name"""

        # storage = FileStorage()
        # storage.reload()
        # objects = storage.all()
        # if len(arg) < 1:
        #     print([str(obj) for obj in objects.values()])
        # elif arg not in classes.keys():
        #     print("** class doesn't exist **")
        # else:
        #     for key, obj in objects.items():
        #         if key.split('.')[0] == arg:
        #             print(str(obj))

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
        updates and instance based on class name and id
        by adding or updating attribute and save change  in json file
        """
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        args = arg.split(" ")
        cls_name = args[0]
        class_id = args[1]
        user_key = cls_name + '.' + class_id
        attr_name = args[2]
        attr_val = args[3]
        if not cls_name:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
        if len(args) == 2:
            print("** attribute name missing **")
        if len(args) == 3:
            print("** value missing **")
        if user_key not in classes.keys():
            print("** class doesn't exist **")
            return
        if user_key in obj_dict.keys():
            obj = obj_dict[user_key]
            setattr(obj, attr_name, attr_val)
            obj.save()
        else:
            print("** no instance found **")

    def do_count(self, args):
        """
        print all objects stored
        """
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        if not args:
            print(len([str(obj) for obj in objects.values()]))
        
        elif args not in classes.keys():
            print("** class doesn't exist **")
        
        else:
            print(len([str(obj) for key, obj in objects.items()
                    if key.split(' ')[0] == args]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
