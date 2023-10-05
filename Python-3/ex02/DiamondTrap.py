from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class"""
    def __init__(self, first_name, is_alive=True):
        """inherits from Baratheon"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """set new eye color"""
        self.eyes = color

    def set_hairs(self, color):
        """"set new hair color"""
        self.hairs = color

    def get_eyes(self):
        """get the eye color"""
        return self.eyes

    def get_hairs(self):
        """get the hair color"""
        return self.hairs
