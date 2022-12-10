class Person:
    def __init__(self, name, age, isMale, goals):
        self.name = name
        self.age = age
        self.isMale = isMale
        self.goals = goals

    def setName(self, name): 
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setGender(self, gender):
        if gender == "Male":
            self.isMale = True
        else:
            self.isMale = False

    def getGender(self):
        if self.isMale == True:
            self.gender = "Male"
            return self.gender
        else:
            self.gender = "Female"
            return self.gender

    def setGoals(self, goals):
        self.goals = goals
    def getGoals(self):
        return self.goals

name = input("Masukkan nama: ")
age = int(input("Masukkan umur: "))
isMale = input("ismale? True or False: ").upper()
if isMale == "TRUE":
    isMale = bool(True)
else:
    isMale = bool(False)
goals = input("Masukkan cita-cita: ")

human = Person(name, age, isMale, goals)
human.setName(name)
print(human.getName())
print(human.getAge())
print(human.getGender())
print(human.getGoals())
