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

class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def attack(self, enemy):
        enemy.health -= self.power

    def alive(self):
        if self.health > 0:
            return True



class Goblin(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
    
    def attack(self, hero):
        hero.health -= self.power
    
    def alive(self):
        if self.health > 0:
            return True


def main():
    hero = Hero("Hero", 10, 5)
    enemy = Goblin("Goblin", 6, 2)

    while enemy.alive() and hero.alive():
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.".format(enemy.health, enemy.power))
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