class Person:
    name = "Ivan"

    def hello(self):
        print(f"Hello, {self.name}")

person = Person()
Person.hello(person)

person2 = Person()
person2.name = "Oleg"
Person.hello(person2)