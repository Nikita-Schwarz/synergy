
import datetime
import calendar



# Функция для определения дня недели по дате

def day_of_week(day, month, year):

    week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

    target_date = datetime.datetime(year, month, day)

    day_idx = target_date.weekday()

    return week_days[day_idx]



# Функция для проверки на високосный год

def is_leap_year(year):

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)



# Функция для определения возраста пользователя

def calculate_age(birth_year):

    current_year = datetime.datetime.now().year

    return current_year - birth_year



# Запрашиваем данные у пользователя

day = int(input("Введите день вашего рождения (1-31): "))

month = int(input("Введите месяц вашего рождения (1-12): "))

year = int(input("Введите год вашего рождения (число): "))



# Определяем день недели

day_of_week_result = day_of_week(day, month, year)

print(f"Это был день недели: {day_of_week_result}")



# Определяем, был ли год високосным

leap_year_result = is_leap_year(year)

if leap_year_result:

    print("Это был високосный год.")

else:

    print("Это НЕ был високосный год.")



# Определяем возраст пользователя

age = calculate_age(year)

print(f"Вам сейчас {age} лет.")

