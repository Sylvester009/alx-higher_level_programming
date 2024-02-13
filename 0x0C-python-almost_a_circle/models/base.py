#!usr/bin/python3
# models/base.py

"""
Write a class Base that will
act as the base for the other
classes in the project.
"""

import json
import os
import turtle
import csv


class Base:
    """
    Base class to manage id attribute in all future classes
    """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        method that returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs into a file.
        """
        if list_objs is None:
            list_objs = []

        filename = '{}.json'.format(cls.__name__)
        with open(filename, 'w') as my_file:
            my_file.write(cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        Method that returns the list of dictionaries
        from the JSON string representation.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance with all attributes already set.
        """
        if cls.__name__ == 'Rectangle':
            dummy_shape = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == 'Square':
            dummy_shape = cls(1)  # Create a dummy Square instance
        else:
            raise ValueError("Unsupported class")
        dummy_shape.update(**dictionary)
        return dummy_shape

    @classmethod
    def load_from_file(cls):
        """
        Class method that returns a list of instances from a file.
        """
        filename = '{}.json'.format(cls.__name__)
        instances = []

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                string_list = cls.from_json_string(json_string)
                for data in string_list:
                    inst = cls.create(**data)
                    instances.append(inst)
        except FileNotFoundError:
            return []

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize list of instances to a CSV file.
        """
        filename = '{}.csv'.format(cls.__name__)
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for i in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([i.id, i.width, i.height, i.x, i.y])
                if cls.__name__ == "Square":
                    writer.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize instances from a CSV file.
        """
        filename = '{}.csv'.format(cls.__name__)
        instances = []

        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for i in reader:
                    if cls.__name__ == "Rectangle":
                        data = {"id": int(i[0]),
                                "width": int(i[1]),
                                "height": int(i[2]),
                                "x": int(i[3]),
                                "y": int(i[4])}
                    if cls.__name__ == "Square":
                        data = {"id": int(i[0]),
                                "size": int(i[1]),
                                "x": int(i[2]),
                                "y": int(i[3])}
                    inst = cls.create(**data)
                    instances.append(inst)
            return instances
