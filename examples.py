from classes import living_room
from classes.kitchen import Kitchen
from classes import Room, Kitchen, LivingRoom, BathRoom, Studio

room1 = Room(10, 12, 4)
room2 = Room(30, 40, 2)

print(room2.length, room2.width, room2.number_of_windows)

# # Class variables can be accessed by the instance or the class
print(f'Does room 2 have a ceiling {room2.HAS_CEILING}')
print(f'Do rooms have a ceiling? {Room.HAS_CEILING}')


# # Even though it's a "constant" the value can still be changed
# room1.HAS_CEILING = False
# print(room1.HAS_CEILING)

# # Instances can call instance, static, and class methods
room1.turn_on_lights()
room1.static_method('Hannah')
# room1.rip_off_all_ceilings()

# print(f'Does room 2 have a ceiling {room2.HAS_CEILING}')

# # The class can only call static and class methods
Room.rip_off_all_ceilings()
Room.static_method('Hannah')
# # This will error because there isn't a 'self' to be passed to the method
# Room.turn_on_lights()

# # Using a property looks like a variable
print(f"Room 1's area is {room1.area}")

room1.wall_color = 'blue'
print(f'Room 1 wall color is {room1.wall_color}')


# # When a class inherits from another class in includes all of the parent classes variables, properties, and methods
kitchen = Kitchen(10, 12, 2, True)
kitchen.turn_on_lights()
print(f'The kitchen has an area of {kitchen.area} and the lights are {kitchen.light}')



# # Overwriting a method changes the context the method is called from
room1.overwrite_this_one()
kitchen.overwrite_this_one()

# # A class can also have variables that are class instances
bathroom = BathRoom(5, 3, 1)
living_room = LivingRoom(15, 20, 5)

studio_apartment = Studio([living_room, kitchen, bathroom])
studio_apartment.turn_on_living_room_lights()

# # Updating the living room inside the studio class affects the living room instance
print(f'The living room lights are {living_room.light}')
