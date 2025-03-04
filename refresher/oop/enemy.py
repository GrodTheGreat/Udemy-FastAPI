class Enemy:
    # Default/Empty Constructor. If __init__ isn't defined this is created automatically.
    # def __init__(self):
    #     pass

    # No Argument Constructor. Needs to arguments pass in, but still need something to be done on instantiation.
    # def __init__(self):
    #     print('Do something')

    # Parameter Constructor. Pass in values for the class to use to instantiate.
    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")

    def special_attack(self):
        print("Enemy has no special attack available.")
