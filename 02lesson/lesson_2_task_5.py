def month_to_season(month_number):
    seasons = {
        12: 'Зима',
        1: 'Зима',
        2: 'Зима',
        3: 'Весна',
        4: 'Весна',
        5: 'Весна',
        6: 'Лето',
        7: 'Лето',
        8: 'Лето',
        9: 'Осень',
        10: 'Осень',
        11: 'Осень'
    }
    if not (1 <= month_number <= 12):
        raise ValueError(f'Номер месяца {month_number} вне диапазона от 1 до 12')
    return seasons.get(month_number)
print(month_to_season(2))

