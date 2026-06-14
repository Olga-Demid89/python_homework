def month_to_season(month):
    if month == 12 or month <= 2:
        return "Зима"
    if 3 <= month <= 5:
        return "Весна"
    if 6 <= month <= 8:
        return "Лето"
    if 9 <= month <= 11:
        return "Осень"
    return "Неверно указан месяц"


month = int(input("Введите месяц (1-12): "))
print(month_to_season(month))
