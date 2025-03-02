from enemy import Enemy
from hero import Hero
from ogre import Ogre
from weapon import Weapon
from zombie import Zombie

# enemy1 = Enemy()
# print(enemy1.health_points)

# enemy2 = Enemy()
# enemy2.health_points = 12

# enemy1.type_of_enemy = "Zombie"
# print(
#     f"{enemy1.type_of_enemy} has {enemy1.health_points} and can do an attack of {enemy1.attack_damage} damage"
# )

# print(enemy1.health_points)

# enemy1.talk()
# enemy1.attack()
# zombie = Enemy("Zombie", 10, 3)
# zombie.attack()

# big_zombie = Enemy("Big Zombie", 100, 10)
# big_zombie.attack()


def battle(enemy1: Enemy, enemy2: Enemy):
    enemy1.talk()
    enemy2.talk()

    while enemy1.health_points > 0 and enemy2.health_points > 0:
        print("---------")
        enemy1.special_attack()
        enemy2.special_attack()
        print(f"{enemy1.get_type_of_enemy()}: {enemy1.health_points} HP left")
        print(f"{enemy2.get_type_of_enemy()}: {enemy2.health_points} HP left")
        enemy1.attack()
        enemy2.health_points -= enemy1.attack_damage
        enemy2.attack()
        enemy1.health_points -= enemy2.attack_damage

    print("---------")
    if enemy1.health_points > 0:
        print(f"{enemy1.get_type_of_enemy()} wins!")
    if enemy2.health_points > 0:
        print(f"{enemy2.get_type_of_enemy()} wins!")


def hero_battle(hero: Hero, enemy: Enemy):
    while hero.health_points > 0 and enemy.health_points > 0:
        print("---------")
        enemy.special_attack()
        print(f"Hero: {hero.health_points} HP left")
        print(f"{enemy.get_type_of_enemy()}: {enemy.health_points} HP left")
        hero.attack()
        enemy.health_points -= hero.attack_damage
        enemy.attack()
        hero.health_points -= enemy.attack_damage

    print("---------")
    if hero.health_points > 0:
        print("Hero wins!")
    if enemy.health_points > 0:
        print(f"{enemy.get_type_of_enemy()} wins!")
    else:
        print("They have slain each other.")


zombie = Zombie(10, 3)
zombie.talk()
zombie.spread_disease()

ogre = Ogre(20, 3)
ogre.talk()

hero = Hero(10, 1)
weapon = Weapon("Sword", 6)
hero.weapon = weapon
hero.equip_weapon()

hero_battle(hero, ogre)
