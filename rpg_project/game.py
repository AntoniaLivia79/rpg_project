from dataclasses import dataclass, field
from typing import List
import random

@dataclass
class Character:
    name: str
    health: int
    mana: int
    inventory: List[str] = field(default_factory=list)
    level: int = 1

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount: int):
        self.health += amount

def buffed(ability_increase: int):
    def decorator(func):
        def wrapper(character: Character, *args, **kwargs):
            print(f"{character.name} is buffed! Increasing health by {ability_increase}.")
            character.health += ability_increase
            return func(character, *args, **kwargs)
        return wrapper
    return decorator

def debuffed(ability_decrease: int):
    def decorator(func):
        def wrapper(character: Character, *args, **kwargs):
            print(f"{character.name} is debuffed! Decreasing health by {ability_decrease}.")
            character.health -= ability_decrease
            return func(character, *args, **kwargs)
        return wrapper
    return decorator

def random_encounter():
    enemies = ["Goblin", "Orc", "Troll", "Dragon"]
    while True:
        yield random.choice(enemies)

@buffed(10)
def attack(character: Character, enemy: str):
    print(f"{character.name} attacks the {enemy}!")

@debuffed(5)
def defend(character: Character, enemy: str):
    print(f"{character.name} defends against the {enemy}!")

# Example Game Loop
if __name__ == "__main__":
    hero = Character(name="Aragorn", health=100, mana=50)
    encounters = random_encounter()

    for _ in range(3):  # Simulate 3 encounters
        enemy = next(encounters)
        action = random.choice([attack, defend])
        action(hero, enemy)
        print(f"Current health: {hero.health}\n")

