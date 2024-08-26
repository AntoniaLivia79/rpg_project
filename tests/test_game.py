import pytest
from rpg_project.game import Character, attack, defend, buffed, debuffed

@pytest.fixture
def hero():
    return Character(name="Aragorn", health=100, mana=50)

def test_character_initialization(hero):
    assert hero.name == "Aragorn"
    assert hero.health == 100
    assert hero.mana == 50
    assert hero.level == 1
    assert hero.inventory == []

def test_take_damage(hero):
    hero.take_damage(30)
    assert hero.health == 70

def test_take_fatal_damage(hero):
    hero.take_damage(120)
    assert hero.health == 0

def test_heal(hero):
    hero.take_damage(50)
    hero.heal(20)
    assert hero.health == 70

def test_attack_with_buff(hero):
    original_health = hero.health
    attack(hero, "Orc")
    assert hero.health == original_health + 10  # Buffed adds 10 health

def test_defend_with_debuff(hero):
    original_health = hero.health
    defend(hero, "Troll")
    assert hero.health == original_health - 5  # Debuffed subtracts 5 health

