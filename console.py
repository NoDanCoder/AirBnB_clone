#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Class which control the console, and user interface """

    prompt = '(hbtn) '
    __buff_class = ['BaseModel']

    # general commands

    def do_quit(self, line):
        """ Exist of the console by cmd """
        return True

    def do_EOF(self, line):
        """ Exist of the console by signal """
        return True

    def emptyline(self):
        """ Disable any action on BlankLine """
        pass

    # handle data comands

    def do_create(self, items):
        """ create a new BaseModel instance """
        if self.check_input(items):
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, items):
        """ Show info of a BaseModel instance """
        if self.check_input(items, 1):
            items = items.split()
            print(storage.all()[".".join(items[:2])])

    def do_destroy(self, items):
        """ Delete an instance """
        if self.check_input(items, 1):
            items = items.split()
            storage.delete(*items[:2])
            storage.save()

    def do_all(self, items):
        """ show all elements stored, compatible with given class """
        items = items.split()
        if not items:
            print([str(v) for v in storage.all().values()])
        elif items[0] not in HBNBCommand.__buff_class:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in storage.all().items() if k.split(".")[0] == items[0]])

    def do_update(self, items):
        """ Update the propertie of a instance """
        if self.check_input(items, 2):
            import re

            items = items.split()
            if '"' not in items[3]:
                value = items[3]
            else:
                value = "".join(items[3:])
                value = re.findall(r'"([^"]*)"', value)[0]

            obj = storage.all()[".".join(items[:2])]
            value = storage.auto_caster(value)
            setattr(obj, items[2], value)
            obj.save()

    # Check functions

    @staticmethod
    def check_input(items, step=0):
        """ """
        items = items.split()
        outValue = False

        # check class input
        if not items:
            print("** class name missing **")
        elif items[0] not in HBNBCommand.__buff_class:
            print("** class doesn't exist **")
        else:
            outValue = True

        if not outValue or step <= 0:
            return outValue
        outValue = False

        # check id input
        if len(items) < 2:
            print("** instance id missing **")
        elif not any(items[1] == x.split(".")[1] for x in storage.all()):
            print("** no instance found **")
        else:
            outValue = True

        if not outValue or step <= 1:
            return outValue
        outValue = False

        # check atribute and value inputs
        if len(items) < 3:
            print("** attribute name missing **")
        elif len(items) < 4:
            print("** value missing **")
        elif items[2] in storage.constants():
            print("** can't modify that property **")
        else:
            return True

        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
