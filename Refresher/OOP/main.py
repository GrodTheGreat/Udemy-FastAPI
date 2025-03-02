from enemy import Enemy

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
zombie = Enemy("Zombie", 10, 3)
zombie.attack()

big_zombie = Enemy("Big Zombie", 100, 10)
big_zombie.attack()
