def yes(x):
    if x == "y" or x == "Y":
        return True
    elif x == "n" or x == "N":
        return False

print("Hello, World!")
isHe = input("Is he Pogi?[y/n]: ")
pogi = yes(isHe)

if pogi:
    print("Damn")
else:
    print("Lol")
