class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        cls.houses_history.append(args[0])
        return obj

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for int in range(1, new_floor + 1):
            if 1 <= new_floor <= self.number_of_floors:
                print(int)
            else:
                print(f"Этаж {new_floor} не существует в {self.name}")
                break

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)