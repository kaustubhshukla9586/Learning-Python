import random

dice = {
    1: (
        "┌───────┐\n"
        "│       │\n"
        "│   ●   │\n"
        "│       │\n"
        "└───────┘"
    ),
    2: (
        "┌───────┐\n"
        "│ ●     │\n"
        "│       │\n"
        "│     ● │\n"
        "└───────┘"
    ),
    3: (
        "┌───────┐\n"
        "│ ●     │\n"
        "│   ●   │\n"
        "│     ● │\n"
        "└───────┘"
    ),
    4: (
        "┌───────┐\n"
        "│ ●   ● │\n"
        "│       │\n"
        "│ ●   ● │\n"
        "└───────┘"
    ),
    5: (
        "┌───────┐\n"
        "│ ●   ● │\n"
        "│   ●   │\n"
        "│ ●   ● │\n"
        "└───────┘"
    ),
    6: (
        "┌───────┐\n"
        "│ ●   ● │\n"
        "│ ●   ● │\n"
        "│ ●   ● │\n"
        "└───────┘"
    ),
]
dice = []
die = 0
total = 0
dice_num = int(input("How many dice do you want to roll? "))

for die in range(dice_num):
    dice.append(random.randint(1, dice_num))
