class Pet:

    def __init__(self, name, type, energy, health):
        self.name = name
        self.type = type
        self.health = int(health)
        self.energy = int(energy)

    def sleep(self):
        self.energy += 25
        print("snooooore, snooooore, snooore.")
        return self 
    
    def eat(self):
        if self.health >= 100:
            print("I'm full..!")
        else:
            self.energy += 5
            self.health += 10
            print("munch munch munch! Deeeeelish!")
        return self
    
    def play(self):
        self.health += 5
        print("*playful sounds*")
        return self
    
    def noise(self):
        print("Thanks for cleaning me up!")
        return self
    
    def display_stats(self):
        print("Current Health:", self.health)
        print("Current Energy:", self.energy)
        return self
        
Morgana = Pet ('Morgana', 'Cat', 50, 50)
Morgana.eat().sleep().eat().eat().eat().eat().eat().display_stats()