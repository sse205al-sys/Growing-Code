def ft_harvest_total():
    day = 1
    total = 0
    while day <= 3:
        harvest = int(input(f"Day {day} harvest: "))
        total += harvest
        day += 1
    print("Total harvest:", total)
