# login simulation (UNDOCUMENTED)
# bagian yang didokumentasikan ada di file pribadi

# ada 3 fungsi utama yang ingin saya buat disini
# 1. login <-- (check)
# 2. register <-- (check)
# 3. pesan masuk <-- check) & tampilkan data user <-- (check)
# 4. poles tampilan mungkin... (check)

import re
from datetime import datetime as dt

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
dummy_data = {  # / seeder
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
        return f"Selamat pagi! {name}!"
    elif now > 11 and now < 15:
        return f"Selamat siang {name}!"
    elif now > 15 and now < 18:
        return f"Selamat sore {name}!"

    return f"Tidur nyenyak, {name}!"


# ---- Service section / Logic business
def validate_email(email):
    if re.fullmatch(email_regex, email):
        return True

    return False


def validate_user_data(db, email_input, password_input):
    if not validate_email(email_input):
        raise ValueError("Domain tidak dapat dikenali")

    for user in db:
        if email_input == user["email"]:
            if password_input == user["password"]:
                print(
                    f"\n---- {greetings(user['username'])} ----"
                )  # greetings, horhorhor
                return
            else:
                raise ValueError("Password anda tidak sesuai")

    raise ValueError("Email anda tidak sesuai")


def display_user_data(db):
    print(f"| {'Nama':<20} | {'Email':<25} |")
    for user in db:
        print(f"| {user['username']:<20} | {user['email']:<25} |")


# ---- Main Program
sequenceDivider(length)
print(banner)
print(today_date)
sequenceDivider(length)

while True:
    print("\n1. Login akun")
    print("2. Daftar akun")
    print("3. Lihat semua akun")
    print("4. Keluar program\n")

    try:
        option = int(input("Pilih opsi : "))

        # biar lebih enak, nanti ubah ke case aja bagian if statements nya
        if option == 1:
            attempt = 0

            login_statements = True

            while login_statements:
                print("\nAnda login sebagai")
                email = input("Masukkan email anda\t: ").strip()
                password = input("Masukkan password anda\t: ").strip()

                try:
                    validate_user_data(database, email, password)
                    login_statements = False
                except ValueError as error_msg:
                    if str(error_msg) == "Password anda tidak sesuai":
                        attempt += 1

                    print(f"Terjadi kesalahan : {error_msg}")
                    print("\n[INFO] Silahkan coba kembali")

                if attempt == 3:
                    print("[DANGER] Akun anda terblokir. Coba lagi nanti")
                    login_statements = False

        elif option == 2:
            # persingkat ajah
            print("Silahkan isi data dibawah ini")
            register_statements = True

            while register_statements:
                email = input("Masukkan email anda\t: ")
                username = input("Masukkan username anda\t: ").strip()
                password = input("Masukkan password anda\t: ").strip()

                if not validate_email(email):
                    print("Email anda tidak sesuai")
                else:
                    break

            user_data = {"email": email, "username": username, "password": password}

            database.append(user_data)

            print(f"Akun, telah dibuat. Silahkan login {user_data['username']}!")
        elif option == 3:
            print("\nDaftar pengguna\n")
            display_user_data(database)
        elif option == 4:
            print("Goodbye!")
            break

        print("[INFO] Harap masukan nomor yang sesuai (1-4)")
    except ValueError:
        print("[INFO] Harap memasukkan nomor, bukan huruf ataupun simbol!")
