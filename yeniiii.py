import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QShortcut
from PyQt5.QtGui import QIcon, QPixmap, QFont, QKeySequence
from PyQt5.QtCore import Qt
from random import choice


class Pencere(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.puan = 0

        self.tekrar_buton = QPushButton('►', self)
        self.tekrar_buton.move(460, 550)
        self.tekrar_buton.hide()
        self.tekrar_buton.resize(200, 80)
        self.tekrar_buton.clicked.connect(self.tekrar_basla)

        self.kullanici_text = QLabel(self)
        self.kullanici_text.setText("...")
        self.kullanici_text.move(280, 300)
        self.kullanici_text.setFixedWidth(100)
        self.kullanici_text.setFixedHeight(100)

        self.makina_text = QLabel(self)
        self.makina_text.setText("...")
        self.makina_text.move(800, 300)
        self.makina_text.setFixedWidth(100)
        self.makina_text.setFixedHeight(100)

        self.sonuc_text = QLabel(self)
        self.sonuc_text.move(300, 250)
        self.sonuc_text.setFixedWidth(500)
        self.sonuc_text.setFixedHeight(300)# Genişliği arttırıldı
        self.sonuc_text.setAlignment(Qt.AlignCenter)  # Metni merkeze hizala
        self.sonuc_text.setStyleSheet("font-size: 32px;")

        self.sonuc2_text = QLabel(self)
        self.sonuc2_text.move(525, 450)
        self.sonuc2_text.setFixedWidth(300)
        self.sonuc2_text.setFixedHeight(100)
        self.sonuc2_text.setStyleSheet("font-size: 32px;")

        self.kullanici_gorsel = QLabel(self)
        self.kullanici_gorsel.move(180, 0)
        self.kullanici_gorsel.setPixmap(QPixmap("kullanici_tas.png").scaled(500,500, Qt.KeepAspectRatio))
        self.kullanici_gorsel.setFixedSize(500, 500)

        self.makina_gorsel = QLabel(self)
        self.makina_gorsel.move(640, 0)
        self.makina_gorsel.setPixmap(QPixmap("makina_tas.png").scaled(500, 500, Qt.KeepAspectRatio))
        self.makina_gorsel.setFixedSize(500, 500)

        self.taş_buton = QPushButton('Taş', self)
        self.taş_buton.move(500, 608)
        self.taş_buton.clicked.connect(self.tas_secildi)

        self.kağıt_buton = QPushButton('Kağıt', self)
        self.kağıt_buton.move(500, 640)
        self.kağıt_buton.clicked.connect(self.kagit_secildi)

        self.makas_buton = QPushButton('Makas', self)
        self.makas_buton.move(500, 672)
        self.makas_buton.clicked.connect(self.makas_secildi)

        self.setWindowTitle("Taş - Kağıt - Makas")
        self.setGeometry(350, 200, 1200, 700)

    def tekrar_basla(self):
        # Mevcut pencereyi kapatır
        self.close()

        # Yeni bir Pencere örneği oluşturarak uygulamayı yeniden başlatır
        self.yeni_pencere = Pencere()
        self.yeni_pencere.show()

    def tas_secildi(self):
        self.kullanici = "taş"
        self.bilgisayar_sec()
        self.kullanici_gorsel.setPixmap(QPixmap("kullanici_tas.png").scaled(500,500, Qt.KeepAspectRatio))
        self.karsilastir()

    def kagit_secildi(self):
        self.kullanici = "kağıt"
        self.bilgisayar_sec()
        self.kullanici_gorsel.setPixmap(QPixmap("kullanici_kagit.png").scaled(500,500, Qt.KeepAspectRatio))
        self.karsilastir()

    def makas_secildi(self):
        self.kullanici = "makas"
        self.bilgisayar_sec()
        self.kullanici_gorsel.setPixmap(QPixmap("kullanici_makas.png").scaled(500, 500, Qt.KeepAspectRatio))
        self.karsilastir()

    def bilgisayar_sec(self):
        secenekler = ["taş", "kağıt", "makas"]
        self.bilgisayar = choice(secenekler)

        if self.bilgisayar == "taş":
            self.makina_gorsel.setPixmap(QPixmap("makina_tas.png").scaled(500, 500, Qt.KeepAspectRatio))
        elif self.bilgisayar == "kağıt":
            self.makina_gorsel.setPixmap(QPixmap("makina_kagıt.png").scaled(500, 500, Qt.KeepAspectRatio))
        elif self.bilgisayar == "makas":
            self.makina_gorsel.setPixmap(QPixmap("makina_makas.png").scaled(500, 500, Qt.KeepAspectRatio))

    def karsilastir(self):
        if self.kullanici == self.bilgisayar:
            self.sonuc = "Berabere!"



            self.sonuc2_text.setText(f"0")
        elif (self.kullanici == "taş" and self.bilgisayar == "makas") or \
                (self.kullanici == "kağıt" and self.bilgisayar == "taş") or \
                (self.kullanici == "makas" and self.bilgisayar == "kağıt"):
            self.sonuc = "Kazandınız!"
            self.puan += 1
            self.sonuc2_text.setStyleSheet("color: green; font-size: 32px;")
            self.sonuc2_text.setText(f"+1")
        else:
            self.sonuc = "Kaybettiniz!"
            self.puan -= 1
            self.sonuc2_text.setStyleSheet("color: red;  font-size: 32px;")
            self.sonuc2_text.setText(f"-1")


        if self.puan == 5 or self.puan == -5:
            if self.puan >= 5:
                self.sonuc_text.setStyleSheet("color: green; font-size: 32px;")
                self.sonuc2_text.setText("You Win")
            elif self.puan <= -5:
                self.sonuc_text.setStyleSheet("color: red; font-size: 32px;")
                self.sonuc2_text.setText("Game Over")
            self.sonuc2_text.move(480, 450)
            self.taş_buton.hide()
            self.kağıt_buton.hide()
            self.makas_buton.hide()
            self.tekrar_buton.show()

        self.kullanici_text.setText(self.kullanici)
        self.kullanici_text.setStyleSheet("font-size: 32px;")
        self.makina_text.setText(self.bilgisayar)
        self.makina_text.setStyleSheet("font-size: 32px;")
        self.sonuc_text.setText(f" {self.sonuc}    Puan: {self.puan}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = Pencere()
    pencere.show()
    sys.exit(app.exec_())

