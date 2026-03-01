class Roket:
    def __init__(self, isim, yakit_seviyesi):
        self.isim = isim
        self.yakit_seviyesi = int(yakit_seviyesi)
        print(f"'{self.isim}' roketi {self.yakit_seviyesi} birim yakıtla inşa edildi.")

    def yakit_doldur(self, miktar):
        if miktar > 0:
            self.yakit_seviyesi += miktar
            print(f"Yakıt eklendi. Yeni seviye: {self.yakit_seviyesi}")
        else:
            print("Hata: Eklenecek yakıt miktarı 0'dan büyük olmalıdır.")

    def firlat(self):
        print(f"[{self.isim}] Fırlatma sekansı başlatılıyor...")
        
        if self.yakit_seviyesi >= 10:
            self.yakit_seviyesi -= 10
            print("Roket başarıyla fırlatıldı!")
            print(f"Kalan yakıt seviyesi: {self.yakit_seviyesi}\n")
        else:
            print("Hata: Yetersiz yakıt! Lütfen yakıt doldurun.\n")

def main():
    print("--- UZAY MERKEZİ SİMÜLASYONU ---\n")
    apollo = Roket("Apollo 11", 5)
    print("\n--- 1. Fırlatma Denemesi ---")
    apollo.firlat()
    print("--- Yakıt İkmali ---")
    apollo.yakit_doldur(15)
    print("\n--- 2. Fırlatma Denemesi ---")
    apollo.firlat()
    print("--- 3. Fırlatma Denemesi (Kalan yakıtla) ---")
    apollo.firlat()

if __name__ == "__main__":
    main()