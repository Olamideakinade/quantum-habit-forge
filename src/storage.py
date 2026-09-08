import json
import os
from src.models import Character, Habit

SAVE_FILE = "save_data.json"

def save_game(character, habits):
    data = {
        "character": character.to_dict(),
        "habits": [h.to_dict() for h in habits]
    }
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving game data: {e}")

def load_game():
    if not os.path.exists(SAVE_FILE):
        # Return default new game state
        return Character(), [
            Habit("Morning Meditation", "Easy", "Mind"),
            Habit("Code for 1 Hour", "Hard", "Skill"),
            Habit("Hydrate 2L", "Easy", "Health")
        ]
    
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            character = Character.from_dict(data.get("character", {}))
            habits = [Habit.from_dict(h) for h in data.get("habits", [])]
            return character, habits
    except Exception as e:
        print(f"Error loading game data: {e}. Starting fresh.")
        return Character(), []
