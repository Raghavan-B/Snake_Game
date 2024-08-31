# Snake Game

This project is a classic Snake game implemented using the Turtle module in Python. It served as a learning experience for object-oriented programming (OOP) concepts.

## Overview

The Snake game is a simple yet engaging project that helps in understanding the fundamentals of OOP. The game consists of a snake that grows longer as it eats food, with the player aiming to achieve the highest possible score. The game speed increases as the snake grows, adding to the challenge.

## Features

- **Object-Oriented Design:** The game is structured using OOP principles, with separate classes for the snake, food, and score.
- **High Score Tracking:** The game saves the highest score achieved by the player in a text file.
- **Modular Code:** The game logic is divided across multiple files, making it easy to understand and maintain.
- **Simple Graphics:** Utilizes the Turtle module for easy and customizable graphics.

## Installation

To run this game, you'll need Python installed on your system. You can install the required modules using the following command:

```bash
pip install turtle
```

Note: The Turtle module is part of the standard Python library, so you usually don’t need to install it separately.

## Usage

1. Clone this repository or download the files.
2. Run the `main.py` file to start the game.
3. Use the arrow keys to control the snake.
4. Try to eat the food and grow the snake while avoiding collisions with the walls or the snake's body.
5. The game ends when the snake collides with itself or the wall.

```bash
python Main.py
```

## Files Description

- **main.py:** The main file that initializes the game, handles key bindings, and manages the game loop.
- **snake.py:** Contains the `Snake` class that defines the snake's behavior, movement, and collision detection.
- **food.py:** Contains the `Food` class that generates food at random positions on the screen.
- **score.py:** Contains the `Score` class that handles the score display and high score tracking.
- **data.txt:** A text file that stores the highest score achieved by the player.

## High Score Tracking

The game keeps track of the highest score achieved by the player during their gaming sessions. The score is saved in the `high_score.txt` file, which is updated whenever a new high score is achieved.

