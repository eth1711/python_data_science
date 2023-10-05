from S1E9 import Character


class Baratheon(Character):
    "Class Baratheon"
    def __init__(self, first_name, is_alive=True):
        """inherit from character class"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        self.is_alive = False

    def __str__(self):
        """"""
        return (f"Vector: {self.family_name, self.eyes, self.hairs}")

    def __repr__(self):
        return (f"Vector: {self.family_name, self.eyes, self.hairs}")


class Lannister(Character):
    def __init__(self, first_name, is_alive=True):
        """inherit from character class"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        self.is_alive = False

    def __str__(self):
        return (f"Vector: {self.family_name, self.eyes, self.hairs}")

    def __repr__(self):
        return (f"Vector: {self.family_name, self.eyes, self.hairs}")

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """create a lannister character using class method"""
        return cls(first_name, is_alive)
