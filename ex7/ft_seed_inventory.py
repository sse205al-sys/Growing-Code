def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    name = seed_type.capitalize()
    if unit == "packets":
        print(f"{name} seed: {quantity} packets available")
    elif unit == "grams":
        print(f"{name} seed: {quantity} grams total")
    elif unit == "area":
        print(f"{name} seed: {quantity} area meters")
    else:
        print("Unknown unit type")
