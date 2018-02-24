def kullanici_adi():
    kontrol = False
    while not kontrol:
        # kullanıcı adı istendi
        k_adi = input("geçerli bir kullanıcı adı giriniz :")
        harfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        boyut = len(k_adi)
        # print(boyut)
        # kullanıcı adı boyutu ölçülüyor
        if boyut <= 8:
            a = 0
            #    print("geçerli uzunlukta bir kullanıcı adı")
            for harf in k_adi:
                if harf in harfler:
                    a = a + 1  # a +=1
            if a == boyut:
                print("geçerli bir kullanıcı adı girildi")
                kontrol = True
    return k_adi

def kullanici_sifre():
    kontrol = False
    while not kontrol:
        # kullanıcı adı istendi
        k_sifre = input("geçerli bir şifre giriniz :")
        rakamlar = "0123456789"
        boyut = len(k_sifre)
        # print(boyut)
        # kullanıcı şifre boyutu ölçülüyor
        if boyut >= 6:
            a = 0
            #    print("geçerli uzunlukta bir şifre")
            for rakam in k_sifre:
                if rakam in rakamlar:
                    a = a + 1  # a +=1
            if a == boyut:
                print("geçerli bir kullanıcı şifresi girildi")
                kontrol = True
    return k_sifre
