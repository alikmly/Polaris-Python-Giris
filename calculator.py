def main():
    
    x = float(input("Birinci sayı: "))
    y = float(input("İkinci sayı: "))

    print(f"Toplam: {x + y}")
    print(f"Fark:   {x - y}")
    print(f"Çarpım: {x * y}")

    if y != 0:
        print(f"Bölüm:  {round(x / y, 2)}")
    else:
        print("Bölüm:  Tanımsız")

main()