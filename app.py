from urun_kayıt import *

Urun_Kayit = Urun_Kayit()

print("""
**************************************

Ürün Kayıt Programına Hoşgeldiniz
İşlemler:

1. Ürünleri Göster

2. Kategriye Göre Ürünleri Göster

3. İsme Göre Ürünleri Göster

4. Ürün Ekle Tekil

5. Ürün Ekle Liste

6. Ürün Sil

7. İsme Göre Miktar Arttır

8. İsme Göre Miktar Azalt

Çıkmak için 'q' ya basın

**************************************
""")

while True:
    talep = input(">>>")
    if talep == "1":
        Urun_Kayit.bilgileri_goster()


    elif talep == "2":
        kategori = input("kategori : ")
        Urun_Kayit.bilgileri_goster_kategori(kategori)


    elif talep == "3":
        isim = input("kategori : ")
        Urun_Kayit.bilgileri_goster_isim(isim)


    elif talep == "4":
        kategori = input("kategori : ")
        ürün_ismi = input("ürün ismi : ")
        fiyat = int(input("fiyat : "))
        adet = int(input("adet : "))
        max_taksit = int(input("maximum yapılabilir taksit : "))

        Urun_Kayit.Urun_kayit_tekil(kategori,ürün_ismi,fiyat,adet,max_taksit)


    elif talep == "5":
        adet = int(input("ürün adeti : "))
        urunler = list()

        for i in range(adet):
            kategori = input("kategori : ")
            urun_ismi = input("ürün ismi : ")
            fiyat = int(input("fiyat : "))
            adet = int(input("adet : "))
            max_taksit = int(input("maximum yapılabilir taksit : "))
            tup = (kategori,urun_ismi,fiyat,adet,max_taksit)
            urunler.append(tup)

        Urun_Kayit.Urun_kayit_liste(ürünler)


    elif talep == "6":
        isim = input("isim : ")
        Urun_Kayit.Urun_sil(isim)


    elif talep == "7":
        miktar = input("miktar : ")
        Urun_Kayit.miktar_arttır(miktar)


    elif talep == "8":
        miktar = input("miktar : ")
        Urun_Kayit.miktar_azalt(miktar)


    elif talep.lower() == "q":
        break














