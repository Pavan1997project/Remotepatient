import random

def generate_random_names(count=10):
    first_names = [
        "John", "Emma", "Liam", "Olivia", "Noah",
        "Ava", "Ethan", "Sophia", "Mason", "Isabella",
        "James", "Mia", "Benjamin", "Charlotte", "Lucas"
    ]

    middle_names = [
        "Alexander", "Grace", "Marie", "Lee", "Rose",
        "Joseph", "Elizabeth", "Michael", "David", "Ann",
        "Daniel", "Ray", "Louise", "Anthony", "Jean"
    ]

    last_names = [
        "Smith", "Johnson", "Williams", "Brown", "Jones",
        "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
        "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson"
    ]

    names = []
    for _ in range(count):
        first = random.choice(first_names)
        middle = random.choice(middle_names)
        last = random.choice(last_names)
        names.append(f"{first} {middle} {last}")

    return names


# Example usage
for name in generate_random_names(8):
    print(name)
