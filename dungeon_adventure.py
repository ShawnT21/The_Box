from sys import exit

def get_hurt(message, severity):
    """
    A simple function that determines damage of mc based on severity level.
    Parameters:
    (String) message: message explaining how the mc got hurt.
    (int) severity: the severity level of how bad the damage inflicted is.
    """
    if severity == 1:
        print(message)
        print("You take 5 damage!")
        health -= int(5)
    elif severity == 2:
        print(message)
        print("You take 25 damage!")
        health -= int(25)
    else:
       print(message)
       print("You take 100 damage!")
       health -= int(100)


def dead(message):
    """
    Function that tells you the MC is dead.
    Parameters:
        (String) message: Message stating the character is dead.
    """
    print(message)
    exit()


def dungeon():
    print("It is dark there's no light")
    print("What do you do? ")
    print(" Go left or right?")
    print(" Or go straight?")
    mc_moved = False

    while True:
        choice = input("> ")
        if choice == "go left":
            get_hurt('Oscar was right if this message prints', 1)
            print('You slipped on some moldy surface while drake plays in' +
                 'the background. You get up with a bruised arm.')
            mc_moved = True
        elif choice =='go right':
            print("You found a small insufficient light source.")
            print("You can move forward.")
            mc_moved = True
        elif choice == "go straight":
            if not light:
                print("You found a police flashlight. Lights up the room decently.")
                #light_found()
            else:
                print("You stumble on some dark object. It falls through a " +
                "crevice in the floor.")


""" Main Program """

health = int(100)
light = False
health_kit = False
bandages = int(0)
name = "Sir Donkulus"
mc = ""
name_1 = mc
print(f"Hello my name is {name}.")
print(f"What is yours {mc} fellow adventurer?")
mc = input(name_1)
print(f"Well {mc} you have entered a dungeon")
dungeon() # Added by Oscar


def light_found():
      print("Where do I go next?")
      print("Do I enter the mysterious room?")
      print("Continue onward?")
      choice = input("> ")

      if choice == "Enter the mysterious room":
          dead("You encounter a dragon! It burned you're face off.")
      mc_moved = False
      if choice == "Continue onward":
          print("Freedom! You did it")
          mc_moved = True
