import re

def check_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).+$"
    if re.match(pattern, password):
        return True
    else:
        return False

def main():
    while True:
        user_pass = input("Şifrenizi girin: ")
        if check_password(user_pass):
            print("Şifre kabul edildi.")
            break
        else:
            print("Şifre zayıf.")

if __name__ == "__main__":
    main()