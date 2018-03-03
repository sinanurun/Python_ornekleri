# ord() => ASCII olarak değeri verme chr() içerisinde ki değere göre karakter üretiyor
#metin = input("şifrelenecek metni giriniz")
metin = "Python"
sifre = ""
for k in metin:
    print(ord(k)) # ASCII kodlarını verir decimal olarak
    print(k, "=>", chr(ord(k) + 5))
    sifre = sifre + chr(ord(k) + 5)
    print(sifre)
print(metin, " = >", sifre)