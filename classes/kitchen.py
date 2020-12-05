from classes import Room

# Classes can Inherit from other classes
class Kitchen(Room):
    appliances = ['fridge', 'oven', 'dishwasher']

    def __init__(self, l, w, win, has_electric_oven):
        # Calling the parent's init will set the length, width, and number of windows on the kitchen instance
        super().__init__(l, w, win)
        self.has_electric_oven = has_electric_oven

    def add_appliance(self, appliance):
        self.appliances.append(appliance)

    # Child classes can overwrite methods on the parent
    # TODO: overwrite a method on Room
    def overwrite_this_one(self):
        super().overwrite_this_one()
        print("this method is from the kitchen class")

