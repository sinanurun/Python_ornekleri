from sezar_sifreleme import sifreleme_fonk as sfr
metin = input("şifrelenecek metni giriniz")
sfr.sifrele(metin)
sifre = input("şifresi çözümlecek metni giriniz")
sfr.sifrecoz(sifre)