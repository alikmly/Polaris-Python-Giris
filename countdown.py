import time
def main():
    while True:
        try:
            second = int(input("Geri sayım kaçtan başlasın? "))
            if second > 0:
                break
            print("Lütfen 0'dan büyük bir sayı girin.")
        except ValueError:
            print("Lütfen geçerli bir rakam girin!")
    print(f"\n{second} saniyelik geri sayım başlatılıyor.\n")

    for i in range(second, 0, -1):
        print(i)
        time.sleep(1)
    print("0")
    print("Ateşle!")

if __name__ == "__main__":
    main()