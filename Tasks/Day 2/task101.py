print("Введите два трехзначных числа: ")
nma = int(input())
nmb = int(input())
ascd = (nma // 10) % 10
bscd = (nmb // 10) % 10
nmb = nmb - bscd * 10 + ascd * 10
nma = nma - ascd * 10 + bscd * 10
print("Новые значения: ", nma, nmb)