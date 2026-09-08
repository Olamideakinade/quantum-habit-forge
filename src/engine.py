import os
import sys
from colorama import init, Fore, Style
from tabulate import tabulate
from src.models import Habit
from src.storage import save_game, load_game

init(autoreset=True)

class GameEngine:
    def __init__(self):
        self.character, self.habits = load_game()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_banner(self):
        print(Fore.CYAN + Style.BRIGHT + "=" * 60)
        print(Fore.MAGENTA + Style.BRIGHT + "               QUANTUM HABIT FORGE v1.0               ")
        print(Fore.CYAN + Style.BRIGHT + "=" * 60 + Style.RESET_ALL)

    def run(self):
        while True:
            self.clear_screen()
            self.print_banner()
            print(f"{Fore.YELLOW}Character: {self.character.name} | Level: {self.character.level} | XP: {self.character.xp}/{self.character.xp_to_next_level} | Gold: {self.character.gold} | Stability: {self.character.stability:.1f}%{Style.RESET_ALL}\n")
            
            print(f"{Fore.GREEN}[1] View Status & Stats")
            print(f"[2] View Quantum Habits")
            print(f"[3] Forge New Habit")
            print(f"[4] Complete Habit (Collapse Superposition)")
            print(f"[5] Reset Daily Quantum State")
            print(f"[6] Save & Exit{Style.RESET_ALL}")
            
            choice = input(f"{Fore.CYAN}\nSelect option (1-6): {Style.RESET_ALL}").strip()
            
            if choice == '1':
                self.view_status()
            elif choice == '2':
                self.view_habits()
            elif choice == '3':
                self.add_habit()
            elif choice == '4':
                self.complete_habit()
            elif choice == '5':
                self.reset_daily()
            elif choice == '6':
                save_game(self.character, self.habits)
                print(f"{Fore.GREEN}\nProgress saved successfully. Goodbye, Quantum Adept!{Style.RESET_ALL}")
                sys.exit(0)
            else:
                input(f"{Fore.RED}Invalid option. Press Enter to try again...{Style.RESET_ALL}")

    def view_status(self):
        self.clear_screen()
        self.print_banner()
        print(f"{Fore.YELLOW}--- CHARACTER STATUS ---{Style.RESET_ALL}")
        print(f"Name: {self.character.name}")
        print(f"Level: {self.character.level}")
        print(f"XP: {self.character.xp} / {self.character.xp_to_next_level}")
        print(f"Gold: {self.character.gold}")
        print(f"Quantum Stability: {self.character.stability:.1f}%")
        input(f"{Fore.CYAN}\nPress Enter to return to main menu...{Style.RESET_ALL}")

    def view_habits(self):
        self.clear_screen()
        self.print_banner()
        print(f"{Fore.YELLOW}--- ACTIVE QUANTUM HABITS ---{Style.RESET_ALL}")
        if not self.habits:
            print("No habits forged yet.")
        else:
            table_data = []
            for idx, h in enumerate(self.habits, 1):
                state = f"{Fore.MAGENTA}Superposition{Style.RESET_ALL}" if h.superposition else f"{Fore.GREEN}Collapsed (Done){Style.RESET_ALL}"
                table_data.append([idx, h.name, h.difficulty, h.category, h.streak, state])
            
            print(tabulate(table_data, headers=["#", "Habit Name", "Difficulty", "Category", "Streak", "State"], tablefmt="fancy_grid"))
        
        input(f"{Fore.CYAN}\nPress Enter to return to main menu...{Style.RESET_ALL}")

    def add_habit(self):
        self.clear_screen()
        self.print_banner()
        print(f"{Fore.YELLOW}--- FORGE NEW HABIT ---{Style.RESET_ALL}")
        name = input("Enter habit name: ").strip()
        if not name:
            input(f"{Fore.RED}Habit name cannot be empty. Press Enter...{Style.RESET_ALL}")
            return
        
        print("Select Difficulty: [1] Easy, [2] Medium, [3] Hard")
        diff_choice = input("Choice (1-3): ").strip()
        diff_map = {'1': 'Easy', '2': 'Medium', '3': 'Hard'}
        difficulty = diff_map.get(diff_choice, 'Medium')
        
        category = input("Enter Category (e.g. Health, Skill, Mind): ").strip() or "General"
        
        new_habit = Habit(name, difficulty, category)
        self.habits.append(new_habit)
        save_game(self.character, self.habits)
        print(f"{Fore.GREEN}\nHabit '{name}' successfully forged into the quantum grid!{Style.RESET_ALL}")
        input(f"{Fore.CYAN}\nPress Enter to continue...{Style.RESET_ALL}")

    def complete_habit(self):
        self.clear_screen()
        self.print_banner()
        print(f"{Fore.YELLOW}--- COMPLETE HABIT ---{Style.RESET_ALL}")
        
        active_indices = [i for i, h in enumerate(self.habits) if h.superposition]
        if not active_indices:
            print(f"{Fore.GREEN}All habits have already been collapsed for today! Amazing work.{Style.RESET_ALL}")
            input(f"{Fore.CYAN}\nPress Enter to return...{Style.RESET_ALL}")
            return
        
        table_data = []
        for i, h in enumerate(self.habits):
            if h.superposition:
                table_data.append([i + 1, h.name, h.difficulty, h.category, h.streak])
        
        print(tabulate(table_data, headers=["#", "Habit Name", "Difficulty", "Category", "Streak"], tablefmt="fancy_grid"))
        
        choice = input(f"{Fore.CYAN}\nEnter the number of the habit to complete: {Style.RESET_ALL}").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(self.habits) and self.habits[idx].superposition:
                habit = self.habits[idx]
                habit.superposition = False
                habit.streak += 1
                
                # Rewards based on difficulty
                xp_rewards = {'Easy': 15, 'Medium': 30, 'Hard': 50}
                gold_rewards = {'Easy': 5, 'Medium': 12, 'Hard': 25}
                
                xp_gained = xp_rewards.get(habit.difficulty, 20)
                gold_gained = gold_rewards.get(habit.difficulty, 10)
                
                self.character.gold += gold_gained
                leveled_up = self.character.gain_xp(xp_gained)
                
                print(f"{Fore.GREEN}\nSuccess! Habit collapsed. Gained {xp_gained} XP and {gold_gained} Gold!{Style.RESET_ALL}")
                if leveled_up:
                    print(f"{Fore.MAGENTA}*** CONGRATULATIONS! YOU REACHED LEVEL {self.character.level}! ***{Style.RESET_ALL}")
                
                save_game(self.character, self.habits)
            else:
                print(f"{Fore.RED}Invalid selection or habit already completed today.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")
        
        input(f"{Fore.CYAN}\nPress Enter to continue...{Style.RESET_ALL}")

    def reset_daily(self):
        self.clear_screen()
        self.print_banner()
        print(f"{Fore.YELLOW}--- RESET DAILY QUANTUM STATE ---{Style.RESET_ALL}")
        
        # Check uncompleted habits for penalty
        uncompleted = [h for h in self.habits if h.superposition]
        if uncompleted:
            penalty = len(uncompleted) * 5
            self.character.stability = max(0.0, self.character.stability - penalty)
            print(f"{Fore.RED}{len(uncompleted)} habits were left uncompleted. Quantum Stability dropped by {penalty}%!{Style.RESET_ALL}")
        else:
            bonus = 10
            self.character.stability = min(100.0, self.character.stability + bonus)
            print(f"{Fore.GREEN}All habits were completed! Quantum Stability increased by {bonus}%.{Style.RESET_ALL}")
        
        for h in self.habits:
            h.superposition = True
            
        save_game(self.character, self.habits)
        print(f"{Fore.CYAN}\nDaily quantum cycle has been reset. Superpositions restored!{Style.RESET_ALL}")
        input(f"{Fore.CYAN}\nPress Enter to continue...{Style.RESET_ALL}")
