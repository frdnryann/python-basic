# Biaya parkir per-jam
BILL_PER_HOUR = 2000

# variable untuk menampung data parkir yang sudah ter-input
data = []
total = int

# variable untuk menampung boolean guna menghentikan infinite looping (jika false)
isActive = True

while isActive:
    startProgramExec = input("Mulai program ? (Y/n) : ")

    # Jika input startProgramExec (y)
    if startProgramExec.lower() == "y":
        id = int(input("ID struk : "))

        parkedHours = int(input("Berapa jam sudah terparkir? : "))

        # menampung data dari input kedalam variable bertipe dictionary / dict
        vehicleParkedData = {"ID": id, "parkedHours": parkedHours, "total": total}

        # ---- Debug state ----
        # print("[DEBUG DATA]", data, vehicleParkedData['parkedHours'])

        # jika inputan parkedHours yang disimpan kedalam dictionary tidak bernilai 0, maka :
        if vehicleParkedData["parkedHours"] != 0:
            # kalkulasi jam parkir dengan biaya per-jam
            total = BILL_PER_HOUR * parkedHours
            vehicleParkedData["total"] = total

            print("Total tagihan anda : Rp.", total)

            # menggabungkan semua array inputan(vehicleParkedData) kedalam array
            data.append(vehicleParkedData)

            # ---- Debug state ----
            # print("[DEBUG DATA]", vehicleParkedData)
        else:
            # jika perintah tidak dapat dikenali
            print("Hell nawhh.., Apaan ini dawg?")

    # jika input bernilai n, maka keluar dari program / infinte loop
    elif startProgramExec.lower() == "n":
        isActive = False
    else:
        print("Perintah tidak dikenali")

    # ---- Debug state ----
    # print("[DEBUG DATA]", data)
