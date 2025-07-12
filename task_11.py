class Dessert:
    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    def set_name(self, new_name):
        self.name = new_name

    def set_calories(self, new_calories):
        self.calories = new_calories

    def get_name(self):
        return self.name

    def get_calories(self):
        return self.calories

    def is_healthy(self):
        if not self.calories:
            return False
        else:
            return self.calories < 200

    def is_delicious(self):
        return isinstance(self, Dessert)


cake = Dessert()
biscuit = Dessert("Lubatovo", 150)
print(cake.is_delicious(), cake.is_healthy())
print(biscuit.get_calories(), biscuit.get_name(), biscuit.is_healthy(), biscuit.is_delicious())
biscuit.set_calories(300)
print(biscuit.get_calories(), biscuit.get_name(), biscuit.is_healthy(), biscuit.is_delicious())

