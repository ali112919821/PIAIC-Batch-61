def calculate_weight_on_mars():
    weight_on_earth = float(input("Enter your weight on Earth (in Kg): "))
    weight_on_mars = (weight_on_earth) * (0.378)
    round(weight_on_mars,2)
    print(f"Your Weight on Mars will be: {weight_on_mars}")

calculate_weight_on_mars()