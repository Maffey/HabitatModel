class Food:
    """
    The class contains data about food which Creatures can eat, like it\'s position,
    nutritional value and time after the food decays.
    """

    def __init__(self, pos_x, pos_y, nutrition=1, decay=10):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.nutrition = nutrition
        self.decay = decay

    def get_position(self):
        return self.pos_x, self.pos_y

    def get_nutrition(self):
        return self.nutrition

    def get_decay(self):
        return self.decay
