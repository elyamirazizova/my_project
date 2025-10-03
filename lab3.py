#задание 1
sqares = [x**2 for x in range(1,11)]
print("Задание 1",sqares)

#задание 2
even_numbers={x for x in range(1,20) if x%2==0}
print("Задание 2",even_numbers)

#задание 3
words = ["python", "Java", "c++", "Rust", "go"]
new_list = [word.upper() for word in words if len(word)>3]
print("Задание 3",new_list)

#задание 4
class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
    
print("Задание 4")
    
countdown = Countdown(5)
for number in countdown:
    print(number)

#задание 5
def fibonacci(n):
    a,b = 0,1
    count = 0
    while count < n:
        yield a
        a,b = b, a+b
        count+=1

print("задание 5")

for num in fibonacci(5):
    print(num)  


#задание 6
from decimal import Decimal, ROUND_HALF_UP

print("задание 6")

def calculate_deposit_decimal():
    P = Decimal(input("Введите начальную сумму: "))
    r = Decimal(input("Введите годовую ставку (%): "))
    t = Decimal(input("Введите срок (лет): "))
    
    # Расчет по формуле: S = P * (1 + r/(12*100))^(12*t)
    monthly_rate = r / (12 * 100)
    total_months = 12 * t
    S = P * (1 + monthly_rate) ** total_months
    
    final_amount = S.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    profit = (final_amount - P).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    print(f"Итоговая сумма: {final_amount} руб.")
    print(f"Прибыль: {profit} руб.")

calculate_deposit_decimal()

#задание 7
from fractions import Fraction

print("задание 7")

a=Fraction(3,4)
b=Fraction(5,6)

addition = a+b
print(f" {a} + {b} = {addition}")

subtraction = a - b
print(f"{a} - {b} = {subtraction}")

multiplication = a * b
print(f"{a} × {b} = {multiplication}")

division = a / b
print(f"{a} ÷ {b} = {division}")


#задание 8

from datetime import datetime

now = datetime.now()

print("задание 8")
print(f"Дата и время: {now}")
print(f"Только дата: {now.date()}")
print(f"Только время: {now.time()}")

#задание 9

from datetime import datetime, date

birthday = date(2006, 7, 26)  
today = date.today()

days_passed = (today - birthday).days

next_birthday_this_year = date(today.year, 7, 26)

if today > next_birthday_this_year:
    next_birthday = date(today.year + 1, 7, 26)
else:
    next_birthday = next_birthday_this_year

days_until_next_birthday = (next_birthday - today).days

print("задание 9")
print(f"Дата рождения: {birthday}")
print(f"Сегодняшняя дата: {today}")
print(f"Дней прошло с рождения: {days_passed:,} дней")
print(f"Следующий день рождения: {next_birthday}")
print(f"Дней до следующего дня рождения: {days_until_next_birthday} дней")

#задание 10

from datetime import datetime

def format_datetime(dt):
    months = {
        1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
        5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
        9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
    }
    
    formatted = f"Сегодня {dt.day} {months[dt.month]} {dt.year} года, время: {dt.hour:02d}:{dt.minute:02d}"
    
    return formatted

print("задание 10")

current_time = datetime.now()
result = format_datetime(current_time)
print(result)