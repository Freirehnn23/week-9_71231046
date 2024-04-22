with open("soal.txt", "r+") as soal:
    for teks in soal:
        i = teks.strip().split(" || ")
        print(i[0])
        jawaban = input("jawab : ")
        if jawaban.lower() == i[1].lower().replace("\n", ""):
            print("Jawaban Anda Benar")
        else:
            print("Jawaban Anda Salah")