class Dedektif:
    def __init__(self):
        self.supheliler = ["Albay Mustard", "Profesör Plum", "Bayan Scarlet"]
        print(f"Başlangıç Dosyası: {self.supheliler}\n")

    def supheli_ele(self, isim):
        if isim in self.supheliler:
            self.supheliler.remove(isim)
            print(f"Yeni Kanıt: '{isim}' masumdur. Listeden elendi.")
        else:
            print(f"'{isim}' zaten şüpheliler listesinde yok.")

    def suclu_kim(self):
        kalansayisi = len(self.supheliler)
        if kalansayisi == 1:
            print(f"Kesin bilgi, suçlu bulundu: {self.supheliler[0]}\n")
        elif kalansayisi > 1:
            print("Henüz yeterli kanıt yok.\n")
        else:
            print("Mantık hatası: Herkes elendi!\n")

def main():    
    yz_ajan = Dedektif()
    yz_ajan.suclu_kim()
    yz_ajan.supheli_ele("Albay Mustard")
    yz_ajan.suclu_kim()
    yz_ajan.supheli_ele("Bayan Scarlet")
    yz_ajan.suclu_kim()

if __name__ == "__main__":
    main()