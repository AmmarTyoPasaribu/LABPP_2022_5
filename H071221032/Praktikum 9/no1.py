class Human:
    def __init__(self, name, position):
        self.name = name
        self.__position = position

    def movement(self, move):
        if move == "R":
            self.__position += self._speed
        elif move == "L":
            self.__position -= self._speed
    
    def getPosition(self):
        return self.__position

class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)

        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    
    def getHealth(self):
        return self._health

    def getPower(self):
        return self._power
    
    def getArmor(self):
        return self._armor

    def getSpeed(self):
        return self._speed

    def attack(self, target):
        target._health -= self._power

class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)

        self._power = 26
        self._armor = 30
    
    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health -= self._power

class Assassin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)

        self._power = 35
        self._speed = 4
    
    def special(self, target):
        self._speed = 7
        self._power = 42
        target._health -= self._power

class Support(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        
        self._speed = 4
        self._health = 500
        self._armor = 8

    def special(self, target):
        self._speed = 6
        target._health += 150


    #   CONTOH PROGRAM  #
warrior = Warrior("bambang", 10)
assassin = Assassin("joko", 25)
support = Support("udin", 30)
# sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.getHealth())
print("-"*10)
# sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())
    # END OF CONTOH PROGRAM #