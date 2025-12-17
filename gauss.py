def main():
    while True:
        try:
            n = int(input("Bir sayı girin: "))
            if n > 0:
                break
            print("Lütfen pozitif bir tam sayı girin.")
        except ValueError:
            print("Hatalı giriş, lütfen sadece sayı yazın.")

    total = (n * (n + 1)) // 2
    print(f"1'den {n}'e kadar olan sayıların toplamı: {total:,}")

if __name__ == "__main__":
    main()