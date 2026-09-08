#!/usr/bin/env python3
"""
Quantum Habit Forge Entrypoint.
"""

from src.engine import GameEngine

if __name__ == "__main__":
    try:
        engine = GameEngine()
        engine.run()
    except KeyboardInterrupt:
        print("\nExiting Quantum Habit Forge. Stay disciplined!")
        exit(0)
