def main():

    name = input("Adın ne? ")
    age = int(input("Yaşın kaç? "))

    if age >= 100:
        print("Zaten 100 yaşını geçmişsin veya 100 yaşındasın.")
    else:
        currentyear = 2025
        yearsleft = 100 - age
        resultyear = currentyear + yearsleft
        print(f"Merhaba {name}, {resultyear} yılında 100 yaşında olacaksın.")

main()