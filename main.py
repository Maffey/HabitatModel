import plotly.offline as py
import plotly.graph_objs as go
from random import randint
from creature import Creature
from food import Food

"""
Map of our habitat model. Dimensions: 10 x 10.
X - location of the creature.
o - location of food.
"""
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
food_list = []


# Creatures functions.


def plot_creatures(creatures):
    for i in range(len(creatures)):
        current_creature = creatures[i]
        position = current_creature.get_position()
        x = position[0]
        y = position[1]
        habitat_map[y][x] = "X"


def generate_creatures(amount):
    for i in range(amount):
        creature = Creature(randint(0, 9), randint(0, 9))
        creatures_list.append(creature)


def print_creatures(creatures):
    for i in range(len(creatures)):
        print("Creature\'s ID: ", creatures[i].get_id())
        print("Position: ", creatures[i].get_position())
        print("Speed: ", creatures[i].get_speed())


# Food functions.


def plot_food(foods):
    for i in range(len(foods)):
        current_food = foods[i]
        position = current_food.get_position()
        x = position[0]
        y = position[1]
        habitat_map[y][x] = "o"


def generate_food(amount):
    for i in range(amount):
        food = Food(randint(0, 9), randint(0, 9), randint(1, 5))
        food_list.append(food)


def print_food(foods):
    for i in range(len(foods)):
        print("Position: ", foods[i].get_position())
        print("Nutrition value: ", foods[i].get_nutrition())
        print("Decay time: ", foods[i].get_decay())


generate_creatures(3)
print_creatures(creatures_list)
print("Population: ", Creature.population)

generate_food(7)
print_food(food_list)

plot_creatures(creatures_list)
plot_food(food_list)
print(habitat_map)

py.plot({
    "data": [go.Scatter(x=[1, 2, 3, 4], y=[1, 2, 3, 4], mode='markers')],
    "layout": go.Layout(title="Habitat Map")
}, auto_open=True, filename="habitat_map.html")
