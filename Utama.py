from Data import Data

class utama(Data):

    def __init__(self):
        super().__init__()
        while True:
            pilih=int(input("Menu Administator \n1.Kasir\n2.Barang\n3.Penjualan\nPilih: "))
            if pilih==1:
                from kasir import kasir
            elif pilih==2:
                from barang import barang
            elif pilih==3:
                data=self.execute(f'SELECT*FROM penjualan')
                for row in data:
                    print (f'ID: {row[0]}\nKode barang: {row[1]}\nTanggal: {row [2]}\nJumlah: {row [3]}\nTotal: {row [4]}')
            else:
                print("Pilihan tidak ada")
        
        
utama=utama()
