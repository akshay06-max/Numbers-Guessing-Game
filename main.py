import random
import time
import sys

BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

def type_effect(text, delay=0.02):
    """Prints text with a typewriter effect for a cinematic feel."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_banner():
    """Displays a high-level stylized game banner."""
    print(BOLD + BLUE + "==================================================" + RESET)
    print(BOLD + CYAN + "          🎯 THE ULTIMATE NUMBER MATRIX 🎯         " + RESET)
    print(BOLD + BLUE + "==================================================" + RESET)
    type_effect(YELLOW + "✨ System initialized. Ready to challenge your mind... ✨\n" + RESET)

def get_difficulty():
    """Allows the player to choose a difficulty tier."""
    print(BOLD + "Select Your Difficulty Level:" + RESET)
    print(f"[{GREEN}1{RESET}] Apprentice  (Range: 1-50)")
    print(f"[{YELLOW}2{RESET}] Specialist  (Range: 1-100)")
    print(f"[{RED}3{RESET}] Grandmaster (Range: 1-500)")
    
    while True:
        choice = input(BOLD + "\nEnter choice (1/2/3): " + RESET).strip()
        if choice == '1': return 50, "Apprentice"
        if choice == '2': return 100, "Specialist"
        if choice == '3': return 500, "Grandmaster"
        print(RED + "⚠ Invalid matrix tier. Choose 1, 2, or 3." + RESET)

def play_game():
    display_banner()
    max_range, level_name = get_difficulty()
    
    secret_number = random.randint(1, max_range)
    attempts = 0
    
    print("\n" + BOLD + MAGENTA + "--------------------------------------------------" + RESET)
    type_effect(f"🔮 Level Loaded: {level_name}. Range set from 1 to {max_range}.")
    type_effect("🔮 The system has locked in the secret number. Begin guessing...")
    print(BOLD + MAGENTA + "--------------------------------------------------\n" + RESET)

    while True:
        try:
           
            guess_str = input(BOLD + CYAN + f"➔ [Attempt {attempts + 1}] Enter your guess: " + RESET).strip()
            
            if guess_str.lower() == 'quit':
                print(RED + f"\nAborting matrix simulation. The number was {secret_number}. Goodbye!" + RESET)
                return

            user_guess = int(guess_str)
            attempts += 1
            
            if user_guess < 1 or user_guess > max_range:
                print(YELLOW + f"⚠ Out of bounds! Please guess between 1 and {max_range}.\n" + RESET)
                continue

            # Feedback mechanics
            if user_guess < secret_number:
                print(BLUE + "📉 TOO LOW! Truncating lower data registers.\n" + RESET)
            elif user_guess > secret_number:
                print(RED + "📈 TOO HIGH! Over-budgeting the upper registry.\n" + RESET)
            else:
                # Victory sequence
                print("\n" + BOLD + GREEN + "==================================================" + RESET)
                print(BOLD + GREEN + "🎉 CRITICAL HIT! ACCESS GRANTED! 🎉" + RESET)
                print(BOLD + GREEN + "==================================================" + RESET)
                type_effect(f"✨ You successfully cracked the code: {BOLD}{secret_number}{RESET}{GREEN}!")
                type_effect(f"📊 Total processing attempts required: {BOLD}{attempts}{RESET}")
                
          # Performance Rating Evaluation (scaled to difficulty)
if max_range == 50:
    thresholds = (3, 6)
elif max_range == 100:
    thresholds = (5, 10)
else:  # 500
    thresholds = (10, 20)

if attempts <= thresholds[0]:
    print(BOLD + YELLOW + "🏅 RANK: Quantum Intelligence (Flawless Performance!)" + RESET)
elif attempts <= thresholds[1]:
    print(BOLD + CYAN + "🏅 RANK: Codebreaker Pro (Excellent Deduction!)" + RESET)
else:
    print(BOLD + BLUE + "🏅 RANK: Cyber Navigator (Determined Victory!)" + RESET)

if __name__ == "__main__":
    while True:
        play_game()
        replay = input(BOLD + "Do you want to run another simulation? (y/n): " + RESET).lower().strip()
        if replay != 'y':
            print(BOLD + CYAN + "\nThank you for playing. Exiting The Number Matrix." + RESET)
            break
        print("\n\n")
