import requests
import json
class Peminjaman:
    def __init__(self):
        self.__id=None
        self.__nomor_bukti = None
        self.__kode_anggota = None
        self.__tanggal_pinjam = None
        self.__tanggal_kembali = None
        self.__kode_buku = None
        self.__url = "http://localhost/perpus/peminjaman_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def nomor_bukti(self):
        return self.__nomor_bukti
        
    @nomor_bukti.setter
    def nomor_bukti(self, value):
        self.__nomor_bukti = value
    @property
    def kode_anggota(self):
        return self.__kode_anggota
        
    @kode_anggota.setter
    def kode_anggota(self, value):
        self.__kode_anggota = value
    @property
    def tanggal_pinjam(self):
        return self.__tanggal_pinjam
        
    @tanggal_pinjam.setter
    def tanggal_pinjam(self, value):
        self.__tanggal_pinjam = value
    @property
    def tanggal_kembali(self):
        return self.__tanggal_kembali
        
    @tanggal_kembali.setter
    def tanggal_kembali(self, value):
        self.__tanggal_kembali = value
    @property
    def kode_buku(self):
        return self.__kode_buku
        
    @kode_buku.setter
    def kode_buku(self, value):
        self.__kode_buku = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_nomor_bukti(self, nomor_bukti):
        url = self.__url+"?nomor_bukti="+nomor_bukti
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['kode_pinjam']
            self.__nomor_bukti = item['nomor_bukti']
            self.__kode_anggota = item['kode_anggota']
            self.__tanggal_pinjam = item['tanggal_pinjam']
            self.__tanggal_kembali = item['tanggal_kembali']
            self.__kode_buku = item['kode_buku']
        return data
    def simpan(self):
        payload = {
            "nomor_bukti":self.__nomor_bukti,
            "kode_anggota":self.__kode_anggota,
            "tanggal_pinjam":self.__tanggal_pinjam,
            "tanggal_kembali":self.__tanggal_kembali,
            "kode_buku":self.__kode_buku,
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_nomor_bukti(self, nomor_bukti):
        url = self.__url+"?nomor_bukti="+nomor_bukti
        payload = {
            "nomor_bukti":self.__nomor_bukti,
            "kode_anggota":self.__kode_anggota,
            "tanggal_pinjam":self.__tanggal_pinjam,
            "tanggal_kembali":self.__tanggal_kembali,
            "kode_buku":self.__kode_buku,
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_nomor_bukti(self,nomor_bukti):
        url = self.__url+"?nomor_bukti="+nomor_bukti
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text