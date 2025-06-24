#!/usr/bin/python3
"""
console module
"""
import cmd
import os 

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

if __name__ == '__main__':
    WKTCommand().cmdloop()