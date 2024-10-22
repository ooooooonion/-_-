money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
total = money_capital + salary

while total >= spend:
    month += 1
    total -= spend
    spend += spend * increase
    total += salary

print("Количество месяцев, которое можно протянуть без долгов:", month)
