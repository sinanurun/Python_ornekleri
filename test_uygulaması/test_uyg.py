import time
import sys
print("MATEMATİK TESTİNE HOŞGELDİNİZ....")
time.sleep(2)
print("Teste başlamak için bekleyiniz...")
time.sleep(2)
print("soru:1-)Aşağıdakilerden hangisi asaldır?")
time.sleep(2)
print("a)4 b)5 c)6 d)8 e)10")
time.sleep(2)
c=int(input("Cevabınız=......"))
print("cevabınız değerlendiriliyor")
for i in range(5,0,-1):
    time.sleep(1)
#    print(str(i),end=" ") #sıra sıra ekrana kalan zamanı yazar
    sys.stdout.write(str(i)+' ') # sadece str tipinde verileri ekrana yazar
    sys.stdout.flush() #print ve ya write içerisinde zamana bağlı veri biriktirilmesi engeller
if c==5:
    print("DOĞRU")
else:
    print("YANLIŞ")