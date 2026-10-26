# for i in range(5):
#     for j in range(4):
#         print(f"i={j}, j={i}")

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print('*', end="")
#     print()

# generator samadengan, pembatas
def equalGenerator(n):
    loremTotal = len(n)
    for i in range(loremTotal):
        print("=", end="")

print("\"yes\", She said")
print("Isn't, they said")

# di python, string dapat digabungkan dengan special characters, contohnya dibawah
print("C:\this\name\ryanbajindul")
# C:      his
# yanbajindul <-- output

# dengan menggunakan r (raw), python akan mengeksekusi string dengan nilai mentah
# tidak memasukkan string bisa dianggap special character untuk output
print(r"C:\this\name\ryanbajindul")
# C:\this\name\ryanbajindul <--output

lorem = 3 * 'hor' + '-' # keren juga, bisa loop string di variabel
equalGenerator(lorem)
print("\n", lorem, '\n', lorem[0:4]) # lorem[0] ambil huruf di index ... (bebas) [:5] = range index
equalGenerator(lorem)

print(f"Loremvariable = {lorem}") # owww.., f dipake buat nambah variable ke string wak
print("Lorem ipsum dolor")

