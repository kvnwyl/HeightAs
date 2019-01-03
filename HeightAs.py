import json
import math

class HeightAs:
    def __init__(self, **kwargs):
        try:
            with open("objects.json") as f:
                objects_json = json.loads(f.read())
        except Exception as e:
            print("Unable to load foodstuffs.json file. Error: {0}".format(e))
            objects_json = {}

        for key in objects_json.keys():
            HeightAs.create_method(key, objects_json)

        self.height_in_mm = self.convert_height_to_mm(**kwargs)

    def convert_height_to_mm(self, **kwargs):
        feet = kwargs.get("feet", 0)
        inches = kwargs.get("inches", 0)
        m = kwargs.get("m", 0)
        cm = kwargs.get("cm", 0)
        mm = kwargs.get("mm", 0)

        height_in_mm = 0
        height_in_mm += feet * 304.8
        height_in_mm += inches * 25.4
        height_in_mm += m * 1000
        height_in_mm += cm * 10
        height_in_mm += mm

        return round(height_in_mm, 2)

    @classmethod
    def create_method(cls, i, objects_json):
        def method(self, key=None):
            objects_dict = {}

            if key:
                objects_dict.update({
                    key:
                    self.height_in_mm / objects_json.get(i).get(key)
                    })
            else:
                json_dict = objects_json.get(i)
                for key, value in json_dict.items():
                    objects_dict.update({key: self.height_in_mm / value})

            print("-"*20)
            print("Your height is:")
            print("-"*20)

            for key, value in objects_dict.items():
                print("{0} {1}s".format(value, key))

        method.__name__ = "{0}".format(i)
        setattr(cls, method.__name__, method)