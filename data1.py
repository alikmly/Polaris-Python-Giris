import re

def main():
    file_path = "lvl1_bozuk_veri.txt"
    output_path = "lvl1_temiz_rehber.txt"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Hata: '{file_path}' bulunamadı. Lütfen dosyanın klasörde olduğundan emin ol.")
        return

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_pattern = r"(?:\+?\d{1,3}[\s]?)?\(?\d{3,4}\)?[\s.-]\d{3}[\s.-]\d{2,4}(?:[\s.-]\d{2})?"
    emails_found = re.findall(email_pattern, content)
    phones_found = re.findall(phone_pattern, content)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("Bulunan E-postalar\n")
        if emails_found:
            for mail in emails_found:
                file.write(mail + "\n")
        else:
            file.write("E-posta bulunamadı.\n")
        file.write("\nBulunan Telefonlar\n")
        if phones_found:
            for tel in phones_found:
                file.write(tel.strip() + "\n")
        else:
            file.write("Telefon numarası bulunamadı.\n")
    print(f"İşlem tamam. Veriler '{output_path}' dosyasına kaydedildi.")

if __name__ == "__main__":
    main()