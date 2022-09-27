Detik = int(input("Masukkan Jumlah Detik yang ingin di Hitung : "))

Jam = Detik // 3600 # guna// itu dibagi trus bulat kebawah
Sisa_Detik = Detik % 3600 # % tuh modulus cuy
Menit = Sisa_Detik // 60
Detik = Sisa_Detik % 60

print('%02d:%02d:%02d'%(Jam,Menit,Detik))