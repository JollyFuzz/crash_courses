class Person:
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        print("Get name")
        return self._name
    
    def set_name(self, value):
        print("Set name")
        self._name = value

    name = property(fget=get_name, fset=set_name)

class Person2:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

class Person3:
    def __init__(self, name):
        self._name = name
    
    # будет только для чтения
    @property
    def name(self):
        return self._name

class Person4:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
    
    # будет только для чтения
    @property
    def full_name(self):
        return f"{self._name} {self._surname}"




# p = Person("Ivan")
# p.name = "Oleg"
# print(p.name)

# p = Person2("Ivan")
# p.name = "Oleg"
# print(p.name)

p = Person4("Ivan", "Ivanov")

print(p.full_name)