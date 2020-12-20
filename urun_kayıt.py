import connection



class Urun_Kayit:

    def __init__(self):
        
        self.connection = connection.connection
        self.cursor = connection.connection.cursor()
        self.baglanti_olustur()
        

    def baglanti_olustur(self):
        sorgu = "create table if not exists urunler(kategori VARCHAR(255),ürün_ismi VARCHAR(255),fiyat FLOAT,adet INT,max_taksit INT)"
        self.cursor.execute(sorgu)
        self.connection.commit()


    def baglanti_kapat(self):
        self.connection.close()


    def Urun_kayit_tekil(self,kategori,urun_ismi,fiyat,adet,max_taksit):
        sorgu = "insert into urunler value(%s,%s,%s,%s,%s)"

        self.cursor.execute(sorgu,(kategori,urun_ismi,fiyat,adet,max_taksit))
        self.connection.commit()
        print("kayıt olusturuldu...")


    def Urun_kayit_liste(self,args):
        sorgu = "insert into urunler (kategori,ürün_ismi,fiyat,adet,max_taksit) values(%s,%s,%s,%s,%s)"

        self.cursor.executemany(sorgu,args)
        self.connection.commit()
        print("kayıt olusturuldu...")


    def Urun_sil(self,urun_ismi):
        self.cursor.execute("delete from urunler where ürün_ismi = %s",(urun_ismi,))
        self.connection.commit()
        print("kayıt silindi...")



    def miktar_arttır(self,urun_ismi,adet):

        self.cursor.execute(f"select adet from urunler where ürün_ismi = %s",(urun_ismi,))
        miktar = self.cursor.fetchone()

        miktar = list(miktar)
        miktar[0] +=adet
        self.cursor.execute("update urunler set adet = %s where ürün_ismi = %s",(miktar[0],urun_ismi))
        self.connection.commit()


    def miktar_azalt(self,urun_ismi,adet):
        self.cursor.execute(f"select adet from urunler where ürün_ismi = %s",(urun_ismi,))
        miktar = self.cursor.fetchone()

        miktar = list(miktar)
        miktar[0] -=adet

        print(miktar)
        self.cursor.execute("update urunler set adet = %s where ürün_ismi = %s",(miktar[0],urun_ismi))
        self.connection.commit()


    def bilgileri_goster(self):
        self.cursor.execute("select * from urunler")
        uruler = self.cursor.fetchall()
        for urun in uruler:
            print(f"kategori = {urun[0]}",f"urun ismi : {urun[1]}",f"fiyat : {urun[2]}",f"adet : {urun[3]}",sep="\n",end="\n")
        

    def bilgileri_goster_kategori(self,kategori):
        self.cursor.execute(f"select * from urunler where kategori = %s",(kategori,))
        urunler = self.cursor.fetchall()
        for urun in urunler:
            print(f"kategori = {urun[0]}",f"urun ismi : {urun[1]}",f"fiyat : {urun[2]}",f"adet : {urun[3]}",sep="\n",end="\n")


    def bilgileri_goster_isim(self,isim):
        self.cursor.execute(f"select * from urunler where isim = %s",(isim,))
        urunler = self.cursor.fetchall()
        for urun in urunler:
            print(f"kategori = {urun[0]}",f"urun ismi : {urun[1]}",f"fiyat : {urun[2]}",f"adet : {urun[3]}",sep="\n",end="\n")

































