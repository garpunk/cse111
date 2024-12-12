import pytest
from rpg_game import Fighter, Boss

def setup_game_objects():
    """Fixture to initialize the fighter and boss."""
    knight = Fighter(400, 330, 'Chrono', 200, 10)
    tyranno = Boss(400, 200, 'Tyranno', 500, 50)
    return knight, tyranno

def test_fighter_attack(setup_game_objects):
    """Test if the fighter's attack correctly reduces the boss's HP."""
    knight, tyranno = setup_game_objects
    initial_hp = tyranno.hp
    knight.attack(tyranno)
    assert tyranno.hp < initial_hp, "Boss HP should decrease after being attacked."
    assert tyranno.hp >= 0, "Boss HP should not be negative."

def test_boss_attack(setup_game_objects):
    """Test if the boss's attack correctly reduces the fighter's HP."""
    knight, tyranno = setup_game_objects
    initial_hp = knight.hp
    tyranno.attack(knight)
    assert knight.hp < initial_hp, "Fighter HP should decrease after being attacked."
    assert knight.hp >= 0, "Fighter HP should not be negative."

def test_fighter_death(setup_game_objects):
    """Test if the fighter's death state is correctly updated when HP reaches 0."""
    knight, tyranno = setup_game_objects
    knight.hp = 0
    knight.update()  # Assume `update` sets alive = False when hp <= 0
    assert not knight.alive, "Fighter should be marked as dead when HP is 0."

def test_boss_death(setup_game_objects):
    """Test if the boss's death state is correctly updated when HP reaches 0."""
    knight, tyranno = setup_game_objects
    tyranno.hp = 0
    tyranno.update()  # Assume `update` sets alive = False when hp <= 0
    assert not tyranno.alive, "Boss should be marked as dead when HP is 0."