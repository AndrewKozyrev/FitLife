user_name = input('Введите имя: ')
user_age = int(input('Введите возраст: '))
user_weight = float(input('Введите вес в кг: '))
user_height = float(input('Введите рост в метрах: '))

# расчёт индекса массы тела
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# расчёт нормы воды
water_ml = user_weight * 30
water_liters = water_ml / 1000

print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_liters:.1f} л. в день')
print('Расчет окончен. Будьте здоровы!')
