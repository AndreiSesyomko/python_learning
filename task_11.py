class Dessert:
    def __init__(self, name=None, calories=None):
        self.__name = name
        self.__calories = calories

    def set_name(self, new_name):
        self.__name = new_name

    def set_calories(self, new_calories):
        self.__calories = new_calories

    def get_name(self):
        return self.__name

    def get_calories(self):
        return self.__calories

    def is_healthy(self):
        if not self.__calories:
            return False
        else:
            return self.__calories < 200

    def is_delicious(self):
        return isinstance(self, Dessert)


cake = Dessert()
biscuit = Dessert("Lubatovo", 150)
print(cake.is_delicious(), cake.is_healthy())
print(biscuit.get_calories(), biscuit.get_name(), biscuit.is_healthy(), biscuit.is_delicious())
biscuit.set_calories(300)
print(biscuit.get_calories(), biscuit.get_name(), biscuit.is_healthy(), biscuit.is_delicious())

