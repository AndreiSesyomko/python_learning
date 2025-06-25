import task_11


class JellyBean(task_11.Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        self.__flavor = flavor
        super().__init__(name, calories)

    def get_flavor(self):
        return self.__flavor

    def set_flavor(self, new_flavor):
        self.__flavor = new_flavor

    def is_delicious(self):
        return self.__flavor != "black licorice"


jb = JellyBean("aboba", 199, "sas")
jb1 = JellyBean("Terry", 365, "black licorice")

print(jb.is_delicious())
print(jb1.is_delicious())