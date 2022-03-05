

class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, school=None, klass=None):
        self.school = school
        self.klass = klass
        super().__init__(name, age)

    def get(self):
        print(f"Name: {self.name}\nAge: {self.age}")
        if self.school != None and self.klass != None:
            print(f"School - {self.school}, {self.klass} klass" )


alex = Student('alex', 3, 'Innopolis', '12o')
alex.get()
