import sqlite3
from Data import Data

class Barang(Data) :
    
    def __init__(self,tipe_barang,jenis_barang,merk,jumlah,harga):
        super().__init__()
        self.tipeBarang = tipe_barang
        self.jenisBarang = jenis_barang
        self.merk = merk
        self.jumlah = jumlah
        self.harga = harga
    
    def tambah(self):
        databarang = self.execute(f'SELECT*FROM Barang WHERE tipeBarang = "{barang.tipeBarang}"')
        for row in databarang:
            if barang.tipeBarang in row:
                  self.execute(f'UPDATE Barang SET jumlah=(jumlah+"{barang.jumlah}")')
                  self.commit()
                  print ("Berhasil dilakukan")
            break
        else:
            query = f'INSERT INTO Barang(tipeBarang,jenisBarang,merk,jumlah,harga) VALUES ("{barang.tipeBarang}","{barang.jenisBarang}","{barang.merk}","{barang.jumlah}","{barang.harga}")'
            self.execute(query)
            self.commit()
            print ("Data berhasil ditambahkan")
    
    def lihat(self):
        data = self.execute("SELECT * FROM Barang")
        for row in data:
            print (f'Kode Barang: {row[0]} | Tipe Barang: {row[1]}   | Jenis Barang: {row[2]}    | Jumlah: {row[4]} | Harga Barang: {row [5]}')

    def ubah(self):
        kode=input("Masukkan kode barang yang ingin diubah: ")
        barang = Barang(input("Tipe: "),input("Jenis: "),input("Merk: "),None,int(input("Harga: ")))
        query = f'UPDATE Barang SET(tipeBarang,jenisBarang,merk,harga)= ("{barang.tipeBarang}","{barang.jenisBarang}","{barang.merk}","{barang.harga}") WHERE kodeBarang={kode}'
        self.execute(query)
        self.commit()
        print ("Data berhasil diubah")

    def hapus(self):
        kode = int(input('Masukkan kode: '))
        query = f'DELETE FROM Barang WHERE kodeBarang={kode}'
        self.execute(query)
        self.commit()
        print ("Data berhasil dihapus")
                  
while True:
    barang=Barang('','','','','')
    pilih=int(input("\nAdmin Menu(Barang) \n1.Menambah Data \n2.Melihat Data \n3.Mengubah Data \n4.Menghapus Data \n5.Kembali \nPilih: "))
    if pilih==1:
        barang = Barang(input("Tipe: "),input("Jenis: "),input("Merk: "),int(input("Jumlah: ")),int(input("Harga: ")))
        barang.tambah()
    elif pilih==2:
        barang.lihat()
    elif pilih==3:
        barang.ubah()
    elif pilih==4:
        barang.hapus()
    elif pilih==5:
        from Utama import Utama
    else:
        print("Menu tidak ada")
