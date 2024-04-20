import random
def get_random_temp(season):
    if season in [6, 7, 8]:
        print("It is summer!")
        return round(random.uniform(32, 40),2)
    elif season in [12, 1, 2]:
        print("It is winter!")
        return round(random.uniform(-10, 16),2)
    elif season in [9, 10, 11]:
        print("It's autumn.")
        return round(random.uniform(16, 23),2)
    elif season in [3, 4, 5]:
        print("It is spring now!")
        return round(random.uniform(24,32),2)

def main():
    season=int(input("What's month? "))
    temperature = get_random_temp(season)
    print(f"The temperature right now is {temperature} degrees Celsius.")
    if temperature < 0:
        print(f"Brrr, that’s freezing! Wear some extra layers today")
    elif temperature >= 0 and temperature < 16:
        print("Quite chilly! Don’t forget your coat")
    elif temperature >= 16 and temperature < 23:
        print(f"That's fine, but take a jaket")
    elif temperature >= 24 and temperature <32:
        print(f"Wow, it's good weather!")
    else:
        print(f"Go to the beech, girl!")


if __name__ == "__main__":
    main()