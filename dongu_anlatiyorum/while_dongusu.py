import os
doymak = "hayır"
print(" Pizzanız Afiyet Olsun")
while doymak =="hayır":
    cevap = input("bir dilim daha pizza ister misiniz ?")
    if cevap =="evet":
        os.system('cls')  # on Windows System
        continue
    else:
        doymak ="evet"


