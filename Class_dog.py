class Dog:
    def __init__(self, breed, nickname, color, wool_length, age):
        self.breed = breed
        self.nickname = nickname
        self.color = color
        self.wool_length = wool_length
        self.age = age

    def general_description(self):
            print(self.breed, self.nickname, self.color, self.wool_length, self.age)


    def sleep(self):
        print('Snoooring')

    def eat(self):
        print('Chafk-Chafk')

    def bark(self):
        print('Whoaaff whooaaaff whoaaf')

    def hunting(self):
        print('Helps during the hunting activity')

    def guard(self):
        print('"Home guard" function')

    def be_nice(self):
        print('"Being nice" function')


    def tore_wolves_apart(self):
        print('Keeps wolves away')


class Wolfdog(Dog):
    def __init__(self, breed, nickname, color, wool_length, age, scars):
        super().__init__(breed, nickname, color, wool_length, age)
        self.scars = scars







dog1 = Dog('BullDog', 'Fury', 'Black', 'short', '3')
dog2 = Dog('Spaniel', 'Jessie', 'Brawn', 'medium', '2')
dog3 = Dog('Beagle', ' Noah', 'Brawn', 'medium', '4')
wolfdog1 = Wolfdog('Beast', 'Hell', 'Black', 'Short', '3', 'avaliable')



print('------------BulldogZ main fuctions------------')

print(dog1.breed, dog1.color, dog1.wool_length, dog1.age, dog1.nickname)
dog1.bark()
dog1.guard()
dog1.sleep()
dog1.eat()

print('------------SpanielZ main fuctions------------')

print(dog2.breed, dog2.color, dog2.wool_length, dog2.age, dog2.nickname)
dog2.bark()
dog2.hunting()
dog2.sleep()
dog2.eat()

print('------------BeagleZ main fuctions------------')

print(dog3.breed, dog3.color, dog3.wool_length, dog3.age, dog3.nickname)
dog3.bark()
dog3.be_nice()
dog3.sleep()
dog3.eat()

print('------------WolfdogZ main fuctions------------')

print(wolfdog1.breed, wolfdog1.color, wolfdog1.wool_length, wolfdog1.age, wolfdog1.nickname, wolfdog1.scars)
wolfdog1.bark()
wolfdog1.eat()
wolfdog1.tore_wolves_apart()




