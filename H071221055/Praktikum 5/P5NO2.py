print('===========================================================')
print('  Selamat datang untuk memulai, silahkan input data anda! ')
print('===========================================================')

nama = input('Input nama: ')
umur = int(input('Input umur: '))
alamat = input('Input alamat: ')

datadiri = {
    'Nama': nama,
    'Umur': umur, 
    'Alamat': alamat
}

while True: 
    print('===========================================================')
    print(f'\t Selamat datang {nama}, silahkan pilih opsi')
    print('===========================================================')
    print('1. Detail anda')
    print('2. Ubah Nama')
    print('3. Ubah Umur')
    print('4. Ubah Alamat')
    print('5. Keluar')
    print('===========================================================')
    opsi = int(input('Input opsi: '))
    print('===========================================================')
    if opsi == 1:
        print('Data anda adalah')
        print('Nama:', datadiri['Nama'])
        print('Umur:', datadiri['Umur'])
        print('Alamat:', datadiri['Alamat'])
    elif opsi == 2:
        nama = input('Silahkan input nama baru: ')
        datadiri['Nama'] = nama
        print('Data anda sukses diperbarui')
    elif opsi == 3:
        umur = int(input('Silahkan input umur baru: '))
        datadiri['Umur'] = umur
        print('Data anda sukses diperbarui')
    elif opsi == 4:
        alamat = input('Silahkan input alamat baru: ')
        datadiri['Alamat'] = alamat
        print('Data anda sukses diperbarui')
    elif opsi == 5:
        print(f'Selamat tinggal {nama}')
        break 
    else:
        print('Opsi salah, masukkan ulang opsi yang benar!')
