def main():
    
    number = float(input("Bir sayı girin: "))

    if number > 0:
        print("Bu sayı pozitiftir.")
    elif number < 0:
        print("Bu sayı negatiftir.")
    else:
        print("Bu sayı sıfırdır.")

main()