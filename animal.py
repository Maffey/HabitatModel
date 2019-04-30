class Animal:
    """Class contains data about the animal, including it\'s position and attributes."""
    population = 0

    def __init__(self, pos_x, pos_y, hunger=0, speed=1):
        self.animal_id = Animal.population
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hunger = hunger
        self.speed = speed
        Animal.population += 1

    # Getters

    def get_id(self):
        return self.animal_id

    def get_position(self):
        return self.pos_x, self.pos_y

    def get_hunger(self):
        return self.hunger

    def get_speed(self):
        return self.speed

    # Setters

    def increase_hunger(self):
        self.hunger += 1

    def decrease_hunger(self):
        self.hunger -= 1

    def set_speed(self, speed):
        self.speed = speed
