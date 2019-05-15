class Vampire:
    coven = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.in_coffin = True
        self.drank_blood_today = True

    @classmethod
    def create(cls, name, age):
        new_vampire = Vampire(name, age)
        cls.coven.append(new_vampire)
        return new_vampire

    def drink_blood(self):
        self.drank_blood_today = True
      
    @classmethod
    def sunrise(cls):
        for self in Vampire.coven:
            if self.in_coffin is False or self.drank_blood_today is False:
                Vampire.coven.remove(self)

    @classmethod
    def sunset(cls):
        for self in Vampire.coven:
            self.drank_blood_today = False
            self.in_coffin = False

    def go_home(self):
        self.in_coffin = True

    def __repr__(self):
        return ' {} , {}-{} '.format(self.name, self.drank_blood_today, self.in_coffin)


the_vampire = Vampire.create('John', '45')
vampire2 = Vampire.create('Max', '66')
Vampire.sunset()
print(the_vampire)
the_vampire.drink_blood()
the_vampire.go_home()
print(the_vampire)

vampire2.drink_blood()


print(vampire2)

Vampire.sunrise()
print(Vampire.coven)