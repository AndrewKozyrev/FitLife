user_name = input('Введите имя: ')
user_age = int(input('Введите возраст: '))
user_weight = float(input('Введите вес в кг: '))
user_height = float(input('Введите рост в метрах: '))

# расчёт индекса массы тела
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# расчёт нормы воды
water_ml = user_weight * 30
water_l = water_ml / 1000


def get_age_word(age):
    word = None
    if user_age in range(10, 21):
        word = 'лет'
    elif user_age % 10 in [2, 3, 4]:
        word = 'года'
    elif user_age % 10 in [0, 5, 6, 7, 8, 9]:
        word = 'лет'
    else:
        word = 'год'
    return word

age_word = get_age_word(user_age)

print(f'Отчет для пользователя: {user_name} ({user_age} {age_word})')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l:.1f} л в день')
print('Расчет окончен. Будьте здоровы!')
