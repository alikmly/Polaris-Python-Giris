import datetime
def main():
    print("Lütfen tarihi şu formatta girin: Yıl-Ay-Gün Saat:Dakika")
    print("Örnek: 2025-12-16 09:00\n")

    while True:
        try:
            date = input("Sınav Tarihi: ")
            examtime = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Hatalı format! Lütfen '2025-12-16 09:00' gibi girin.")

    now = datetime.datetime.now()
    remainingtime = examtime - now
    if remainingtime.total_seconds() < 0:
        print("\nBu sınavın tarihi geçti.")
    else:
        day = remainingtime.days
        hour = remainingtime.seconds // 3600
        print(f"Sınava kalan süre: {day} gün, {hour} saat")

if __name__ == "__main__":
    main()