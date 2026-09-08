# Quantum Habit Forge

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**Quantum Habit Forge** is an interactive, terminal-based RPG habit tracker built in Python. Transform your daily routines into epic quests, manage your character's quantum energy states, earn XP, and level up as you build unbreakable habits.

## ✨ Key Features

- **Quantum State Mechanics**: Habits exist in superposition until checked in, affecting your character's overall stability and energy multiplier.
- **RPG Progression**: Earn Experience Points (XP) and Gold for completing habits. Level up and unlock achievements.
- **Interactive CLI**: Rich terminal UI with color-coded feedback, banners, and clean formatted tables.
- **Persistent Storage**: Automatically saves your character stats and habit progress locally in JSON format.
- **Daily Resets & Streaks**: Track consecutive completions and maintain your momentum.

## 📁 Project Structure

```text
quantum-habit-forge/
├── README.md
├── requirements.txt
├── main.py
├── .gitignore
└── src/
    ├── __init__.py
    ├── engine.py
    ├── models.py
    └── storage.py
```

## 🚀 Prerequisites & Installation

- Python 3.8 or higher
- `pip` package manager

Clone the repository and install dependencies:

```bash
git clone https://github.com/username/quantum-habit-forge.git
cd quantum-habit-forge
pip install -r requirements.txt
```

## 🎮 Quickstart & Usage

Run the application via the main entrypoint:

```bash
python main.py
```

### Interactive Menu Options:
1. **View Status**: Check your character's level, XP, Gold, and Quantum Stability.
2. **View Habits**: See active habits, current streaks, and superposition states.
3. **Add Habit**: Forge a new daily habit with custom difficulty.
4. **Complete Habit**: Check off a habit for today to gain rewards.
5. **Reset Daily Quests**: Trigger the daily cosmic reset.
6. **Exit**: Save and quit.

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
