import plotly.offline as py
import plotly.graph_objs as go
from random import randint
from animal import Animal
from food import Food

# Global variables

animals_list = []
food_list = []

x_animals, y_animals = [], []
x_food, y_food = [], []
# Temporary variable for ensuring that consumption is executed correctly.
x_feast, y_feast = [], []


# Operations on sets of animals data


def plot_animals(animals):
    for i in range(len(animals)):
        current_animal = animals[i]
        position = current_animal.get_position()
        x = position[0]
        y = position[1]
        x_animals.append(x)
        y_animals.append(y)


def generate_animals(amount):
    for i in range(amount):
        animal = Animal(randint(0, 9), randint(0, 9))
        animals_list.append(animal)


def print_creatures(animals):
    for i in range(len(animals)):
        print("==ANIMAL==")
        print("Animal\'s ID: ", animals[i].get_id())
        print("Position: ", animals[i].get_position())
        print("Hunger: ", animals[i].get_hunger())
        print("Speed: ", animals[i].get_speed())
    print("=" * 15)


# Operations on sets of food data


def plot_food(foods):
    for i in range(len(foods)):
        current_food = foods[i]
        position = current_food.get_position()
        x = position[0]
        y = position[1]
        x_food.append(x)
        y_food.append(y)


def generate_food(amount):
    for i in range(amount):
        food = Food(randint(0, 9), randint(0, 9), randint(1, 5))
        food_list.append(food)


def print_food(foods):
    for i in range(len(foods)):
        print("===FOOD===")
        print("Position: ", foods[i].get_position())
        print("Nutrition value: ", foods[i].get_nutrition())
        print("Decay time: ", foods[i].get_decay())
    print("=" * 15)


# Habitat processes


def plot_habitat():
    # Create traces for animals and food.
    animals_trace = go.Scatter(
        x=x_animals,
        y=y_animals,
        mode="markers",
        name="Animal",
        marker=dict(
            size=50,
            color="rgb(255, 0, 0)"
        )
    )
    food_trace = go.Scatter(
        x=x_food,
        y=y_food,
        mode="markers",
        name="Food",
        marker=dict(
            size=25,
            color="rgb(0, 255, 0)"
        )
    )

    feast_trace = go.Scatter(
        x=x_feast,
        y=y_feast,
        mode="markers",
        name="Eating",
        marker=dict(
            size=15,
            color="rgb(0, 0, 255)"
        )
    )
    # Plot the traces.
    data = [animals_trace, food_trace, feast_trace]
    py.plot(data, filename="habitat_map.html")


# TODO: Figure how to remove food entries after eating it.


def food_consumption():
    food_dump_list = []

    for i in range(len(animals_list)):
        current_animal = animals_list[i]
        animal_pos = current_animal.get_position()
        animal_id = current_animal.get_id()

        for j in range(len(food_list)):
            current_food = food_list[j]
            food_pos = current_food.get_position()

            if animal_pos == food_pos:
                current_animal.decrease_hunger()
                print("Animal '", animal_id,
                      "' just had a meal!\nIt\'s hunger now: ",
                      current_animal.get_hunger())
                food_dump_list.append(current_food)
    # Might be a temporary solution, since it kind of makes it possible to eat one food multiple times.
    # However, that probably will be changed in the future when the code to disallow multiple objects
    # on the same position to be present.
    for item in food_dump_list:
        # Temporary code to ensure food consumption is working.
        pos = item.get_position()
        x = pos[0]
        y = pos[1]
        x_feast.append(x)
        y_feast.append(y)
        # Possible error [rare]: Two animals spawn at the same food, causing the method
        # to try removing one food two times.
        food_list.remove(item)


# Run instance code
generate_animals(15)
print_creatures(animals_list)

generate_food(40)
print_food(food_list)

food_consumption()

plot_animals(animals_list)
plot_food(food_list)

plot_habitat()
