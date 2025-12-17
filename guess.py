import random
def main():
    targetnumber = random.randint(1, 100)
    print("1 ile 100 arasında bir sayı tuttum, sayıyı tahmin et.")

    while True:
        try:
            guess = int(input("Tahminin nedir?: "))
            if guess < targetnumber:
                print("Daha yukarı çık.")
            elif guess > targetnumber:
                print("Daha aşağı in.")
            else:
                print(f"\nTebrikler, sayıyı buldun!")
                break
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    main()