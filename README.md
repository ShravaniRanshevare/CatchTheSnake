# CatchTheSnake
Snake Game 🐍 is a simple arcade-style game built in Python using the Pygame library. The player controls a snake that moves around the screen, eating food to grow longer while avoiding collisions with walls or itself. The game includes scoring and sound effects making it a fun way to practice Python game development and event handling.
A classic **Snake Game** built with **Python** and **Pygame**.  
Control the snake, eat food, grow longer, and avoid collisions with walls or yourself. Simple, fun, and addictive!

---

## 🎮 Features
- **Snake movement**: Navigate using arrow keys (Up, Down, Left, Right).  
- **Food spawning**: Randomly placed red blocks appear on the screen.  
- **Scoring system**: Gain +10 points each time the snake eats food.  
- **Collision detection**: Game ends if the snake hits the wall or itself.  
- **Restart/Quit option**: Press `Q` to quit the game gracefully.  
- **Sound effect**: Plays a ping sound when food is eaten (macOS default sound).  

---

## 🛠️ Requirements
- **Python 3.x**
- **Pygame library**

Install dependencies:
```bash
pip install pygame


▶️ How to Run
1. Clone or download repository
2. Save script as snake_game.py
3. Run the game:
4. python snake_game.py 

🎯 Controls
* Arrow Keys: Move the snake in the desired direction.
* Q Key: Quit the game after a short delay.

📊 Scoring
* +10 points per food
* Highest score tracked

🖼️ Game Design
* Snake: Green blocks that grow longer when food is eaten.
* Food: Red block randomly placed on the grid.
* Background: Yellow screen for contrast.

🚀 Future Improvements
* Levels or increasing speed
* Persistent high scores
* Custom sound effects/themes

📌 Notes
* The sound effect uses afplay (macOS). On other systems, replace with a suitable audio player or Pygame’s mixer module.
* Ensure your terminal/IDE supports running Pygame windows.
