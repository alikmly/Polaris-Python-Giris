import re

def main():
    file_path = "lvl2_bozuk_veri.txt"
    output_path = "lvl2_temiz_rehber.txt"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("Dosya bulunamadı. Lütfen dosya ismini kontrol et.")
        return

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_pattern = r"(?:\+90\s?)?\(?0?\d{3}\)?[\s.-]\d{3}[\s.-]\d{2}[\s.-]\d{2}"
    emails = re.findall(email_pattern, content)
    phones = re.findall(phone_pattern, content)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(f"Bulunan E-postalar\n")
        for mail in sorted(set(emails)):
            file.write(f"{mail}\n")
        file.write(f"\nBulunan Telefonlar\n")
        for tel in sorted(set(phones)):
            file.write(f"{tel}\n")

    print(f"İşlem başarılı. Veriler '{output_path}' dosyasına kaydedildi.")
    print(f"İstatistik: {len(set(emails))} mail, {len(set(phones))} telefon bulundu.")
if __name__ == "__main__":
    main()