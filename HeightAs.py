import json
import math

class HeightAs:
    """Display your height as a quantity of a variety of different
    objects. Objects and their height is stored in the objects.json
    file.
    """
    def __init__(self, **kwargs):
        try:
            with open("objects.json") as f:
                objects_json = json.loads(f.read())
        except Exception as e:
            print("Unable to load foodstuffs.json. Error: {0}".format(e))
            objects_json = {}

        # For each key in the dictionary, create a method with the same
        # name. This will make the key callable.
        for key in objects_json.keys():
            HeightAs.create_method(key, objects_json)

        self.height_in_mm = self.convert_height_to_mm(**kwargs)

    def convert_height_to_mm(self, **kwargs):
        """Convert height into millimetres (mm) from a variety of
        units.

        Args:
            **kwargs (dict): Keyword arguments to represent height
                             units.

        Returns:
            height_in_mm (float): The final calculated height in mm.
                                  rounded to the 2 decimal places.

        Notes:
            As this relies on the standard round() method to round the
            number - it is prone to slight inaccuracies.
        """
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
        """Create a new method with the name of i

        Args:
            i (str): The name to give to the method on creation.

        objects_json (dict): The dictionary of objects with their
                             associated heights as millimetres (mm).
        """
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