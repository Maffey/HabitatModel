class Creature:
    """Class contains data about the creature, including it\'s position and attributes."""
    population = 0

    def __init__(self, pos_x, pos_y, atr_speed=1):
        self.creature_id = Creature.population
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.atr_speed = atr_speed
        Creature.population += 1

    def get_id(self):
        return self.creature_id

    def get_position(self):
        return self.pos_x, self.pos_y

    def get_speed(self):
        return self.atr_speed

    def set_speed(self, speed):
        self.atr_speed = speed
