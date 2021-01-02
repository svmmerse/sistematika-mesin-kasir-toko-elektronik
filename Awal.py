import sqlite3
from Data import Data

class aktor(Data):

    def register(self):
        username = input("Username: ")
        password = input("Password: ")
        register = f'INSERT INTO Pemilik (username, password,status) VALUES ("{username}","{password}","Admin")'
        self.execute(register)
        self.commit();
        print("Data berhasil ditambahkan")
    
    def loginAdmin(self):
        while True:
            username = input("Username: ")
            password = input("Password: ")
            query = f'SELECT*FROM Pemilik WHERE username = "{username}" AND password = "{password}"'
            hasil = self.execute(query)
            for row in hasil:
                if username and password in row:
                    print("Selamat Datang Admin")
                    from Utama import Utama
                    
            else:
                print("Username dan Password Salah")

    def loginKasir(self):
        while True:
            username = input("Username: ")
            password = input("Password: ")
            query = f'SELECT*FROM Kasir WHERE username = "{username}" AND password = "{password}"'
            hasil = self.execute(query)
            for row in hasil :
                if username and password in row:
                    print("Selamat Datang",row[1])
                    from penjualan import penjualan
            else:
                print("Username dan Password Salah")

aktor=aktor()    
while True:
    pilih=int(input("1.Register Pemilik \n2.Login Pemilik \n3.Login kasir \nPilih: "))
    if pilih==1:
        aktor.register()
    elif pilih==2:
        aktor.loginAdmin()
    elif pilih==3:
        aktor.loginKasir()
    else:
        print('pilihan tidak ada')
