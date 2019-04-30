from random import randint
from creature import Creature
from food import Food

# Map of our habitat model. Dimensions: 10 x 10.
# TODO: Find a better way to initialize and display the map.
habitat_map = [['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', '']]

creatures_list = []


def plot_creatures(creatures):
    for i in range(len(creatures)):
        current_creature = creatures[i]
        position = current_creature.get_position()
        x = position[0]
        y = position[1]
        print("Coordinates: ", x, y)
        habitat_map[y][x] = "X"
    print(habitat_map)


def generate_creatures(amount):
    for i in range(amount):
        creature = Creature(randint(0, 9), randint(0, 9))
        creatures_list.append(creature)


def print_creatures(creatures):
    for i in range(len(creatures)):
        print("Creature\'s ID: ", creatures[i].get_id())
        print("Position: ", creatures[i].get_position())
        print("Speed: ", creatures[i].get_speed())


generate_creatures(7)
print("First batch generated.")
print_creatures(creatures_list)

generate_creatures(3)
print("Second batch generated.")
print_creatures(creatures_list)

print("Population: ", Creature.population)
plot_creatures(creatures_list)
