#!/usr/bin/python3
"""
The program to launch the HBNB console
entry point of command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = '(hbnb)'
    classes = ['BaseModel']

    def do_quit(self, arg):
        """ if quit is used exit"""
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
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new = HBNBCommand.className[arg]()
            #HBNBCommand.className[arg].save(new)
            #new = eval(arg)()
            new.save()
            print(new.id)
    
    def do_show(self, arg):
        """print string representation of an instance 
        based on class name and id"""

        split_args = arg.split(" ")
        if  not arg:
           print("** class name missing **") 
        elif split_args[0] not in self.classes:
            print("** class doesn't exist **")

        elif len(split_args) == 1:
            print("** instance id missing **")

        elif split_args[0] + "." + split_args[1] not in FileStorage.__objects.keys():
            print("** no instance found **")
        
        else:
            print(FileStorage.__objects[split_args[0]+"."+split_args[1]])

    def do_destroy(self, arg):
        """
        delete an instance based on class name 
        and id and save changes in Json file
        """
        args_split = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif args_split[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif args_split[0]+'.'+args_split[1] not in FileStorage.__objects.keys():
            print("** no instance found **")
        else:
            del FileStorage.__objects[args_split[0]+'.'+args_split[1]].save()

    def do_all(self, arg):
        """print str representation of all instances
        based on or not on class name"""

        split_arg = arg.split(" ")
        if split_arg[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            list_Obj = []
            for k, val in FileStorage.__objects.items():
                if split_arg[0] in k:
                    list_Obj.append(str(val))
            print(list_Obj)
        if len(arg) == 0: #if not arg
            obj_list = []
            for key, vals in FileStorage._objects.items():
                obj_list.append(str(vals))
            if len(str(obj_list)) > 0:
                print(obj_list)

    def do_update(self, arg):
        """
        updates and instance based on class name and id 
        by adding or updating attribute and save change  in json file
        """
        args = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif args[0]+'.'+args[1] not in FileStorage.__objects.items():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj_dict = FileStorage().all()
            value = type(eval(args[3]))
            third_arg = args[3]
            third_arg = third_arg.strip("'")
            third_arg = third_arg.strip('"')
            for key in obj_dict:
                setattr(obj_dict.get(key), args[2], value(third_arg))
                obj_dict[key].save()
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()