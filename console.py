#!/usr/bin/python3
""" The CLI module """
import re
import cmd
from models import base_model, storage


BaseModel = base_model.BaseModel
file_storage = storage


class HBNBCommand(cmd.Cmd):
    """ The Clasas for perfoming CLI
    operatinons """

    prompt = '(hbnb) '
    errors = [
            '** class name missing **',
            "** class doesn't exist **",
            '** instance id missing **',
            '** no instance found **',
            '** attribute name missing **',
            '** value missing **',
        ]

    def __error(self, arg):
        """" Handles some errors """
        error = 0
        if not arg:
            print(HBNBCommand.errors[0])
            error = 1
        else:
            class_name = arg.split()[0]
            if class_name not in globals() or not issubclass(globals()[class_name], BaseModel):
                print(HBNBCommand.errors[1])
                error = 1
        return error

    def __error_id(self, arg):
        """ Handles Th Casee when the id missing """
        error = 0
        if len(arg.split()) < 2:
            print(HBNBCommand.errors[2])
            error = 1
        return error

    def do_quit(self, line):
        """ command for exiting the CLI """
        return True

    def do_EOF(self, line):
        """ command for quitting """
        return True

    def emptyline(self):
        """ Handle cases when the user
        doesn't type any command """
        pass

    def default(self):
        """ default errors """
        pass

    def handle_keyboard_interrupt(self):
        """ handle ctrl+c """
        print("Use 'quit' or 'EOF' to exit")

    def do_create(self, arg):
        """  Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id """
        class_name = arg
        error = self.__error(arg)
        if not error:
            class_obj = globals()[class_name]
            instance = class_obj()
            print(instance.id)
            instance.save()

    def do_show(self, arg):
        """ Prints the string representation of an
        instance based on the class name and id. """
        error = self.__error(arg)
        if not error:
            error += self.__error_id(arg)
        if not error:
            objects = file_storage.all()
            args = arg.split()
            key = ".".join(args)
            try:
                print(objects[key])
            except Exception:
                print(HBNBCommand.errors[3])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class
        name and id (save the change into the JSON file). """
        error = self.__error(arg)
        if not error:
            error += self.__error_id(arg)
        if not error:
            objects = file_storage.all()
            args = arg.split()
            key = '.'.join(args)
            try:
                del objects[key]
                file_storage.save()
            except Exception:
                print(HBNBCommand.errors[3])

    def do_all(self, arg):
        """  Prints all string representation of all
        instances based or not on the class name """
        args = arg.split()
        objects = file_storage.all()
        if len(args) < 2:
            filtered = [str(instance) for instance in objects.values()]
            print(filtered)
        else:
            error = self.__error(arg)
            if not error:
                filtered = [
                        str(v) for k, v in objects.items() if args[1] in k
                        ]
                print(filtered)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
