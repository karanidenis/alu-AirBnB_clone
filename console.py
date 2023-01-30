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
        'User': User,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "Amenity": Amenity}


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = '(hbnb)'

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
        if  not arg:
           print("** class name missing **") 
        elif split_args[0] not in classes.keys():
            print("** class doesn't exist **")

        elif len(split_args) == 1:
            print("** instance id missing **")

        #elif split_args[0] + "." + split_args[1] not in FileStorage().all().keys():
            print("** no instance found **")

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
        args_split = arg.split(' ')
        if len(arg) == 0:
            print("** class name missing **")
        elif args_split[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(args_split) == 1:
            print("** instance id missing **")
        
        user_key = args_split[0] + '.' + args_split[1]
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        if user_key in objects.keys():
            del objects[user_key]
            storage.save()
            return 

        print("** no instance found **")

    def do_all(self, arg):
        """print str representation of all instances
        based on or not on class name"""

        split_arg = arg.split(" ")
        if split_arg[0] not in classes.keys():
            print("** class doesn't exist **")

        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            print([str(obj) for key, obj in objects.items()
                    if key.split('.')[0] == arg])

    def do_update(self, arg):
        """
        updates and instance based on class name and id 
        by adding or updating attribute and save change  in json file
        """
        args = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")            
        else:
            storage = FileStorage()
            storage.reload()
            obj_dict = storage.all()
            user_key = args[0] + args[1]
            attr_name = args[2]
            attr_val = args[3]
            if user_key not in obj_dict:
                print("** no instance found **")
            obj = obj_dict[user_key]
            setattr(obj, attr_name, attr_val)
            obj.save()
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()