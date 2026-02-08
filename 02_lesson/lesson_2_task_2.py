year = int(input("Введите год: "))

def is_year_leap(year):
    if year % 4 != 0:
        return False
    else:
        return True

print(year, ":", is_year_leap(year))