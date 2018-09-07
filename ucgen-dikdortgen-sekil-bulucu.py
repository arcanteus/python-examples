print ("Geometrik Şekil Hesaplama Programı "
       "\nGirmek İstediğiniz şekli belirtiniz."
       "\n1-) Üçgen"
       "\n2-) Dörtgen ")

a = int(input("Şekli Belirtin"))

if   (a == 1):
       print("Şekil Üçgen")

       kenar1 = int(input("İlk kenar"))
       kenar2 = int(input("İkinci kenar"))
       kenar3 = int(input("Üçüncü kenar"))

       if ((kenar1 == kenar2 and kenar2!=kenar3 ) or (kenar1==kenar3 and kenar3!=kenar2) or (kenar2==kenar3 and kenar1!=kenar2)) and (kenar3-kenar2 < kenar1 < kenar2+kenar3):
              print("İkizkenar Üçgen")
       elif kenar1 == kenar2 == kenar3:
              print("Eşkenar Üçgen")
       elif kenar3-kenar2 < kenar1 < kenar2+kenar3:
              print("Sıradan Üçgen")
       else:
              print("Üçgen Belirtmiyor")


elif (a == 2):
       print("Şekil Dörtgen")
       kenar1 = int(input("İlk kenar"))
       kenar2 = int(input("İkinci kenar"))
       kenar3 = int(input("Üçüncü kenar"))
       kenar4 = int(input("Dördüncü kenar"))

       if kenar1 == kenar2 == kenar3 == kenar4:
              print("Kare")
       else:
              print("Dikdörtgen")

else:
       print("Doğru şekli giriniz. \n")