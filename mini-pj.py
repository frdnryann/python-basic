# login simulation (UNDOCUMENTED)
# bagian yang didokumentasikan ada di file pribadi

# ada 3 fungsi utama yang ingin saya buat disini
# 1. login <-- (check)
# 2. register <-- (check)
# 3. pesan masuk <-- check) & tampilkan data user <-- (belum)
# 4. poles tampilan mungkin...

import re
from datetime import datetime as dt

# loop = True
today_date = dt.now().strftime("%A %d. %B %Y - %H:%M")
email_regex = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
banner = r"""
 _                _       
| |    ___   __ _(_)_ __  
| |   / _ \ / _` | | '_ \ 
| |__| (_) | (_| | | | | |
|_____\___/ \__, |_|_| |_| sim
            |___/         

by  : ryanBajindul
NIM : iykyk
"""
length = len(banner)

# ---- Database section
database = []
dummy_data = {
    "email": "Lorem@gmail.com",
    "username": "ryan bajindul",
    "password": "ryanbajindul24432",
}

database.append(dummy_data)


# ---- Helper section
def sequenceDivider(n: int):
    len = int(n / 5.5)
    for i in range(len):
        print("=", end="")
    print()


def greetings(name):
    now = int(dt.now().strftime("%H"))

    if now > 5 and now < 11:
        print(f"Selamat pagi! {name}!")
    elif now > 11 and now < 15:
        print(f"Selamat siang {name}!")
    elif now > 15 and now < 18:
        print(f"Selamat sore {name}!")
    else:
        print(f"Tidur nyenyak, {name}!")


# ---- Service section / Logic business
def validate_email(email):
    if re.fullmatch(email_regex, email):
        return True

    return False


def validate_user_data(db, email_param, password_param):
    if not validate_email(email_param):
        print("Domain tidak dapat dikenali")
        return False

    for user in db:
        if email_param == user["email"]:
            if password_param == user["password"]:
                print(greetings(user["username"]))  # greetings, horhorhor
                return True
            else:
                print("Password tidak sesuai jir")
                return False

    print("Email tidak Sesuai jir, daftar sana")
    return False


def display_user_data(db):
    for user in db:
        print(user["email"])


# ---- Main Program
sequenceDivider(length)
print(banner)
print(today_date)
sequenceDivider(length)

while True:
    print("\n1. Login akun")
    print("2. Daftar akun")
    print("3. Keluar program\n")

    option = int(input("Pilih opsi : "))

    if option == 1:
        print("Anda login sebagai\n")
        email = input("Masukkan email anda : ")
        password = input("Masukkan password anda : ")

        validate_user_data(database, email, password)
        display_user_data(database)
    elif option == 2:
        print("Silahkan isi data dibawah ini")
        option_statements = True

        while option_statements:
            email = input("Masukkan email anda : ")
            username = input("Masukkan username anda : ")
            password = input("Masukkan password anda : ")

            if not validate_email(email):
                print("Email tidak sesuai bung..,")
            else:
                # print("Pass")
                break

        user_data = {"email": email, "username": username, "password": password}

        database.append(user_data)

        print(f"Akun, telah dibuat. Silahkan login {user_data['username']}!")
    elif option == 3:
        print("Goodbye!")
        break
    else:
        print("Perintah tidak dikenali")
        break
