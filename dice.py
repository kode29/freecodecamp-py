import random

def roll_dice():
    roll = input("Roll the dice? (y/n): ")
    
    dice_drawing = {
        1: (
            "┌─────────┐",
            "│    1    │",
            "│    ●    │",
            "│         │",
            "└─────────┙"
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│    2    │",
            "│      ●  │",
            "└─────────┙"
        ),
        3: (
            "┌─────────┐",
            "│  ●  3   │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┙"
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    4    │",
            "│  ●   ●  │",
            "└─────────┙"
        ),
        5: (
            "┌─────────┐",
            "│  ● 5 ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┙"
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ● 6 ●  │",
            "│  ●   ●  │",
            "└─────────┙"
        )
    }
    
    while roll.lower()=="y".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        print("Dice Rolled: {} and {}".format(dice1, dice2))
        # similiar to JS console.log(`Variable: ${variable}`);
        
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        
        
        roll = input("Roll again? (y/n): ")
        
    if roll.lower()=="n".lower():
        print("Oh well")
        quit()
    else:
        print("Invalid input")
        quit()
        
roll_dice()