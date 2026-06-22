# Проект FitLife - MVP версия 1.0
# import sys
# import io


# Принудительно устанавливаем кодировку для вывода (ошибка с кириллицей)
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

# Константы
WATER_PER_KG_ML = 30  # Рекомендация по воде: 30 мл на 1 кг веса


# 1. Знакомство
print('Приветствую в приложение FitLife!')
user_name = input('Как вас называть? ')
user_age = int(input('Введите свой возраст: '))


# 2. Сбор данных
user_weight = float(input('Введите свой вес: '))
user_height = float(input('Введите свой рост (в метрах, например 1.75): '))


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / (user_height ** 2)


# Подсчет воды: вес * 30 мл
water_ml = user_weight * WATER_PER_KG_ML
water_l = water_ml / 1000  # Перевести в литры

# 4. Вывод красивого результата
print(f'Отчет для пользователя: {user_name.title()} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi:.1f}')
print(f'Рекомендуемая норма воды: {water_l:.1f} л. в день')
print('\nРасчет окончен. Будьте здоровы!')