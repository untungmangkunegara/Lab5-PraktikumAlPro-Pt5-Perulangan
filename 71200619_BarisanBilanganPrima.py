# Rudi adalah seorang anak yang saat ini memasuki kelas 4 SD, 
# ia memiliki tugas untuk menuliskan semua barisan bilangan prima dari jarak tertentu. 
# Karena kemungkinan jarak antar angka yang diperintahkan terlalu lebar, 
# buatlah sebuah program untuk mencari tau barisan bilangan prima dari jarak tertentu untuk membantu Rudi menyelesaikan tugasnya.
# input=angka awal, angka akhir
# proses=fungsi for
# output= bilangan prima
# ============================================
print("Selamat datang di Program Barisan Bilangan Prima")
#input
angka_awal=int(input("Masukkan angka awal: "))
angka_akhir=int(input("Masukkan angka akhir: "))
#output
print("Bilangan prima diantara",angka_awal,"dan",angka_akhir,"adalah: ")
#proses
for i in range (angka_awal,angka_akhir+1):
    if i>1:
        for x in range (2,i):
            if (i%x)==0:
                break
        else:
            print(i, end=" ")