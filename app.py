

class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")


class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 10
        # super().__init__()

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


mammal = Mammal()
print(mammal.age)
print(mammal.weight)
# print(issubclass(Mammal, object))
# fish = Fish()
# fish.sleep()
