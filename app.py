class Employee:
    def greet(self):
        print("Hello Employee")


class Person:
    def greet(self):
        print("Hello person")


class Manager(Person, Employee):
    pass


# manager object takes the first parent class look through for the method specified,
manager = Manager()
# If can't find in the first then it will look in the other parent class.
manager.greet()
# It is always good to have diff methods in the parent classes so that it won't create a mess.
#
