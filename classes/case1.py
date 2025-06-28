# Case Study 1: Basic Animal Representation
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
         print(f'{self.name.title()} makes a sound')

# Example 1
catAnimal = Animal('cat','domestic_cat')
catAnimal.make_sound()

# Example 2
dogAnimal = Animal('dog', 'bull_dog')
dogAnimal.make_sound()