   # ord() => ASCII olarak değeri verme chr() içerisinde ki değere göre karakter üretiyor
#sifre = input("şifrelenecek metni giriniz")
sifre = "rjwmfgf%rfmrzy"
metin = "" # metne dönüştürülmesi için değişken tanımlandı
for k in sifre:
#    print(ord(k)) # ASCII kodlarını verir decimal olarak
    print(k, "=>", chr(ord(k) - 5))
    metin = metin + chr(ord(k) - 5)
print(sifre, " = >", metin)
print(sifre, " = >", metin)