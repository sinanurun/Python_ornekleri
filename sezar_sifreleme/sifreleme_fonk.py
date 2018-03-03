def sifrele(metin):
    # ord() => ASCII olarak değeri verme chr() içerisinde ki değere göre karakter üretiyor
#    metin = input("şifrelenecek metni giriniz")
    # metin = "Python"
    sifre = ""
    for k in metin:
        #    print(ord(k)) # ASCII kodlarını verir decimal olarak
        print(k, "=>", chr(ord(k) + 5))
        sifre = sifre + chr(ord(k) + 5)
    print(metin, " = >", sifre)
def sifrecoz(sifre): # şifresi çözülecek şifre fonksiyona parametre olarak geliyor
    # ord() => ASCII olarak değeri verme chr() içerisinde ki değere göre karakter üretiyor
#    sifre = input("şifrelenecek metni giriniz")
    # sifre = "Python"
    metin = "" # metne dönüştürülmesi için değişken tanımlandı
    for k in sifre:
        #    print(ord(k)) # ASCII kodlarını verir decimal olarak
        print(k, "=>", chr(ord(k) - 5))
        metin = metin + chr(ord(k) - 5)
    print(sifre, " = >", metin)