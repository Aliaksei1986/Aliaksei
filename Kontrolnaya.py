get_deposit = float(input("Введите сумму:"))
per_cient = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [rate * (get_deposit / 100) for rate in per_cient.values()]
print(deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))