class calculator:
    """calculator class that calculate the operation of two vectors.
we are overriding the inbuilt functions to produce our own given output"""
    def __init__(self, value):
        """store the given list to variable"""
        self.value = value

    def __add__(self, object) -> None:
        """overrides the built-in function to update
    the variable by adding each item"""
        self.value = [x + object for x in self.value]
        print(self.value)

    def __mul__(self, object) -> None:
        """overrides the built-in function to update
    the variable by multiplying each item"""
        self.value = [x * object for x in self.value]
        print(self.value)

    def __sub__(self, object) -> None:
        """overrides the built-in function to update
    the variable by subtracting each item"""
        self.value = [x - object for x in self.value]
        print(self.value)

    def __truediv__(self, object) -> None:
        """overrides the built-in function to update
    the variable by divising each item, and has an extra
    error check so that it doesnt divide by 0"""
        assert object != 0, "not divisible by 0"
        self.value = [x / object for x in self.value]
        print(self.value)
