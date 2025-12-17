def main():
    number = get_int("Lütfen bir sayı girin: ")
    print(f"Teşekkürler, girdiğiniz sayı: {number}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Hata! Lütfen harf değil, geçerli bir sayı giriniz.")

if __name__ == "__main__":
    main()