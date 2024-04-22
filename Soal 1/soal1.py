file1 = input("Masukkan nama file pertama: ")
file2 = input("Masukkan nama file kedua: ")

with open(file1, 'r') as f1, open(file2, 'r') as f2:
    baris1 = f1.readlines()
    baris2 = f2.readlines()

for i in range(len(baris1)):
    line1 = baris1[i]
    line2 = baris2[i]

    if line1 == line2:
        print("Perbedaan pada baris " + str(i + 1) + ":")
        print("File 1: " + line1.strip())
        print("File 2: " + line2.strip())
        print()