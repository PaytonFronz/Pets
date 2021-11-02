from pets import Pet

class Owner:

    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        print("testing")
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.noise()
        return self
Test = Owner ("test", "test", "test","test","test")
Test.bathe()