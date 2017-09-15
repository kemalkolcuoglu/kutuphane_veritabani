###########################################################################################
#                           KÜTÜPHANE VERİTABANI 2017.9.10                                #
#                                                                                         #
#      Python v3.5.2 ve PyQt v5.6 kullanılmıştır! Beceri geliştirme için yazılmış bu      #
#   uygulama 21 saatte hayata geçirildi. Ağırlıklı olarak 'list' veri yapısı kullanıldı.  #
#   Modüler bir yapıda çalışması için neredeyse her işlem için ayrı methodlar yazıldı.    #
#                                                                                         #
#   Özellikleri -> Tabloya veri yazmak, kitap eklemek, kitap güncellemek, kitap silmek,   #
#   sorgu ile filtrelemek, metin dosyasına verileri kayıt etmek.                          #
#                                                                                         #
#   Öğrenim amaçlı geliştirdiğim ilk projemdir.                                           #
#   GNU General Public License v3.0 lisanslıdır. Kullanım hakları özgürdür!               #
#                                                                                         #
#   Kemal Kolcuoğlu -> Selçuk Üniversitesi Bilgisayar Mühendisliği Öğrencisi              #
###########################################################################################

# -*- coding: utf-8 -*-

# Değişkenlerin adlandırılması :
# Değişkeneler -> (d_ -> Demet(Tuple), l_ -> Liste(list))
# Bileşenler -> ( m_ -> Menü, act_ -> Action, bt_ -> PushButton, rb_ -> RadioButton, lb_ -> Label, le_ -> LineEdit, gb_ -> GroupBox)
# Layoutlar -> (vbl_ -> VBoxLayout, hbl_ -> HBoxLayout)
# ke -> 'Kitap Ekle', kg -> 'Kitap Güncelle

from PyQt5 import QtCore, QtGui, QtWidgets
from Kutuphane_Otomasyonu import *
import sys, os


