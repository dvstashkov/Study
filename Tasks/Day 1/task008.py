print("Введите сумму в рублях: ")
rub = float(input())
RUB_2_USD = 0.6
RUB_2_EUR = 0.7
print("Сумма в USD:" + str(rub / RUB_2_USD), "Сумма в EUR:" + str(rub / RUB_2_EUR), sep="\n")