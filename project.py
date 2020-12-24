class User :

    def __init__(self, username, password, status) :
        self.username = username
        self.password = password
        
    @property
    def setUsername(self):
        pass

    @property
    def getUsername(self):
        pass

    @property
    def setPassword(self):
        pass

    @property
    def getPassword(self):
        pass
    
    @property
    def setStatus(self):
        pass

    @property
    def getStatus(self):
        pass

    @setUsername.setter
    def setUsername(self,input):
        self.username = input

    @getUsername.getter
    def getUsername(self):
        return self.username

    @setPassword.setter
    def setPassword(self,input):
        self.password = input

    @getPassword.getter
    def getPassword(self):
        return self.password

    @getStatus.getter
    def getStatus(self):
        return self.Status

    def getInfo(self):
        return "Username = {} \nPassword = {} \nStatus = {}".format(self.getUsername, self.getPassword, self.getStatus)
    

    
class Pemilik(User) :
    def __init__(self, status):
        super().__init__(username, password, status)
        self.status = status
            
    def setStatus(self):
        self.status = "Admin"


class Kasir(User) :

    def __init__(self,nama,id_user,alamat,no_hp,status):
        super().__init__(username, password, status)
        self.nama = nama
        self.id_user = id_user
        self.alamat = alamat
        self.no_hp = no_hp
        self.status = status

    @property
    def setNama(self):
        pass

    @property
    def getNama(self):
        pass

    @property
    def setId(self):
        pass

    @property
    def getId(self):
        pass

    @property
    def setAlamat(self):
        pass

    @property
    def getAlamat(self):
        pass

    @property
    def setNoHp(self):
        pass

    @property
    def getNoHp(self):
        pass

    @setNama.setter
    def setNama(self,input):
        self.nama = input

    @getNama.getter
    def getNama(self):
        return self.nama

    @setId.setter
    def setId(self,input):
        self.id_user = input

    @getId.getter
    def getId(self):
        return self.id_user

    @setAlamat.setter
    def setAlamat(self,input):
        self.alamat = input

    @getAlamat.getter
    def getAlamat(self):
        return self.alamat

    @setNoHp.setter
    def setNoHp(self,input):
        self.no_hp = input

    @getNoHp.getter
    def getNoHp(self):
        return self.no_hp

    def setStatus(self):
        self.status = "Kasir"

class Barang :
    def __init__(self,kode_barang,nama_barang,jenis_barang,merk,jumlah,total):
        self.kodeBarang = kode_barang
        self.namaBarang = nama_barang
        self.jenisBarang = jenis_barang
        self.merk = merk
        self.jumlah = jumlah
        self.total = total

    @property
    def setKodeBarang(self):
        pass

    @setKodeBarang.setter
    def setKodeBarang(self,input):
        self.kodeBarang = input

    @property
    def getKodeBarang(self):
        pass

    @getKodeBarang.getter
    def getKodeBarang(self):
        return self.kodeBarang

    @property
    def setNamaBarang(self):
        pass

    @setNamaBarang.setter
    def setNamaBarang(self,input):
        self.namaBarang = input

    @property
    def getNamaBarang(self):
        pass

    @getNamaBarang.getter
    def getNamaBarang(self):
        return self.namaBarang

    @property
    def setJenisBarang(self):
        pass

    @setJenisBarang.setter
    def setJenisBarang(self,input):
        self.jenisBarang = input

    @property
    def getJenisBarang(self):
        pass

    @getJenisBarang.getter
    def getJenisBarang(self):
        return self.jenisBarang

    @property
    def setMerk(self):
        pass

    @setMerk.setter
    def setMerk(self,input):
        self.merk = input

    @property
    def getMerk(self):
        pass

    @getMerk.getter
    def getMerk(self):
        return self.merk

    @property
    def setJumlah(self):
        pass

    @setJumlah.setter
    def setJumlah(self,input):
        self.jumlah = input

    @property
    def getJumlah(self):
        pass

    @getJumlah.getter
    def getJumlah(self):
        return self.jumlah

    @property
    def setTotal(self):
        pass

    @setTotal.setter
    def setTotal(self,input):
        self.total = input

    @property
    def getTotal(self):
        pass

    @getTotal.getter
    def getTotal(self):
        return self.total

    def getInfo(self):
        return "Kode Barang = {} \nNama Barang = {} \nJenis Barang = {} \nJumlah Barang = {} \nTotal barang = {}".format(self.getKodebarang, self.getNamaBarang, self.getjenisBarang, self.getJumlah, self.getTotal)

