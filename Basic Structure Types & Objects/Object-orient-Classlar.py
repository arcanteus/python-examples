# object orient örneği ve classlar
class Kitap():
    pass

kitap = Kitap() ## __init__ metodu

print(kitap) ## __str__ metodu

#len(kitap) ## __len__ metodu tanımlanmamış.

del kitap ##objeyi siler __del__ metodunu çalıştırır

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,türü):
        print("Kitap init fonksiyonu")
        self.isim = isim
        self.yazar=yazar
        self.sayfa_sayısı=sayfa_sayısı
        self.türü=türü
    def __str__(self):
       ##return ile string döndürücez.
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTürü: {}".format(self.isim,self.yazar,self.sayfa_sayısı,self.türü)
    def __len__(self): ##__len__ metodunun kullanımı
        return self.sayfa_sayısı
    def __del__(self): ##del metodu varsayılanı override etme imkanı yok ancak ekstra özellik eklenebilir
        print("Kitap objesi siliniyor...")

kitap = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
print(kitap) ##__str__ metodunu çağırıyoruz.
print("sayfa sayısı: ",len(kitap),"\n")
del kitap

print("Özel Metodlar İçin Kaynak : \n http://www.diveintopython3.net/special-method-names.html")
