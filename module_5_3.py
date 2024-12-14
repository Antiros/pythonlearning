from  magic_methods import Magic
class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floors = number_of_floor

if __name__ == "__main__":
    h1 = Magic('ЖК Эльбрус', 10)
    h2 = Magic('ЖК Акация', 20)

    print(h1) # __str__
    print(h2)

    print(h1 == h2) # __eq__

    h1 = h1 + 10 # __add__
    print(h1)

    print(h1 == h2) # __eq__

    h1 += 10 # __iadd__
    print(h1)

    h2 = 10 + h2 # __radd__
    print(h2)

    print(h1 > h2) # __gt__

    print(h1 >= h2) # __ge__

    print(h1 < h2) # __lt__

    print(h1 <= h2) # __le__

    print(h1 != h2) # __ne__


# __len__
# print(len(h1))
# print(len(h2))