class Televisi(Barang):
    def __init__(self,ukuran):
        super().__init__(kode_barang,nama_barang,jenis_barang,merk,jumlah,total)
        self.ukuran = ukuran

    @property
    def setUkuran(self):
        pass

    @setUkuran.setter
    def setUkuran(self,input):
        self.ukuran = input

    @property
    def getUkuran(self):
        pass

    @getUkuran.getter
    def getUkuran(self):
        return self.ukuran

    def setJenisBarang(self):
        self.jenisBarang = "Televisi"

class Kulkas(Barang):
    def __init__(self,model):
        super().__init__(kode_barang,nama_barang,jenis_barang,merk,jumlah,total)
        self.model = model

    @property
    def setModel(self):
        pass

    @setModel.setter
    def setModel(self,input):
        self.model = input

    @property
    def getModel(self):
        pass

    @getModel.getter
    def getModel(self):
        return self.model

    def setJenisBarang(self):
        self.jenisBarang = "Kulkas"
        
class MesinCuci(Barang):
    def __init__(self,model):
        super().__init__(kode_barang,nama_barang,jenis_barang,merk,jumlah,total)
        self.model = model

    @property
    def setModel(self):
        pass

    @setModel.setter
    def setModel(self,input):
        self.model = input

    @property
    def getModel(self):
        pass

    @getModel.getter
    def getModel(self):
        return self.model

    def setJenisBarang(self):
        self.jenisBarang = "Mesin Cuci"

class Transaksi:
    def __init__(self,id_transaksi,tanggal,nama_barang,jumlah_barang):
        self.idTransaksi = id_transaksi
        self.Tanggal = tanggal
        self.namaBarang = nama_barang
        self.jumlahBarang = jumlah_barang

    @property
    def setIdTransaksi(self):
        pass

    @setIdTransaksi.setter
    def setIdtransaksi(self,input):
        self.idTransaksi = input

    @property
    def getIdTransaksi(self):
        pass

    @getIdTransaksi.getter
    def getIdTransaksi(self):
        return self.idTransaksi

    @property
    def setTanggal(self):
        pass

    @setTanggal.setter
    def setTanggal(self):
        import datetime
        self.Tanggal = datetime.date.today()

    @property
    def getTanggal(self):
        pass

    @getTanggal.getter
    def getTanggal(self):
        return self.Tanggal

    @property
    def setNamaBarang(self):
        pass

    @setNamaBarang.setter
    def setNamaBarang(self,input):
        self.namaBarang = input

    @property
    def getNamaBarang(self):
        pass

    @getNamaBarang.getter
    def getNamaBarang(self):
        return self.namaBarang

    @property
    def setJumlahBarang(self):
        pass

    @property
    def getJumlahBarang(self):
        pass

    @setJumlahBarang.setter
    def setJumlahBarang(self,input):
        self.jumlahBarang = input

    @getJumlahBarang.getter
    def getJumlahBarang(self):
        return self.jumlahBarang

    def getInfo(self):
        return "Id Transaksi = {} \nTanggal = {} \nNama Barang = {} \nJumlah Barang = {}".format(self.getIdTransaksi, self.getTanggal, self.getNamaBarang, self.getJumlahBarang)
    


class Penjualan :
    def __init__(self,tanggal,nama_barang,kode_barang,jumlah_barang):
        self.tanggal = tanggal
        self.namaBarang = nama_barang
        self.kodeBarang = kode_barang
        self.jumlah = jumlah_barang


    @property
    def setTanggal(self):
        pass

    @property
    def getTanggal(self):
        pass

    @property
    def setNamaBarang(self):
        pass

    @property
    def getNamaBarang(self):
        pass

    @property
    def setKodeBarang(self):
        pass

    @property
    def getKodeBarang(self):
        pass

    @property
    def setJumlah(self):
        pass

    @property
    def getJumlah(self):
        pass

    @setTanggal.setter
    def setTanggal(self,input):
        import datetime
        self.tanggal = datetime.date.today()

    @getTanggal.getter
    def getTanggal(self):
        return self.tanggal

    @setNamaBarang.setter
    def setNamaBarang(self,input):
        self.namaBarang = input

    @getNamaBarang.getter
    def getNamaBarang(self):
        return self.namaBarang

    @setKodeBarang.setter
    def setKodeBarang(self,input):
        self.kodeBarang = input

    @getKodeBarang.getter
    def getKodeBarang(self):
        return self.kodeBarang

    @setJumlah.setter
    def setJumlah(self,input):
        self.jumlah = input

    @getJumlah.getter
    def getJumlah(self):
        return self.jumlah

    def getInfo(self):
        return "Tanggal = {} \nNama Barang = {} \nKode Barang = {} \nJumlah = {}".format(self.getTanggal, self.getNamaBarang, self.getKodeBarang, self.getJumlah)
