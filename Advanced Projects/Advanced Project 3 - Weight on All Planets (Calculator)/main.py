weight_on_earth = float(input("Enter your Weight (in Kg): "))

def weight_on_mercury_calculator(weight_on_earth):
    weight_on_mercury = weight_on_earth * 0.376
    weight_on_mercury = round(weight_on_mercury,2)
    print(f"Your Weight on mercury will be: {weight_on_mercury}")

def weight_on_venus_calculator(weight_on_earth):
    weight_on_venus = weight_on_earth * 0.889
    weight_on_venus = round(weight_on_venus,2)
    print(f"Your Weight on venus will be: {weight_on_venus}")

def weight_on_mars_calculator(weight_on_earth):
    weight_on_mars = weight_on_earth * 0.378
    weight_on_mars = round(weight_on_mars,2)
    print(f"Your Weight on mars will be: {weight_on_mars}")

def weight_on_jupiter_calculator(weight_on_earth):
    weight_on_jupiter = weight_on_earth * 2.36
    weight_on_jupiter = round(weight_on_jupiter,2)
    print(f"Your Weight on jupiter will be: {weight_on_jupiter}")

def weight_on_saturn_calculator(weight_on_earth):
    weight_on_saturn = weight_on_earth * 1.08
    weight_on_saturn = round(weight_on_saturn,2)
    print(f"Your Weight on saturn will be: {weight_on_saturn}")

def weight_on_uranus_calculator(weight_on_earth):
    weight_on_uranus = weight_on_earth * 0.815
    weight_on_uranus = round(weight_on_uranus,2)
    print(f"Your Weight on uranus will be: {weight_on_uranus}")

def weight_on_neptune_calculator(weight_on_earth):
    weight_on_neptune = weight_on_earth * 1.14
    weight_on_neptune = round(weight_on_neptune,2)
    print(f"Your Weight on neptune will be: {weight_on_neptune}")

choice = input("Enter the name of a Planet in our Solar System: ")

match(choice):
    case "mercury":
        weight_on_mercury_calculator(weight_on_earth)
    case "venus":
        weight_on_venus_calculator(weight_on_earth)
    case "mars":
        weight_on_mars_calculator(weight_on_earth)
    case "jupiter":
        weight_on_jupiter_calculator(weight_on_earth)
    case "saturn":
        weight_on_saturn_calculator(weight_on_earth)
    case "uranus":
        weight_on_uranus_calculator(weight_on_earth)
    case "neptune":
        weight_on_neptune_calculator(weight_on_earth)