from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, first_name, is_alive=True):
        """abstract base class for character"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """abstract class : has a declaration but not an implementation"""
        pass


class Stark(Character):
    """class stark that inherits from character"""
    def die(self):
        """function die overrids the method and marks the character dead"""
        self.is_alive = False
