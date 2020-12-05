# Classes are a blueprint
class Room:
    # Variables outside of the init can be accessed by the class or the instance
    # Python doesn’t have constants (const) like javascript. 
    # Naming convention is all caps for variables that shouldn’t change
    # TODO: create HAS_CEILING lights

    HAS_CEILING = True
    light = 'off'
    

    def __init__(self, l, w, win):
        # Variables that can change between instances can be set in the __init__
        # TODO: create length width number_of_windows 
        self.length = l
        self.width = w
        self.number_of_windows = win

    # There are 3 types of methods

    # Instance Methods
    # Must have self as the first argument
    # Can update instance and class state

    # TODO: create turn_on_lights
    def turn_on_lights(self):
        self.light = 'on'


    # Class Methods
    # Must take cls as the first argument and have @classmethod decorator
    # Can update class state
    # TODO: create rip_off_all_ceilings
    @classmethod
    def rip_off_all_ceilings(cls):
        cls.HAS_CEILING = False
        
   
        

    # Static Methods
    # Cannot update class or instance state
    # Must have @staticmethod decorator
    # TODO: create static_method
    @staticmethod
    def static_method(name):
        return f'Hello, {name}'
    
    # Classes can have properties with getters and or setters
    # Getters must have the @property decorator
    # TODO: create area property
    @property
    def area(self):
        return self.width * self.length
    
    # TODO: create wall_color getter and setter
    @property
    def wall_color(self):
        print('getting color')
        return self.__wall_color
    
    # Setters must have a @<property name>.setter decorator
    @wall_color.setter
    def wall_color(self, color):
        print('setting color')
        self.__wall_color = color
    
    def overwrite_this_one(self):
        print("this method is from the Room class")
    



