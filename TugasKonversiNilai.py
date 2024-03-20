masukkan_bilangan = int(input("Masukkan Angka Anda Yang Diinginkan: "))
masukkan_pilihan_user = int(input("Silahkan Pilih 1, 2, 3, atau 4: "))

bil_bin = bin(masukkan_bilangan)[2:]
bil_oktal = oct(masukkan_bilangan)[2:]
bil_des = masukkan_bilangan
bil_hex = hex(masukkan_bilangan)[2:]

def pilih_operasi(pilihan):
    if pilihan == 1:
        print("Bilangan Biner Dari", masukkan_bilangan, "Adalah", bil_bin)
    elif pilihan == 2:
        print("Bilangan Oktal Dari", masukkan_bilangan, "Adalah", bil_oktal)
    elif pilihan == 3:
        print("Masukkan Bilangan Desimal Dari", masukkan_bilangan, "Adalah", bil_des)
    elif pilihan == 4:
        print("Bilangan Hexadesimal Dari", masukkan_bilangan, "Adalah", bil_hex)
    else:
        print("Pilihan Tidak Sesuai")

pilih_operasi(masukkan_pilihan_user)