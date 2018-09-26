print("""

Faktöriyel Bulma

Çıkmak İçin Q'ya Basın!


""")

while True:
    sayı = input("Sayı:")
    if (sayı=="q"):
        print("program sonlandı.")
        break

    else:
        sayı=int(sayı)

        faktoriyel= 1

        for i in range(2,sayı+1):
            faktoriyel*=i
        print("{} Sayısının Faktöriyel Değeri =".format(i),faktoriyel)