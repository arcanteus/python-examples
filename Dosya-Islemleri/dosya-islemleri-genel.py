## open(dosya_adı,dosya_erişme_kipi)
## w Dosya kipi ( Write bilgileri override eder.)
## a Dosya kipi ( Üzerine bilgi ekler.)
## r Dosya kipi ( Okumaya yarar.)

"""open("bilgiler.txt","a")
file= open("bilgiler.txt","a",encoding="utf-8") ## UTF-8 Encode formatını destekler


file.write("Python,Java,C,PHP Programlama Dilleridir\n")
file.write("Hayırlı işler.\n")

file.close()"""
file = open("bilgiler.txt","r",encoding="utf-8") ## Okuma Kipiyle Dosya Açma

"""print(file.readline()) ## line(satır okuma fonk.)
print(file.readline())"""

liste = file.readlines() ##Satırları oku ve listenin içine atar.
print(liste)
"""for i in file:       ##Dosyayı Okuma İşlemleri
    print(i, end="")    ##for döngüsü ile yazdırma

icerik = file.read()    ##read fonk. ile okuma.
print("Dosya icerigi \n",icerik,sep="" "\nOkunamadı! 1 defa okumadan sonra string read başa dönmekte.") ## icerik okunduktan sonra ilk okuma sonrası string boş kalır
"""
file.close()
### Dosyaları Otomatik Kapatma
#with open(dosya.txt,r,encoding="utf-8") as file:


## Dosyaları İleri Geri Sarmak
##seek() ve tell() fonk.

with open("bilgiler.txt","r",encoding="utf-8") as file:
    """""##print(file.tell()) # 0. byte'da
    file.seek(20) #20. byte'a gider.
    ##print(file.tell()) #20 çıktısını alırsınız.
    file.seek(5) # 5. byte'a git
    icerik = file.read(10) #10 byte oku.
    print(icerik)
    file.seek(0)# en başa git.
    icerik2=file.read(6) # 6 karakter okur
    print(icerik2)"""
file.close()

with open("bilgiler.txt","r+") as file:
    print(file.read())
file.close()

with open("bilgiler.txt","r+") as file:
    file.seek(0)
    icerik = file.read()
    for i in range(1,3):
        icerik = input("İsim Girin") +"\n" +icerik
    print(icerik)

file.close()


