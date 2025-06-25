#!/usr/bin/python3
"""
console module
"""
import cmd
import os 
import models
from models.base_model import BaseModel


classes = {"BaseModel": BaseModel}

class WKTCommand(cmd.Cmd):
    """contains the entry point for the command interpreter.inherits from the cmd class
    """
    intro = 'Welcome ot the workout tracker shell.\n'
    prompt = '(wrkt) '
    file = None

    def do_clear(self, line):
        """clears the console screen"""
        # for windows
        if os.name == 'nt':
            _ = os.system('cls')

        # for unix/linux/
        else:
            _ =os.system('clear')

    def do_quit(self, line):
        """command to exit the program"""
        print("Thank you for using the shell")
        return True
    
    def do_EOF(self, line):
        """Exit the program, similar to quit"""
        return True
    
    def emptyline(self):
        """Handles empty input, overides to do nothing"""
        return False
    
    def do_create(self, arg):
        """Creates a new instance of a given class"""
        arguments = arg.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return False
        if arguments[0] in classes:
            object = classes[arguments[0]]() # creates a new instance of the specified class
        else:
            print("** class doesn't exist **")
            return 
        print(object.id)
        object.save()

    def do_show(self, arg):
        """prints the string representation of an instance
        based on the clas name and id"""
        arguments = arg.split()
        # check if class name is provided
        if len(arguments) == 0:
            print(" ** class name doesnot exist")
            return False
        # check if class name provided dose exist
        if arguments[0] not in classes:
            print(" ** class doesnot exist ")
            return False
        # check if instance id is not provided
        if len(arguments) < 2:
            print(" ** instance id is missing **")
            return False
        # check if a given instance exists in storage
        instance_key = f"{arguments[0]}.{arguments[1]}"
        if instance_key in models.storage.all():
            print(models.storage.all()[instance_key])
        else:
            print(" ** no instance found **")

    def do_destroy(self,arg):
        """destorys an instance based on the class name and id"""
        arguments = arg.split()
        if len(arguments) == 0:
            print(" ** class  name missing ")
            return False
        if arguments[0] not in classes:
            print(" ** class doesnot exist")
            return False
        if len(arguments) < 2:
            print("** instance id missing ")
            return False
        # check if the instance does exist in storage 
        instance_key = f"{arguments[0]}.{arguments[1]}"

        # delete instance if present in storage
        if instance_key in models.storage.all():
            del models.storage.all()[instance_key]
            models.storage.save()
        else:
            print(" **No instance found **")
            
    def do_all(self, arg):
        """Prints all string representation of all instances based 
        or not on the class name"""
        arguments = arg.split()
        if len(arguments) > 0:
            class_name = arguments[0]
            if class_name not in classes:
                print("** class doesnot exist **")
                return False 
        objects = models.storage.all()
        all_instaces = []

        if len(arguments) > 0:
            all_instaces = [str(obj) for key, obj in objects.items() if key.startswith(class_name)]
        else:
            all_instaces = [str(obj) for obj in objects.values()]
        print(all_instaces)
    
    def do_update(self, arg):
        """updates an instance based on the class name and id
    by adding or updating atribute"""
        arguments = arg.split()

        # Restric multiple updating/ addition of attribute at ones
        if len(arguments) > 4:
            print("** only one attribute can be updated at a time")
            return False 
        #Check if class name is missing
        if len(arguments) == 0:
            print("** class name missing **")
            return False
        # check if class name doesn't exist
        if arguments[0] not in classes:
            print("** class doesnot exist **")

        # check if id is missing
        if len(arguments) < 2:
            print("** instance id is missing ")
            return False
        # constract the instance key 
        instance_key = f"{arguments[0]}.{arguments[1]}"
        if instance_key not in models.storage.all():
            print("** no instance found **")
            return False
        # check if attribute name is provided
        if len(arguments) < 3:
            print("** attribute name missing **")
            return False
        # check if attribute value is provided
        if len(arguments) < 4:
            print("** value missing")
            return False
        
        # Retrieve the obj from storage 
        obj = models.storage.all()[instance_key]

        # extract attribute name and value
        attribute_name = arguments[2]
        attribute_value = arguments[3]

        # skip restricted attributes
        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** restricted attribute ")
            return False
        
        # Ensure attribute type casting is applicable 
        if hasattr(obj, attribute_name):
            attr_type = type(getattr(obj, attribute_name))
            try:
                attribute_value = attr_type(attribute_value)
            except (ValueError, TypeError):
                pass
        else:
            attribute_value = str(attribute_value)
            setattr(obj, attribute_name, attribute_value)
            obj.save()


    
        







if __name__ == '__main__':
    WKTCommand().cmdloop()