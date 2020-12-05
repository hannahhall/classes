class Studio:
    def __init__(self, lr, kitchen, br):
        self.living_room = lr
        self.kitchen = kitchen
        self.bathroom = br

    def turn_on_living_room_lights(self):
        self.living_room.turn_on_lights()
