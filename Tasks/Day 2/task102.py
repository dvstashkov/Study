print("Введите четырехзначное число: ")
nma = int(input())
fts = (nma // 1000) + (nma % 100 - nma % 10) // 10
sfm = (nma % 1000 - nma % 100) // 100 - nma % 10
print("Сумма первой и третьей цифры: " + str(fts), "Разность второй и четвертой цифр: " + str(sfm), sep = "\n")