def version1():
    alien_color = "green"
    if alien_color == "green":
        print("You earned 5 points.")
    elif alien_color == "yellow":
        print("You earned 10 points.")
    elif alien_color == "red":
        print("You earned 15 points.")
    else:
        print("Unknown color.")

def version2():
    alien_color = "yellow"
    if alien_color == "green":
        print("You earned 5 points.")
    if alien_color == "yellow":
        print("You earned 10 points.")
    if alien_color == "red":
        print("You earned 15 points.")

def version3():
    alien_color = "red"
    points = {"green":5, "yellow":10, "red":15}.get(alien_color)
    if points is not None:
        print(f"You earned {points} points.")
    else:
        print("Unknown color.")

if __name__ == "__main__":
    version1()
    version2()
    version3()