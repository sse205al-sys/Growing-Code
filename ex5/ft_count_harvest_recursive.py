def recursive(day):
    if day <= 0:
        return
    recursive(day - 1)
    print("Day", day)


def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))
    recursive(day)
    print("Harvest time!")
