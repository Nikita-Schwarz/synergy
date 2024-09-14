import datetime

def is_leap_year(year):
    """Определяет, является ли год високосным."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_week(day, month, year):
    week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    target_date = datetime.datetime(year, month, day)
    day_idx = target_date.weekday()
    return week_days[day_idx]

def calculate_age(day, month, year):
    """Определяет возраст пользователя в годах."""
    today = datetime.date.today()
    birthday = datetime.date(year, month, day)
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

def print_date_in_stars(day, month, year):
    """Выводит дату в формате дд мм гггг звездочками."""
    digits = {
        '0': ["* * *",
              "*   *",
              "*   *",
              "*   *",
              "*   *",
              "*   *",
              "* * *"],
        '1': ["    *",
              "    *",
              "    *",
              "    *",
              "    *",
              "    *",
              "    *"],
        '2': ["* * *",
              "    *",
              "    *",
              "* * *",
              "*    ",
              "*    ",
              "* * *"],
        '3': ["* * *",
              "    *",
              "    *",
              "* * *",
              "    *",
              "    *",
              "* * *"],
        '4': ["*   *",
              "*   *",
              "*   *",
              "* * *",
              "    *",
              "    *",
              "    *"],
        '5': ["* * *",
              "*    ",
              "*    ",
              "* * *",
              "    *",
              "    *",
              "* * *"],
        '6': ["* * *",
              "*    ",
              "*    ",
              "* * *",
              "*   *",
              "*   *",
              "* * *"],
        '7': ["* * *",
              "    *",
              "    *",
              "    *",
              "    *",
              "    *",
              "    *"],
        '8': ["* * *",
              "*   *",
              "*   *",
              "* * *",
              "*   *",
              "*   *",
              "* * *"],
        '9': ["* * *",
              "*   *",
              "*   *",
              "* * *",
              "    *",
              "    *",
              "* * *"],
    }

    date_str = f"{day:02d} {month:02d} {year}"

    lines = [""] * 7
    for char in date_str:
        if char == " ":
            for i in range(7):
                lines[i] += "     "  # пустое пространство для пробела
        else:
            digit_lines = digits[char]
            for i in range(7):
                lines[i] += digit_lines[i] + "  "

    for line in lines:
        print(line)

# Основная часть программы
day = int(input("Введите день рождения (1-31): "))
month = int(input("Введите месяц рождения (1-12): "))
year = int(input("Введите год рождения (например, 1990): "))

# Определение дня недели
day_name = day_of_week(day, month, year)
print(f"День недели: {day_name}")

# Определение, является ли год високосным
if is_leap_year(year):
    print(f"Год {year} является високосным.")
else:
    print(f"Год {year} не является високосным.")

# Определение возраста
age = calculate_age(day, month, year)
print(f"Сейчас вам {age} лет.")

# Вывод даты рождения в звёздочках
print("Ваша дата рождения в формате звёздочек:")
print_date_in_stars(day, month, year)