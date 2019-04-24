#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        print("The {} has {} health and {} power.".format(self.name, self.health, self.power))
    
    def attack(self, enemy):
        enemy.health -= self.power


class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)


class Goblin(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)


def main():
    hero = Hero("Hero", 10, 5)
    enemy = Goblin("Goblin", 6, 2)

    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(enemy)
            print("You do {} damage to the goblin.".format(hero.power))
            if enemy.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.health > 0:
            # Goblin attacks hero
            enemy.attack(hero)
            print("The goblin does {} damage to you.".format(enemy.power))
            if hero.health <= 0:
                print("You are dead.")

main()