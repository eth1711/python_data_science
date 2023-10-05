class calculator:
    """calculator class that calculate the operation of two vectors
we use static method in this version of calucalator. Static method
doesnt require constructors thus no nee for __init__ woohoo"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """calculates the dot product of the vectos and
    prints the results"""
        print("Dot product is:", [sum(v1 * v2 for v1, v2 in zip(V1, V2))])

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """adds the vectors and prints the results"""
        print("Add Vector is", ([float(v1 + v2) for v1, v2 in zip(V1, V2)]))

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """subtracts the vectors and print the results"""
        print("Sous Vector is", ([float(v1 - v2) for v1, v2 in zip(V1, V2)]))
