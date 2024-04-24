nm = float(input("Введите цену товара: "))
nmp = float(input("Введите скока доллеров: "))
print("Купить можно: " + str(nmp // nm), "КНа мороженку останется: " + str(nmp % nm), sep = "\n")