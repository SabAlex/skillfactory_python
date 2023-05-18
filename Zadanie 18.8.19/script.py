cost = 0
num_tickets = (int(input("Введите количество билетов:")))
for i in range(num_tickets):
    age = (int(input("Введите возраст посетителя:")))
    if age < 18:
        cost += 0
    elif age >= 18 and age <= 25:
        cost += 990
    elif age > 25:
        cost += 1390
if num_tickets > 3:
    cost -= cost / 100 * 10
print("Стоимость Ваших билетов", cost)