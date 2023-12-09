#!/usr/bin/python3
""" The CLI module """
import re
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


file_storage = FileStorage()


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
            if class_name not in globals() or not issubclass(
                    globals()[class_name], BaseModel):
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

    def default(self, line):
        """ default errors """
        args = (line.replace("(", ".").replace(")", ".").replace(
            '"', "").replace(",", "").split("."))
        functions = {"all": self.do_all, "update": self.do_update,
                "show": self.do_show, "destroy": self.do_destroy}
        try:
            cmd_args = args[0] + " " + args[2]
            func = functions[args[1]]
            func(cmd_args)

        except Exception:
            print("** Invalid Syntax: ", line, "**")

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
        if len(args) < 1:
            filtered = [str(instance) for instance in objects.values()]
            print(filtered)
        else:
            error = self.__error(arg)
            if not error:
                filtered = [
                        str(v) for k, v in objects.items() if args[0] in k
                        ]
                print(filtered)

    def do_update(self, arg):
        """  Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file) """
        file_storage.reload()
        objects = file_storage.all()
        error = self.__error(arg)
        if not error:
            error += self.__error_id(arg)
        args = arg.split()
        key = ".".join([args[0], args[1]])
        if len(arg) < 3:
            print('** attribute name missing **')
            error += 1
            return
        elif len(arg) < 4:
            print('** value missing **')
            error += 1
            return
        if not error:
            try:
                obj_value = objects[key]
            except KeyError:
                print("** no instance found **")
                return
            if type(args[3]) == "str":
                value = args[3].strip('"')
                try:
                    value = int(value)
                except ValueError:
                    pass
            elif type(args[3]) == "int":
                value = int(args[3])
            else:
                value = str(args[3]).strip('"')

            setattr(obj_value, args[2], value)
            obj_value.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
