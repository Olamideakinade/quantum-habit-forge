import datetime

class Habit:
    def __init__(self, name, difficulty="Medium", category="General"):
        self.name = name
        self.difficulty = difficulty  # Easy, Medium, Hard
        self.category = category
        self.streak = 0
        self.superposition = True  # True means unsettled for today
        self.last_completed = None

    def to_dict(self):
        return {
            "name": self.name,
            "difficulty": self.difficulty,
            "category": self.category,
            "streak": self.streak,
            "superposition": self.superposition,
            "last_completed": self.last_completed
        }

    @classmethod
    def from_dict(cls, data):
        habit = cls(data["name"], data["difficulty"], data["category"])
        habit.streak = data.get("streak", 0)
        habit.superposition = data.get("superposition", True)
        habit.last_completed = data.get("last_completed", None)
        return habit

class Character:
    def __init__(self, name="Quantum Adept"):
        self.name = name
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100
        self.gold = 50
        self.stability = 100.0  # Percentage

    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= self.xp_to_next_level:
            self.xp -= self.xp_to_next_level
            self.level += 1
            self.xp_to_next_level = int(self.xp_to_next_level * 1.5)
            return True
        return False

    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "xp": self.xp,
            "xp_to_next_level": self.xp_to_next_level,
            "gold": self.gold,
            "stability": self.stability
        }

    @classmethod
    def from_dict(cls, data):
        char = cls(data.get("name", "Quantum Adept"))
        char.level = data.get("level", 1)
        char.xp = data.get("xp", 0)
        char.xp_to_next_level = data.get("xp_to_next_level", 100)
        char.gold = data.get("gold", 50)
        char.stability = data.get("stability", 100.0)
        return char
