per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму "))
#values_percent = list(map(float, per_cent.values()))

deposit = [i*(money/100) for i in per_cent.values()]
#i = 0
#deposit =[]
#while i < len(values_percent):
#    deposit_st = money*values_percent[i]/100
 #   i+=1
 #   deposit.append(deposit_st)
print(deposit)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))
