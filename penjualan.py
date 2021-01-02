from Data import Data 
from datetime import datetime
class Penjualan(Data):
    def init(self, idPenjualan, tanggal, jumlah, harga):
        super().__init__()
        self.idPenjualan = idPenjualan
        self.tanggal = tanggal
        self.jumlah = jumlah
        self.harga = harga

    def tampil(self,pilih):
        if pilih==1:
            jenis="Mesin Cuci"
        elif pilih==2:
            jenis="Televisi"
        elif pilih==3:
            jenis="Kulkas"
        else:
            print("Tidak ada Pilihan")
            return
        data = self.execute(f'SELECT * FROM Barang WHERE jenisBarang="{jenis}"')
        for row in data:
            print (f'Kode Barang: {row[0]} ,Tipe Barang: {row[1]} ,Stok Barang: {row [4]}, Harga Satuan: {row [5]}')

    def transaksi(self):
        total=0
        while True:
            tanggal=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            kode =input("Masukkan kode barang pesanan: ")
            jumlah=int(input("Masukkan jumlah barang yang dipesan: "))
            data = self.execute(f'SELECT * FROM Barang WHERE kodeBarang="{kode}"')
            for row in data:
                semua=jumlah*row[5]
            total=total+semua
            print("Total: ",total)
            self.execute(f'INSERT INTO Penjualan (kodeBarang,tanggal,jumlah,total) VALUES ("{kode}","{tanggal}","{jumlah}","{total}")')
            self.execute(f'UPDATE Barang SET jumlah=(jumlah-"{jumlah}") WHERE kodeBarang="{kode}"')
            self.commit()
            lagi=input("Ingin menambah pesanan?(Y/T):")
            if (lagi=="Y") or (lagi=="y"):
                pass
            elif (lagi=="T")or (lagi=="t"):
                print("Selesai di lakukan")
                break
        



a=Penjualan()
while True:
    print("Menu Transaksi")
    a.tampil(int(input("1.Mesin Cuci \n2.Televisi \n3.Kulkas \nPilih: ")))
    a.transaksi()
     
