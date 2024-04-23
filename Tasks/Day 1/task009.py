print("Введите расстояние в км: ")
lng = float(input())
KM_2_MI = 1.609
KM_2_SMI = 1.852
print("Расстояние в сухопутных милях:" + str(lng / KM_2_MI), "Расстояние в морских милях:" + str(lng / KM_2_SMI), sep="\n")