def tambolenler(sayi):
    tam_bolenler = []

    for i in range(1,sayi+1):
        if (sayi % i == 0):
            tam_bolenler.append(i)
    return tam_bolenler

sayi = input("Sayı girin:")
sayi = int(sayi)
print("tam bolenler:",tambolenler(sayi))