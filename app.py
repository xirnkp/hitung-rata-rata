# meminta pengguna untuk memasukan nilai numerik 
input_str = input("masukan nilai-nilai numerik, pisahkan dengan koma: ")

# memisahkan nilai-nilai numerik menjadi list
nilai_list = input_str.split(",")

# memgubah nilai dalam list dari string ke floatf
nilai_list = [float(nilai) for  nilai in nilai_list]

# menghitung rata-rata dari nilai dalam list
rata_rata = sum(nilai_list) /  len(nilai_list)

# mencetak hasil
print("Nilai rata-ratanya adalah:", rata_rata)