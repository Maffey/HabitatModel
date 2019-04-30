from Creature import Creature
from Food import Food

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


def plot_map(creature):
    position = creature.get_position()
    x = position[0]
    y = position[1]
    print("Coordinates: ", x, y)
    habitat_map[x][y] = "X"
    print(habitat_map)


test_creature = Creature(0, 1, 2)
test_food = Food(5, 5, 2, 3)
print("Creature\'s current position: ", test_creature.get_position())
print("Food\'s nutritional value: ", test_food.get_nutrition())
plot_map(test_creature)
