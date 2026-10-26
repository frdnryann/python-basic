# tentukan sudut abc
# sudut a, dari sisi kiri, b dari sisi bawah, c dari sisi kanan
a = int(input("Panjang sudut A : "))
b = int(input("Panjang sudut B : "))
c = int(input("Panjang sudut C : "))

# kondisi (jika sudut a dan b sama, dan lebih panjang dari c) maka sudut segitiga sama kaki
# kondisi (jika sudut a, b, dan c sama panjangnya) maka sudut segitiga sama sisi
# else (sudut a, b, dan c berbeda beda) maka sudut segitiga sembarang
if a == b and c < a or c < b:
    print("Segitiga sama kaki")
elif a == b and c == a or c == b:
    print("Segitiga sama sisi")
else:
    print("Segitiga sembarang")