class Kutuphane_GUI(object):
    def setupUi(self, anaPencere):
        anaPencere.setObjectName("anaPencere")
        anaPencere.resize(700, 400)
        anaPencere.setMinimumSize(QtCore.QSize(700, 400))
        anaPencere.setMaximumSize(QtCore.QSize(700, 400))

        # Bütün bileşen tanımlamaları yapılıyor
        self.govde = QtWidgets.QWidget(anaPencere)
        self.kitap_tablo = QtWidgets.QTableWidget(self.govde)
        self.gb_islemler = QtWidgets.QGroupBox(self.govde)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.gb_islemler)
        self.verticalLayout_islemler = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.bt_kitapEkle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_veriGuncelle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_kitapSil = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.lb_durumYazisi = QtWidgets.QLabel(self.govde)
        self.gb_filtre = QtWidgets.QGroupBox(self.govde)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.gb_filtre)
        self.verticalLayout_filtre = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.rb_kitapadi = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rb_yazar = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rb_yayinevi = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rb_tur = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.lineEdit_filtreGiris = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.bt_filtrele = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.line = QtWidgets.QFrame(self.govde)
        self.menubar = QtWidgets.QMenuBar(anaPencere)
        self.m_dosya = QtWidgets.QMenu(self.menubar)
        self.m_yardim = QtWidgets.QMenu(self.menubar)
        self.act_farkliKaydet = QtWidgets.QAction(anaPencere)
        self.act_cikis = QtWidgets.QAction(anaPencere)
        self.act_hakkinda = QtWidgets.QAction(anaPencere)

        self.kitap_tablo.setEnabled(True)
        self.kitap_tablo.setGeometry(QtCore.QRect(10, 10, 530, 330))
        self.kitap_tablo.setMinimumSize(QtCore.QSize(530, 330))
        self.kitap_tablo.setMaximumSize(QtCore.QSize(530, 330))
        self.kitap_tablo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.gb_islemler.setGeometry(QtCore.QRect(560, 210, 121, 131))
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 101, 101))
        self.verticalLayout_islemler.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_islemler.addWidget(self.bt_kitapEkle)
        self.verticalLayout_islemler.addWidget(self.bt_veriGuncelle)
        self.verticalLayout_islemler.addWidget(self.bt_kitapSil)

        self.lb_durumYazisi.setGeometry(QtCore.QRect(10, 350, 680, 25))
        self.lb_durumYazisi.setMinimumSize(QtCore.QSize(680, 25))
        self.lb_durumYazisi.setMaximumSize(QtCore.QSize(680, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lb_durumYazisi.setFont(font)

        self.gb_filtre.setGeometry(QtCore.QRect(560, 20, 121, 181))
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 101, 151))
        self.verticalLayout_filtre.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_filtre.addWidget(self.rb_kitapadi)
        self.verticalLayout_filtre.addWidget(self.rb_yazar)
        self.verticalLayout_filtre.addWidget(self.rb_yayinevi)
        self.verticalLayout_filtre.addWidget(self.rb_tur,stretch=0) # Alignment sorunu
        self.verticalLayout_filtre.addWidget(self.lineEdit_filtreGiris)
        self.verticalLayout_filtre.addWidget(self.bt_filtrele)

        self.line.setGeometry(QtCore.QRect(0, 340, 701, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.m_dosya.addAction(self.act_farkliKaydet)
        self.m_dosya.addSeparator()
        self.m_dosya.addAction(self.act_cikis)
        self.m_yardim.addAction(self.act_hakkinda)
        self.menubar.addAction(self.m_dosya.menuAction())
        self.menubar.addAction(self.m_yardim.menuAction())

        self.govde.setObjectName("govde")
        self.kitap_tablo.setObjectName("kitap_tablo")
        self.gb_islemler.setObjectName("gb_islemler")
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_islemler.setObjectName("verticalLayout_islemler")
        self.bt_kitapEkle.setObjectName("bt_kitapEkle")
        self.bt_veriGuncelle.setObjectName("bt_veriGuncelle")
        self.bt_kitapSil.setObjectName("bt_kitapSil")
        self.lb_durumYazisi.setObjectName("lb_durumYazisi")
        self.gb_filtre.setObjectName("gb_filtre")
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_filtre.setObjectName("verticalLayout_filtre")
        self.rb_kitapadi.setObjectName("rb_kitapadi")
        self.rb_yazar.setObjectName("rb_yazar")
        self.rb_yayinevi.setObjectName("rb_yayinevi")
        self.rb_tur.setObjectName("rb_tur")
        self.lineEdit_filtreGiris.setObjectName("lineEdit_filtreGiris")
        self.bt_filtrele.setObjectName("bt_filtrele")
        self.line.setObjectName("line")
        self.menubar.setObjectName("menubar")
        self.m_dosya.setObjectName("m_dosya")
        self.m_yardim.setObjectName("m_yardim")
        self.act_farkliKaydet.setObjectName("act_farkliKaydet")
        self.act_cikis.setObjectName("act_cikis")
        self.act_hakkinda.setObjectName("act_hakkinda")

        anaPencere.setMenuBar(self.menubar)
        anaPencere.setCentralWidget(self.govde)

        self.retranslateUi(anaPencere)
        self.otomasyon()

        self.act_farkliKaydet.triggered.connect(self.farkliKaydet)
        self.act_hakkinda.triggered.connect(self.hakkinda)
        self.act_cikis.triggered.connect(lambda x : QtWidgets.qApp.quit())

        QtCore.QMetaObject.connectSlotsByName(anaPencere)

    def otomasyon(self):
        self.kutup = Kutuphane()  # Veritabanındaki tabloyu oluşturan Kütüphane Method'u çağrılıyor.
        self.kitap_listesi = self.kutup.butun_verileri_al()  # Veritabanındaki bütün veriler bir listeye atılıyor.
        # type(kitap_listesi) = <class 'list'>
        self.kitap_listesi = sorted(self.kitap_listesi)  # Alfabetik sıralama yapılıyor.
        self.kitap_tablo_olusturma()  # kitap_tablo_olustur() methodu çağrılıyor

        self.bt_filtrele.clicked.connect(self.filtreleme)  # 'Filtrele' butonuna basılınca çalışan method
        self.bt_kitapEkle.clicked.connect(self.kitap_ekle_butonu)  # 'Kitap Ekle' butonuna basılınca çalışan method
        self.bt_veriGuncelle.clicked.connect(self.veriGuncelle)  # 'Veri Güncelle' butonuna basılınca çalışan method
        self.bt_kitapSil.clicked.connect(self.veriSil)  # 'Kitap Sil' butonuna basılınca çalışan method

        self.tabloyaVeriYazma(self.kitap_listesi)  # Uygulama başlatıldığında oluşturulan kitap tablosu

    def farkliKaydet(self):
        """
        Bu method'a metne yazdırma işlevi kullanılıyor.
        'kutup.kitap_nesnesi()' methodu gönderilen verilerden kitap nesneler oluşturuyor. Bu nesnelerde bir listede toplanıyor.
        Burada kullanacağımız asıl değişken 'kutup.l_nesne_listesi' ve liste tipindedir.
        """
        self.kutup.kitap_nesnesi(self.kitap_listesi)
        try:
            dosya_adi = QtWidgets.QFileDialog.getSaveFileName(anaPencere, "Dosya Kaydet", os.getenv("HOME"))

            with open(dosya_adi[0], "w", encoding = "utf-8") as dosya:
                for i in range(0, len(self.kutup.l_nesne_listesi)):
                    # Listedeki nesnelerin yazısını dosyaya yazdırıyoruz.
                    dosya.write(self.kutup.l_nesne_listesi[i].__str__())

            self.lb_durumYazisi.setText("Dosya Kaydedildi -> " + dosya_adi[0])
        except:
            self.lb_durumYazisi.setText("Dosya Kaydedilirken Hata Oluştu!\nLütfen Tekrar Deneyiniz!")

    def kitap_tablo_olusturma(self):
        self.kitap_tablo.setColumnCount(5)  # Kitap, Yazar, Tür, Yayınevi, Baskı_Sayısı değişkenleri oluduğu için 5 değeri veriliyor.

        # Başlık Sutunlarının Oluşturulduğu Döngü
        for i in range(0, 5):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(8)
            item.setFont(font)
            self.kitap_tablo.setHorizontalHeaderItem(i, item)

        # Başlık Sutunların Adları Elle Girildi
        item = self.kitap_tablo.horizontalHeaderItem(0)
        item.setText("Kitap Adı")
        item = self.kitap_tablo.horizontalHeaderItem(1)
        item.setText("Yazar")
        item = self.kitap_tablo.horizontalHeaderItem(2)
        item.setText("Tür")
        item = self.kitap_tablo.horizontalHeaderItem(3)
        item.setText("Yayınevi")
        item = self.kitap_tablo.horizontalHeaderItem(4)
        item.setText("Baskı Sayısı")

        __sortingEnabled = self.kitap_tablo.isSortingEnabled()
        self.kitap_tablo.setSortingEnabled(False)  # Tablonun alfabetik sıralanmasını sağlayan Method. True yaparsan sıralama yapmaz.
        self.kitap_tablo.setSortingEnabled(__sortingEnabled)  # Alfabetik sıralama methodu uygulanıyor.

        # Bellek boşaltım işleri
        del item

    def tabloyaVeriYazma(self,l_liste):
        self.kitap_tablo.setRowCount(len(l_liste))  # Tablo kaç satırdan oluşacağını veritabanından alınan liste karar veriyor.

        # Satırlardaki Numaraların Oluşturulduğu Döngü
        for i in range(0, self.kitap_tablo.rowCount()):
            item = QtWidgets.QTableWidgetItem()
            self.kitap_tablo.setVerticalHeaderItem(i, item)

        # Satırlardaki Numaraların Yazıldığı Döngü
        for i in range(0, self.kitap_tablo.rowCount()):
            item = self.kitap_tablo.verticalHeaderItem(i)
            item.setText(str(i + 1))

        for i in range(0, self.kitap_tablo.rowCount()):  # Satır sayısı kadar veri işleniyor.
            for j in range(0, 5):  # Kitap, Yazar, Tür, Yayınevi, Baskı_Sayısı değişkenleri oluduğu için 5 kez dönüyor.
                # Burada değişken string'e dönüştürülüyor çünkü veritabanınnın 5 değişkeni int tipinde tanımlı
                _str = str(l_liste[i][j])
                item = QtWidgets.QTableWidgetItem()
                self.kitap_tablo.setItem(i, j, item)
                item = self.kitap_tablo.item(i, j)
                item.setText(_str)

        # Bellek boşaltım işleri
        del l_liste

    def filtreleme(self):
        aranan = self.lineEdit_filtreGiris.text()  # LineEdit'e girilen arama sözcüğü
        filtre_listesi = list()

        # Kriter bulunamadığında yazdırılan durum. Eğer kriter bulunursa zaten aşağıdaki kontrollerde lb_durumYazisi değişiyor.
        self.lb_durumYazisi.setText("Aradığınız Kriterlere Uygun Veri Bulunamadı.")

        """
        Bu döngüde i satır sayısı kadar geziyor.
        'RadioButton'ların hangisi etkinse ve 'lineEdit'e veri girilmişse aranan değişkenine girilen veri varsa o verinin ...
         tablo karşılığı olan 'Kitap_Adı' değeri listeye ekleniyor.
        """
        for i in range(0, self.kitap_tablo.rowCount()):
            if (self.rb_kitapadi.isChecked()) and (self.lineEdit_filtreGiris.text() != ""):
                _str = str(self.kitap_listesi[i][0])
                if _str.find(aranan) > -1 or _str.lower().find(aranan) > -1 or _str.upper().find(aranan) > -1:
                    filtre_listesi.append(self.kitap_listesi[i][0])
                    self.lb_durumYazisi.setText("Filtreleme Tamamlandı! Filtrelenen Veri Tipi -> "+self.rb_kitapadi.text()+"\nBulunan Değer Sayısı -> "+str(len(filtre_listesi)))
            elif (self.rb_yazar.isChecked()) and (self.lineEdit_filtreGiris.text() != ""):
                _str = str(self.kitap_listesi[i][1])
                if _str.find(aranan) > -1 or _str.lower().find(aranan) > -1 or _str.upper().find(aranan) > -1:
                    filtre_listesi.append(self.kitap_listesi[i][0])
                    self.lb_durumYazisi.setText("Filtreleme Tamamlandı! Filtrelenen Veri Tipi -> " + self.rb_yazar.text()+"\nBulunan Değer Sayısı -> "+str(len(filtre_listesi)))
            elif (self.rb_tur.isChecked()) and (self.lineEdit_filtreGiris.text() != ""):
                _str = str(self.kitap_listesi[i][2])
                if _str.find(aranan) > -1 or _str.lower().find(aranan) > -1 or _str.upper().find(aranan) > -1:
                    filtre_listesi.append(self.kitap_listesi[i][0])
                    self.lb_durumYazisi.setText("Filtreleme Tamamlandı! Filtrelenen Veri Tipi -> " + self.rb_tur.text()+"\nBulunan Değer Sayısı -> "+str(len(filtre_listesi)))
            elif (self.rb_yayinevi.isChecked()) and (self.lineEdit_filtreGiris.text() != ""):
                _str = str(self.kitap_listesi[i][3])
                if _str.find(aranan) > -1 or _str.lower().find(aranan) > -1 or _str.upper().find(aranan) > -1:
                    filtre_listesi.append(self.kitap_listesi[i][0])
                    self.lb_durumYazisi.setText("Filtreleme Tamamlandı! Filtrelenen Veri Tipi -> " + self.rb_yayinevi.text()+"\nBulunan Değer Sayısı -> "+str(len(filtre_listesi)))
            else:
                self.lb_durumYazisi.setText("Herhangi bir değer girilmedi! Tablo yeniden oluşturuldu.")

        # Filtrelenmiş liste, verileri almak için 'kutup.filtre_verisi_al' methoduna iletiliyor.
        # Dönen liste yeni listeye atılıyor.
        yeni_liste = self.kutup.filtre_verisi_al("Kitap_Adı", filtre_listesi)
        # type(yeni_liste) -> <class 'list'>

        # Filtrede aranan kriterlere uygun veri bulunmazsa liste ilk haline döndürülüyor.
        if len(filtre_listesi) == 0:
            yeni_liste = self.kitap_listesi

        yeni_liste = sorted(yeni_liste)  # Alfabetik sıralama yaptırılıyor.

        self.kitap_tablo.setRowCount(len(yeni_liste))  # Tablo kaç satırdan oluşacağını veritabanından alınan liste karar veriyor.
        self.tabloyaVeriYazma(yeni_liste)  # Tabloya veriler method yardımıyla yazdırılıyor.

        # Bu ifade filtreleme yapıldıktan sonra küçülen tablonun asıl boyutunu geri kazanması için yazıldı.
        self.kitap_tablo.setRowCount(len(self.kitap_listesi))

        # Bellek boşaltma işlemi
        del yeni_liste
        del aranan
        del filtre_listesi

        # --------------------------------------------------------------------------------
        # Filtreleme yaptıktan sonra radioButton'nun seçili kalmasını önlemek için yazılmış komutlardır. Ancak bug içeriyor.
        # Buton seçili olmadığı halde seçiliymiş gibi gözüküyor. Fare ile üzerine gidince durumu normale dönüyor.
        self.rb_kitapadi.setCheckable(False)
        self.rb_yazar.setCheckable(False)
        self.rb_yayinevi.setCheckable(False)
        self.rb_tur.setCheckable(False)
        self.rb_kitapadi.setCheckable(True)
        self.rb_yazar.setCheckable(True)
        self.rb_yayinevi.setCheckable(True)
        self.rb_tur.setCheckable(True)
        # --------------------------------------------------------------------------------

    def kitap_ekle_butonu(self):
        # 'bt_kitapEkle' bileşeninin çalıştıracağı kodlar çağrılıyor
        self.ke = kitapMenu()
        self.lb_durumYazisi.setText("Kitap ekleme menüsü açıldı.")

    def tablodanGirdiAl(self):
        # Bu method tablodaki üzerine tıklanılan verinin bilgilerini almak için kullanılıyor.
        row = self.kitap_tablo.currentItem().row()
        col = self.kitap_tablo.currentItem().column()
        cell = self.kitap_tablo.item(row, col).text()  # get cell at row, col
        if col == 4:  # 4. Kolon 'Baskı Sayısı' barındırır ve 'kitap_listesi'nde int değerindedir.
            degerler = [int(cell), row, col]
        else:
            degerler = [cell,row,col]
        # Bir listeye atılıyor ve döndürülüyor.
        return degerler

    def veriGuncelle(self):
        aranan = self.tablodanGirdiAl()
        # aranan[0]->Tablo Değeri, aranan[1]->Satır, aranan[2]->Sutun
        # type(aranan) -> <class 'list'>
        self.aranankitap = list()  # Eşleştirme tamamlanınca kitap bilgilerinin yazılacağı liste
        if self.kitap_listesi[aranan[1]][aranan[2]] == aranan[0]:
            for i in range(0,5):
                self.aranankitap.append(str(self.kitap_listesi[aranan[1]][i]))
        self.kg = kitapMenu()
        # Güncellecek veriler 'lineEdit' üzerine elle yazılıyor.
        self.kg.le_kitapadi.setText(self.aranankitap[0])
        self.kg.le_yazar.setText(self.aranankitap[1])
        self.kg.le_tur.setText(self.aranankitap[2])
        self.kg.le_yayinevi.setText(self.aranankitap[3])
        self.kg.le_baskiSayisi.setText(self.aranankitap[4])


    def veriSil(self):
        self.lb_durumYazisi.setText("Silme işlemi gerçekleşecek!")
        def silmeİslemi():
            self.kutup.veri_sil(self.kitapAdi)
            self.kitap_listesi = self.kutup.butun_verileri_al()
            self.kitap_listesi = sorted(self.kitap_listesi)
            self.tabloyaVeriYazma(self.kitap_listesi)

        aranan = self.tablodanGirdiAl()
        if self.kitap_listesi[aranan[1]][aranan[2]] == aranan[0]:
            self.kitapAdi = self.kitap_listesi[aranan[1]][0]
            ks = kitapsil()
            ks.bt_tamam.clicked.connect(silmeİslemi)
        else:
            self.lb_durumYazisi.setText("Lütfen tablodan silmek istediğiniz kitabı seçtikten sonra butona tıklayınız.")

    def hakkinda(self):
        hak = hakkinda()
        self.lb_durumYazisi.setText("Kolcuoglu © 2017 - Bütün Hakları Özgürdür! ")
        # Bellek boşaltım işleri
        del hak

    def retranslateUi(self, anaPencere):
        anaPencere.setWindowTitle("Kütüphane Veritabanı")

        # Menübar'daki Menü ve Action'lar adlandırılıyor.
        self.m_dosya.setTitle("Dosya")
        self.m_yardim.setTitle("Yardım")
        self.act_farkliKaydet.setText("Farklı Kaydet")
        self.act_cikis.setText("Çıkış")
        self.act_hakkinda.setText("Hakkında")

        # Diğer bileşenlerin adlandırılması yapılıyor.
        self.gb_islemler.setTitle("İşlemler")
        self.bt_kitapEkle.setText("Kitap Ekle")
        self.bt_veriGuncelle.setText("Veri Güncelle")
        self.bt_kitapSil.setText("Kitap Sil")
        self.gb_filtre.setTitle("Filtrele")
        self.rb_kitapadi.setText("Kitap Adı")
        self.rb_yazar.setText("Yazar Adı")
        self.rb_yayinevi.setText("Yayınevi")
        self.rb_tur.setText("Tür")
        self.bt_filtrele.setText("Filtrele")
        self.lb_durumYazisi.setText("Kutuphane Veritabanına Hoş Geldiniz!")


class kitapMenu(QtWidgets.QDialog):
    def __init__(self, parent = None ):
        super(kitapMenu, self).__init__(parent)
        self.lb_yazi = QtWidgets.QLabel()
        self.lb_kitapadi = QtWidgets.QLabel("Kitap Adı :")
        self.lb_yazar = QtWidgets.QLabel("Yazar : ")
        self.lb_tur = QtWidgets.QLabel("Tür : ")
        self.lb_yayinevi = QtWidgets.QLabel("Yayınevi : ")
        self.lb_baskiSayisi = QtWidgets.QLabel("Baskı Sayısı :")
        self.le_kitapadi = QtWidgets.QLineEdit("")
        self.le_yazar = QtWidgets.QLineEdit("")
        self.le_tur = QtWidgets.QLineEdit("")
        self.le_yayinevi = QtWidgets.QLineEdit("")
        self.le_baskiSayisi = QtWidgets.QLineEdit("")
        self.bt_tamam = QtWidgets.QPushButton()
        self.init_ui()

    def init_ui(self):
        self.resize(270, 225)
        self.setMinimumSize(QtCore.QSize(270, 225))
        self.setMaximumSize(QtCore.QSize(270, 225))

        vbl_lbDuzeni = QtWidgets.QVBoxLayout()
        vbl_lbDuzeni.addWidget(self.lb_kitapadi)
        vbl_lbDuzeni.addWidget(self.lb_yazar)
        vbl_lbDuzeni.addWidget(self.lb_tur)
        vbl_lbDuzeni.addWidget(self.lb_yayinevi)
        vbl_lbDuzeni.addWidget(self.lb_baskiSayisi)

        vbl_leDuzeni = QtWidgets.QVBoxLayout()
        vbl_leDuzeni.addWidget(self.le_kitapadi)
        vbl_leDuzeni.addWidget(self.le_yazar)
        vbl_leDuzeni.addWidget(self.le_tur)
        vbl_leDuzeni.addWidget(self.le_yayinevi)
        vbl_leDuzeni.addWidget(self.le_baskiSayisi)

        hbl_duzen = QtWidgets.QHBoxLayout()
        hbl_duzen.addLayout(vbl_lbDuzeni, stretch=0)
        hbl_duzen.addLayout(vbl_leDuzeni, stretch=0)

        vbl_duzen = QtWidgets.QVBoxLayout()
        vbl_duzen.addStretch(2)
        vbl_duzen.addWidget(self.lb_yazi)
        vbl_duzen.addStretch(5)
        vbl_duzen.addLayout(hbl_duzen)
        vbl_duzen.addStretch(5)
        vbl_duzen.addWidget(self.bt_tamam)

        self.setLayout(vbl_duzen)

        # Kitap Ekleme ve Göncelleme aynı arayüzü kullandığı için 'Sender' methodu kullanıldı.
        self.gonderen = self.sender()
        # Gönderene göre düzenlenen başlık, durum yazısı ve buton yazısı kodları
        if self.gonderen == ui.bt_kitapEkle:
            self.setWindowTitle("Kitap Ekle")
            self.lb_yazi.setText("Uygun Değerleri Girerek 'Kitap Ekle' Tuşuna Basınız.")
            self.bt_tamam.setText("Kitap Ekle")
        elif self.gonderen == ui.bt_veriGuncelle:
            self.setWindowTitle("Kitap Güncelle")
            self.lb_yazi.setText("Uygun Değerleri Girerek 'Verileri Güncelle' Tuşuna Basınız.")
            self.bt_tamam.setText("Verileri Güncelle")

        self.show()

        self.bt_tamam.clicked.connect(self.tamamButonu)

    def tamamButonu(self):
        try:
            # d_bilgiler lineEdit'in içine yazdığımız değerleri bir demet içinde topluyor.
            # type(d_bilgiler) -> <class 'tuple'>
            self.l_bilgiler = [self.le_kitapadi.text().capitalize(), self.le_yazar.text().capitalize(), self.le_tur.text().capitalize(), self.le_yayinevi.text().capitalize(), int(self.le_baskiSayisi.text())]
            if type(self.l_bilgiler[4]) != int:  # Baskı Sayısı bir int değer olmalı. Yoksa verinin eklenmesine izin verilmez
                raise TypeError
            for i in self.l_bilgiler:
                if i == " " or i == "":
                    self.lb_yazi.setText("Eksik Bilgi Girdiniz.\nLütfen Tekrar Deneyiniz!")
                    self.l_bilgiler = list()  # Eksik bilgi girildiğinde 'd_bilgiler'in içeriği boşaltılıyor. Bu sayede veri eklemesi engelleniyor.
            if len(self.l_bilgiler) == 5:  # demet üzerinde Kitap için gereken 5 değerin tamamı uygun şekilde girildiğinde çalışır.
                kutuphane = Kutuphane()
                try:
                    if self.gonderen == ui.bt_kitapEkle:
                        kutuphane.veri_ekle(kutuphane.veri_bilgisi_girisi(self.l_bilgiler))
                        ui.lb_durumYazisi.setText("Kitap Ekleme İşlemi Tamamlandı! Girilen kitabın adı -> {}".format(self.l_bilgiler[0]))
                    elif self.gonderen == ui.bt_veriGuncelle:
                        kutuphane.veri_guncelle(ui.aranankitap,self.l_bilgiler)
                        ui.lb_durumYazisi.setText("Kitap Güncelleme İşlemi Tamamlandı! Girilen kitabın adı -> {}".format(self.l_bilgiler[0]))
                except:
                    self.lb_yazi.setText("Veriler yazılırken hata oluştu!\nLütfen bilgilerin kontrol edip tekrar deneyiniz.")
                finally:
                    ui.kitap_listesi = kutuphane.butun_verileri_al()  # Yeni eklenen kitabıda içeren tablo verisi alınıyor.
                    ui.kitap_listesi = sorted(ui.kitap_listesi)  # Liste alfabetik sıralanıyor.
                    ui.tabloyaVeriYazma(ui.kitap_listesi)  # MainWindow 'ui' nesnesi üzerinde tanımlı olduğu için ui çağrıldı.
                    kutuphane.baglantiyi_kes()  # 'kutuphane' nesnesinin üzerindeki SQL Bağlantısı sonlandırılıyor.
                    self.close()  # Kitap Ekle QDialog'u kapatılıyor
                    # Bellek boşaltım işlemleri
                    del kutuphane
                    del self.l_bilgiler
                    del self
        except TypeError:
            self.lb_yazi.setText("Baskı Sayısı Sayı Değerinde olmalıdır!\nLütfen Doğru Değer Giriniz!")
        except:
            self.lb_yazi.setText("Eksik ya da Yanlış Bilgi Girdiniz.\nLütfen Tekrar Deneyiniz!")

class kitapsil(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(kitapsil, self).__init__(parent)
        self.lb_yazi = QtWidgets.QLabel()
        self.bt_tamam = QtWidgets.QPushButton("Tamam")
        self.bt_iptal = QtWidgets.QPushButton("İptal")
        self.init_ui()

    def init_ui(self):
        self.resize(250, 150)
        self.setMinimumSize(QtCore.QSize(250, 150))
        self.setMaximumSize(QtCore.QSize(250, 150))

        self.lb_yazi.setText("Seçtiğiniz kitap silinecek!\nSilmek istediğinize Emin Misiniz?\nKitap Adı -> {}".format(ui.kitapAdi))

        hbl_duzen = QtWidgets.QHBoxLayout()
        hbl_duzen.addWidget(self.bt_tamam)
        hbl_duzen.addWidget(self.bt_iptal)

        vbl_duzen = QtWidgets.QVBoxLayout()
        vbl_duzen.addWidget(self.lb_yazi)
        vbl_duzen.addLayout(hbl_duzen)

        self.setLayout(vbl_duzen)
        self.setWindowTitle("Kitap Silinecek")
        self.show()

        self.bt_tamam.clicked.connect(lambda x: self.close())
        self.bt_iptal.clicked.connect(lambda x: self.close())



class hakkinda(QtWidgets.QDialog):
    def __init__(self, parent = None ):
        super(hakkinda, self).__init__(parent)
        self.lb_yazi = QtWidgets.QLabel()
        self.bt_tamam = QtWidgets.QPushButton("Tamam")
        self.init_ui()

    def init_ui(self):
        self.resize(250, 150)
        self.setMinimumSize(QtCore.QSize(250, 150))
        self.setMaximumSize(QtCore.QSize(250, 150))

        self._str = (
            """
Kütüphane Veritabanı 2017.9.10

Python v3.5.2 & PyQt v5.6 ile hazırlandı!
GNU General Public License v3.0 lisanslıdır.
    
Kolcuoglu © 2017
            """)
        self.lb_yazi.setText(self._str)

        vbl_duzen = QtWidgets.QVBoxLayout()
        vbl_duzen.addWidget(self.lb_yazi)
        vbl_duzen.addWidget(self.bt_tamam)

        self.setLayout(vbl_duzen)
        self.setWindowTitle("Hakkında")
        self.show()

        self.bt_tamam.clicked.connect(lambda x: self.close())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    anaPencere = QtWidgets.QMainWindow()
    ui = Kutuphane_GUI()
    ui.setupUi(anaPencere)
    anaPencere.show()
    sys.exit(app.exec_())

# -----------------------------------------------------------------------------
#     +Bilinen Bugları:
#   -Filtreleme yaptıktan sonra RadioButton'un tıklanık olarak gözükmesi.
#   -Filtrelenen verileri güncellemiyor veya silmiyor.
# -----------------------------------------------------------------------------