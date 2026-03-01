import datetime
import random

class Asistan:
    def __init__(self, name):
        self.name = name
        self.islem_sayisi = 0 
        print(f"Sistem: '{self.name}' isimli asistan başlatıldı...\n")

    def selam_ver(self, username):
        print(f"Merhaba {username}, ben {self.name}. Sana nasıl yardım edebilirim?")
        self.islem_sayisi += 1

    def saat_soyle(self):
        su_an = datetime.datetime.now().strftime("%H:%M")
        print(f"{self.name}: Şu an saat {su_an}.")
        self.islem_sayisi += 1

    def zar_at(self):
        zar = random.randint(1, 6)
        print(f"{self.name}: Senin için bir zar attım, sonuç: {zar}")
        self.islem_sayisi += 1

    def durum_raporu(self):
        print("-" * 30)
        print(f"{self.name} Durum Raporu:")
        print(f"Bugüne kadar toplam {self.islem_sayisi} işlem gerçekleştirdim.")
        print("-" * 30)

def main():
    benim_asistan = Asistan("Kumru")
    benim_asistan.selam_ver("Patron")
    benim_asistan.saat_soyle()
    benim_asistan.zar_at()
    benim_asistan.selam_ver("Misafir")
    benim_asistan.durum_raporu()

if __name__ == "__main__":
    main()