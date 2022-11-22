from abc import ABC, abstractmethod

class House():
    
    def __init__(self, building_type='Apartment', doors=0,
                 windows=0, wall_material='Brick'):
        self.wall_material = wall_material
        self.building_type = building_type
        self.doors = doors
        self.windows = windows
        
    def construction(self):
        return f"This is a {self.wall_material} "\
            f"{self.building_type} with {self.doors} "\
            f"door(s) and {self.windows} window(s)."


class IHouserBuilder(ABC):
    
    @staticmethod
    @abstractmethod
    def set_building_type(building_type):
        'Building type'

    @staticmethod
    @abstractmethod
    def set_wall_material(wall_material):
        "Build material"

    @staticmethod
    @abstractmethod
    def set_number_doors(number):
        "Number of doors"

    @staticmethod
    @abstractmethod
    def set_number_windows(number):
        "Number of windows"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"
        

class HouseBuilder(IHouserBuilder):
    
    def __init__(self):
        self.house = House()

    def set_building_type(self, building_type):
        self.house.building_type = building_type
        return self

    def set_wall_material(self, wall_material):
        self.house.wall_material = wall_material
        return self

    def set_number_doors(self, number):
        self.house.doors = number
        return self

    def set_number_windows(self, number):
        self.house.windows = number
        return self

    def get_result(self):
        return self.house
    

class HouseBoatDirector:
    
    @staticmethod
    def construct():
        
        return HouseBuilder()\
                .set_building_type('House Boat')\
                .set_wall_material('Wood')\
                .set_number_doors(6)\
                .set_number_windows(8)\
                .get_result()
    
    
class CastleDirector:

    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_building_type("Castle")\
            .set_wall_material("Sandstone")\
            .set_number_doors(100)\
            .set_number_windows(200)\
            .get_result()
    
    
class IglooDirector:  # pylint: disable=too-few-public-methods

    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_building_type("Igloo")\
            .set_wall_material("Ice")\
            .set_number_doors(1)\
            .get_result()
    
    
IGLOO = IglooDirector.construct()
CASTLE = CastleDirector.construct()
HOUSEBOAT = HouseBoatDirector.construct()

print(IGLOO.construction())
print(CASTLE.construction())
print(HOUSEBOAT.construction())