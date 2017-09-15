###########################################################################################
#                           KÜTÜPHANE VERİTABANI 2017.9.10                                #
#                                                                                         #
#      Python v3.5.2 ile yazılmıştır! Beceri geliştirme için yazılmış bu kodlar           #
#   yaklaşık 3 saatte hayata geçirildi. Modüler bir yapıda çalışması için neredeyse her   #
#   işlem için ayrı methodlar yazıldı.                                                    #
#                                                                                         #
#   Öğrenim amaçlı geliştirdiğim ilk projemdir.                                           #
#   GNU General Public License v3.0 lisanslıdır. Kullanım hakları özgürdür!               #
#                                                                                         #
#   Kemal Kolcuoğlu -> Selçuk Üniversitesi Bilgisayar Mühendisliği Öğrencisi              #
###########################################################################################

# -*- coding: utf-8 -*-

# Değişkenlerin adlandırılması :
# Değişkeneler -> (d_ -> Demet(Tuple), l_ -> Liste(list))

import sqlite3


class Kutuphane:
    def __init__(self):
        # Veritabanı bağlanıtısı nesne oluştuğu anda kuruluyor
        self.con = sqlite3.connect(".\kutuphane.db")
        self.cursor = self.con.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Kütüphane (Kitap_Adı TEXT, Yazar TEXT, Tür TEXT, Yayınevi TEXT, Baskı_Sayısı INT)")
        self.con.commit()

        # Diğer methodları daha dinamik hale getirmek için tanımlanan değişkenler
        self.kitap = object
        self.d_kitap_bilgisi = tuple()
        self.l_nesne_listesi = list()

    # Bu methodu işlem tamamlandıktan sonra mutlaka çalıştır.
    def baglantiyi_kes(self):
        self.con.close()

    # En çok kullanılan method. Bütün verileri almak için bunu kullanıyoruz.
    def butun_verileri_al(self):
        # 'SELECT * FROM' kullanmak SQL Enjection'a neden olabileceği için bu yolu tercih ettim.
        self.cursor.execute("SELECT Kitap_Adı, Yazar, Tür, Yayınevi, Baskı_Sayısı FROM Kütüphane")
        veri = self.cursor.fetchall()
        return veri

    # Gönderilen tip üzerinden aranan değerleri satır satır alan ve 'veri' listesine atan method
    def filtre_verisi_al(self, tip, deger):
        veri = list()
        for i in range(len(deger)):
            # 'Tip' değişkeni tablodaki 5 değerden hangisinde aranacağını belirliyor.
            _str = "SELECT Kitap_Adı, Yazar, Tür, Yayınevi, Baskı_Sayısı FROM Kütüphane WHERE " + tip + " = '" + deger[i] + "'"
            self.cursor.execute(_str)
            veri.append(self.cursor.fetchone())

        return veri

    def veri_bilgisi_girisi(self, liste):
        # 'Kutuphane_GUI' üzerinde kitap eklendiğinde liste ile aldığı değerlerle bir nesne oluşturan method
        # Burada nesne oluştuktan sonra 'veri_ekle' methodunda bu nesne işlenir.
        self.kitap = Kitap(liste)
        return self.kitap

    def veri_ekle(self, nesne):
        # 'Kutuphane_GUI' üzerinde girilen değerlere göre dönen nesneyi veritabanına yazan method
        self.cursor.execute("INSERT INTO Kütüphane VALUES(?,?,?,?,?)", (nesne.Kitap_Adi, nesne.Yazar, nesne.Tur, nesne.Yayinevi, nesne.Baski_Sayisi))
        self.con.commit()

    def veri_guncelle(self, eski_liste, yeni_liste):
        # 'eski_liste' üzerindeki veriler veritabanı sorgusuna iletiliyor ve eşleneği 'yeniListe'den çekiliyor.
        _str = ("UPDATE Kütüphane SET Kitap_Adı = '" + yeni_liste[0] + "', Yazar = '" + yeni_liste[1] +
                "', Tür = '" + yeni_liste[2] + "', Yayınevi = '" + yeni_liste[3] + "', Baskı_Sayısı = " + str(yeni_liste[4]) +
                " WHERE Kitap_Adı = '" + eski_liste[0] + "'")
        """+ ", Yazar = " + eskiListe[1] +", Tür = " + eskiListe[2] + ", Yayınevi = " + eskiListe[3] + ", Baskı_Sayısı = " + str(eskiListe[4]))"""
        self.cursor.execute(_str)
        self.con.commit()

    def veri_sil(self,deger):
        # 'değer' değişkeni içine kitap adı gönderiliyor ve veritabanınde eşleştirilip işlem yapılıyor.
        self.cursor.execute("DELETE FROM Kütüphane WHERE Kitap_Adı = ?", (deger, ))
        self.con.commit()

    def kitap_nesnesi(self, veri):
        # 'Veri' olarak bir demet ya da liste dönmeli
        if len(veri) != 0:
            for i in veri:
                self.kitap = Kitap(i)
                self.l_nesne_listesi.append(self.kitap)


class Kitap:
    def __init__(self, liste):
        self.Kitap_Adi = liste[0]
        self.Yazar = liste[1]
        self.Tur = liste[2]
        self.Yayinevi = liste[3]
        self.Baski_Sayisi = liste[4]

    def __str__(self):
        # 'Kutuphane_GUI' üzerinde .txt üzerine kaydedilirken kitaplar bu formatta yazılıyor.
        return "\nKitap Adı : {}\nYazar : {}\nTür : {}\nYayınevi : {}\nBaskı Sayısı : {}\n".format(self.Kitap_Adi, self.Yazar, self.Tur, self.Yayinevi, self.Baski_Sayisi)