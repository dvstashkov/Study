print("Введите значения a и b: ")
nma = float(input())
nmb = float(input())
print("A равно ", nma ,"\nB равно ", nmb)
nmc = nma
nma = nmb
nmb = nmc
print("A равно ", nma ,"\nB равно ", nmb)
nma, nmb = nmb, nma
print("A равно ", nma ,"\nB равно ", nmb)