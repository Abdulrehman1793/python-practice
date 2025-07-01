# case #6:-Simple Game Character
class GameCharacter:
    def __init__(self, name, health = 100, attack_power = 10):
       self.name = name
       self.health = health
       self.attack_power = attack_power
    
    def take_damage(self , amount):
        self.health = self.health - amount 
        if self.health < 0:
            print(f'{self.name}, "have been defeated"')
        else:
            print(self.health)

    def attacking(self, npc_health = 100):
        npc_health = npc_health - self.attack_power
        if npc_health < 0:
            print("character is defeated")

    def is_alive(self):
        if self.health >= 10:
            print("your character still have courage to fight")
            return
        else:
         self.health <= 10
        print("your character need health")

    def display_status(self):
        print(f'{self.name} " have reamining health "{self.health}')

#example 1
shadow = GameCharacter("shadow")
shadow.take_damage(99)
shadow.display_status()
shadow.attacking()
shadow.is_alive()


#example 2
khalid = GameCharacter("khalid")
khalid.take_damage(70)
khalid.display_status()
khalid.attacking()
khalid.is_alive()


           




    
