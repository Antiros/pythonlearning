class Magic:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floors = number_of_floor

    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"


    def __add__(self, other):
        if isinstance(other, int):
            return Magic(self.name, self.number_of_floors + other)


    def __iadd__(self, other):
            return self.__add__(other)


    def __radd__(self, other):
        return self.__add__(other)


    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors


    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors


    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors


    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors


    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
