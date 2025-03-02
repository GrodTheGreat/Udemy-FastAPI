class Enemy:
    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    # Default/Empty Constructor. If __init__ isn't defined this is created automatically.
    # def __init__(self):
    #     pass

    # No Argument Constructor. Needs to arguments pass in, but still need something to be done on instantiation.
    # def __init__(self):
    #     print('Do something')

    # Parameter Constructor. Pass in values for the class to use to instantiate.
    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage")
