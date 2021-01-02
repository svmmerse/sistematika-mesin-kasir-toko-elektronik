import sqlite3
from Data import Data


class User :

    def __init__(self, username, password, status) :
        self.username = username
        self.password = password
        self.status = status
        
    @property
    def getUsername(self):
        pass

    @property
    def getPassword(self):
        pass

    @property
    def getStatus(self):
        pass

    @getUsername.getter
    def getUsername(self):
        return self.username

    @getPassword.getter
    def getPassword(self):
        return self.password

    @getStatus.getter
    def getStatus(self):
        return self.status

class Kasir(User) :

    def __init__(self,nama,alamat,no_hp,username,password,status):
        super().__init__(username, password, status)
        self.nama = nama
        self.alamat = alamat
        self.no_hp = no_hp
        self.status = "Kasir"

    @property
    def getNama(self):
        pass

    @property
    def getAlamat(self):
        pass

    @property
    def getNoHp(self):
        pass

    @getNama.getter
    def getNama(self):
        return self.nama

    @getAlamat.getter
    def getAlamat(self):
        return self.alamat

    @getNoHp.getter
    def getNoHp(self):
        return self.no_hp

class Pengguna(Data):
        
    def daftar(self):
        kasir = Kasir(input("Nama: "),input("Alamat: "),input("No HP: "),input("Username: "),input("Password: "),'Kasir')
        query = f'INSERT INTO Kasir(nama,alamat,noHp,status,username,password) VALUES ("{kasir.getNama}","{kasir.getAlamat}","{kasir.getNoHp}","{kasir.getStatus}","{kasir.getUsername}","{kasir.getPassword}")'
        self.execute(query)
        self.commit()
        print ("Data berhasil ditambahkan")

    def melihat(self):
        data = self.execute("SELECT * FROM Kasir")
    
        for row in data:
            print ("ID:",f'{row[0]}',"\nNama:",f'{row[1]}',"\nAlamat:",f'{row [2]}',"\nNo HP:",f'{row [3]}',"\nStatus",f'{row [4]}',"\nUsername:",f'{row [5]}',"\nPassword:",f'{row[6]}')

    def mengubah(self):
        no_id=input("Masukkan id data yang ingin diubah: ")
        nama = input("Nama baru: ")
        alamat = input("Alamat baru: ")
        nohp = input("No Hp baru: ")
        username = input("Username baru: ")
        password = input("Password baru: ")
        query = f'UPDATE Kasir SET (nama,alamat,noHp,username,password)= ("{nama}","{alamat}","{nohp}","{username}","{password}") WHERE id={no_id}'
        self.execute(query)
        self.commit()
        print ("Data berhasil diubah")

    def menghapus(self):
        nomor_id = int(input('Masukkan ID: '))
        query = f'DELETE FROM Kasir WHERE id={nomor_id}'
        self.execute(query)
        self.commit()
        print ("Data berhasil dihapus")
        
while True:
    kasir=Pengguna()
    pilih=int(input("\nAdmin Menu(Kasir) \n1.Menambah Data \n2.Melihat Data \n3.Mengubah Data \n4.Menghapus Data \n5.Keluar \nPilih: "))
    if pilih==1:
        kasir.daftar()
    elif pilih==2:
        kasir.melihat()
    elif pilih==3:
        kasir.mengubah()
    elif pilih==4:
        kasir.menghapus()
    elif pilih==5:
        from Utama import Utama
    else:
        print("Menu tidak ada")
        




    
