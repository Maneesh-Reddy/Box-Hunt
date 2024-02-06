import random
import heapq
import os

# Box statuses
box_statuses = {
    1: 'empty',
    2: 'empty',
    3: 'bomb',
    4: 'empty',
    5: 'empty',
    6: 'bomb',
    7: 'bomb',
    8: 'empty',
    9: 'empty',
    10: 'bomb',
    11: 'empty',
    12: 'bomb'
}

# Set of questions and answers
questions_answers = {
    'What is the capital of France?': 'paris',
    'Which planet is known as the Red Planet?': 'mars',
    'What is the largest mammal in the world?': 'blue whale',
    'What is the currency of Japan?': 'yen',
}

# Heap Tree
class Heap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            raise IndexError("Heap is empty")

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Custom List
class CustomList:
    def __init__(self):
        self.custom_list = []

    def append(self, item):
        self.custom_list.append(item)

    def pop(self):
        if self.custom_list:
            return self.custom_list.pop()
        else:
            raise IndexError("List is empty")

    def get_length(self):
        return len(self.custom_list)

# Stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

# Function to play the game
def play_game(player, box_heap):
    # Custom list to keep track of selected boxes
    selected_boxes = CustomList()

    # Stack to store previous attempts
    previous_attempts = Stack()

    attempts = 0
    clear_console()
    print(f"\nWelcome, {player}! Try to find the box with gold.")
    
    while True:
        # Player selects a box
        try:
            box_number = int(input(f"\n{player}, enter the box number (1-12): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if box_number < 1 or box_number > 12:
            print("Invalid input. Please choose a number between 1 and 12.")
            continue

        # Check if the box has already been selected
        if box_number in selected_boxes.custom_list:
            print("You've already selected this box. Choose a different one.")
            continue

        # Ask a random question
        question, correct_answer = random.choice(list(questions_answers.items()))
        user_answer = input(f"\n{question} ")

        # Player answers the question and opens the box
        selected_boxes.append(box_number)

        if user_answer.lower() == correct_answer:
            print(f"\n{player}, you selected Box {box_number}. The status is {box_statuses[box_number]}!")

            if box_statuses[box_number] == 'gold':
                print(f"Congratulations, {player}! You found the box with gold. You win!")
                break
            elif box_statuses[box_number] == 'bomb':
                print(f"Oops! The box had a bomb. {player}, you lost!")
                break
            else:
                print("Continue searching for the box with gold.")
        else:
            print("Incorrect answer. Try again.")

        # Use stack to store previous attempts
        previous_attempts.push(box_number)

        attempts += 1

        if attempts == 4:
            print(f"You've reached the maximum number of attempts, {player}. Game over. You lost!")
            break

        print(f"\nBoxes selected so far: {selected_boxes.custom_list}")
        print(f"Previous attempts: {previous_attempts.stack}")

# Main game loop
players = [input("Enter Player 1's name: "), input("Enter Player 2's name: ")]

# Initialize the heap with box numbers
box_numbers = list(range(1, 13))
random.shuffle(box_numbers)
box_heap = Heap()
for number in box_numbers:
    box_heap.push(number)

# Player 1 sets the box number with gold
print(f"\n{players[0]}, set the box number (1-12) that will have the gold status.")
gold_box = int(input())
while gold_box < 1 or gold_box > 12:
    print("Invalid input. Please choose a number between 1 and 12.")
    gold_box = int(input())
box_statuses[gold_box] = 'gold'

# Player 2 plays
play_game(players[1], box_heap)

# Inform players that both have completed their turns
print("\nGame over!")
