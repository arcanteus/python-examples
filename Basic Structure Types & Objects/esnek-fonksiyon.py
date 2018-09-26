#TOPLAMA ÖRNEĞİ

def toplama(*a):
    toplam=0
    for i in a:
        toplam+=i
    print(toplam)


toplama(3,4,5,6,7)
## _____________________
c = 10
def fonk():
    c=2
    print(c) ##lokal kullanır.
fonk()
print(c)

#LOKAL DEĞİŞKENLER SADECE CLASSLAR VE FONKSİYONLARDA GEÇERLİ

##lambda örneği

üçleçarp = lambda x : x * 3 #Tek satırda fonk. tanımlama

print(üçleçarp(111))