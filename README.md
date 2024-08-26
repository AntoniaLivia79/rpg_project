# RPG Project

This is a simple role-playing game (RPG) project written in Python. The project demonstrates the use of Python's data classes, generators, and decorators in the context of an RPG. The game simulates a character encountering random enemies and either attacking or defending against them, with the character's health being affected by buffs and debuffs.

## Features

- **Character Class**: Represents a character in the game with attributes like health, mana, inventory, and level.
- **Buff and Debuff Decorators**: Modify the behavior of character actions such as attacking and defending.
- **Random Encounter Generator**: Simulates random enemy encounters.

## Getting Started

### Prerequisites

- Python 3.8+
- [Poetry](https://python-poetry.org/) for dependency management

### Installation

1. Clone the repository:

```bash
git clone https://github.com/AntoniaLivia79/rpg_project.git
cd rpg_project
```

2. Install the dependencies using Poetry:

```bash
poetry install
```

### Building the Project

To ensure that all dependencies are installed and the environment is set up correctly, run:

```bash
poetry install
```

This command will install all the dependencies defined in the `pyproject.toml` file.

### Running the Game    

You can run the game by executing the game.py script. This script simulates a character encountering random enemies and either attacking or defending against them.

```bash
poetry run python rpg_project/game.py
```

### Example Output

```plaintext
Aragorn attacks the Orc!
Aragorn is buffed! Increasing health by 10.
Current health: 110

Aragorn defends against the Troll!
Aragorn is debuffed! Decreasing health by 5.
Current health: 105

Aragorn attacks the Goblin!
Aragorn is buffed! Increasing health by 10.
Current health: 115
```

### Unit Tests

Unit tests are provided to ensure the core functionality of the game behaves as expected. The tests cover various aspects of the `Character` class and the effects of buffs and debuffs during combat.

#### Running the Tests

```bash
poetry run pytest
```

#### Test Coverage

- **Character Initialization**: Tests that a Character is initialized with the correct attributes.
- **Taking Damage**: Ensures that the take_damage method correctly reduces health and handles fatal damage.
- **Healing**: Ensures that the heal method correctly increases health.
- **Buffed Attack**: Verifies that the attack method, when buffed, increases the character's health.
- **Debuffed Defense: Verifies that the defend method, when debuffed, decreases the character's health.

#### Example Test Output

```plaintext
============================= test session starts ==============================
collected 6 items

tests/test_game.py ......                                                  [100%]

============================== 6 passed in 0.05s ===============================
```

### Project Structure

```bash
rpg_project/
├── pyproject.toml          # Project metadata and dependencies
├── README.md               # Project documentation
├── rpg_project/
│   ├── __init__.py         # Makes the directory a package
│   └── game.py             # Main game logic
└── tests/
    └── test_game.py        # Unit tests for the game
```

### Summary of Additional Instructions:

- **Building the Project**: Use `poetry install` to ensure all dependencies are installed and the environment is set up.
- **Running the Game**: Use `poetry run python rpg_project/game.py` to execute the game script.
- **Running the Tests**: Use `poetry run pytest` to run the tests and verify the functionality of the code.

This README provides a comprehensive guide for building, running, and testing your RPG project using Poetry, making it easy for anyone to set up and interact with your code.

