import task_11


class JellyBean(task_11.Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        self.flavor = flavor
        super().__init__(name, calories)

    def get_flavor(self):
        return self.flavor

    def set_flavor(self, new_flavor):
        self.flavor = new_flavor

    def is_delicious(self):
        return self.flavor != "black licorice"


jb = JellyBean("aboba", 199, "sas")
jb1 = JellyBean("Terry", 365, "black licorice")
jb2 = JellyBean()
jb2.calories = 199.9999

print(jb2.is_healthy(), "a")
