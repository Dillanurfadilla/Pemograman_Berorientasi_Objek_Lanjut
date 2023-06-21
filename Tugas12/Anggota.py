import requests
import json
class Anggota:
    def __init__(self):
        self.__id=None
        self.__kode_anggota = None
        self.__nama = None
        self.__jk = None
        self.__prodi = None
        self.__Alamat = None
        self.__url = "http://localhost/perpus/anggota_api.php"
                    
    @property
    def id(self):
        return self.__id
    
    @property
    def kode_anggota(self):
        return self.__kode_anggota
        
    @kode_anggota.setter
    def kode_anggota(self, value):
        self.__kode_anggota = value
    
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
   
    @property
    def jk(self):
        return self.__jk
        
    @jk.setter
    def jk(self, value):
        self.__jk = value
    
    @property
    def prodi(self):
        return self.__prodi
        
    @prodi.setter
    def prodi(self, value):
        self.__prodi = value
    @property
    def Alamat(self):
        return self.__Alamat
        
    @Alamat.setter
    def Alamat(self, value):
        self.__Alamat = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_anggota(self, kode_anggota):
        url = self.__url+"?kode_anggota="+kode_anggota
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_anggota']
            self.__kode_anggota = item['kode_anggota']
            self.__nama = item['nama']
            self.__jk = item['jk']
            self.__prodi = item['prodi']
            self.__Alamat = item['Alamat']
        return data
    def simpan(self):
        payload = {
            "kode_anggota":self.__kode_anggota,
            "nama":self.__nama,
            "jk":self.__jk,
            "prodi":self.__prodi,
            "Alamat":self.__Alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_anggota(self, kode_anggota):
        url = self.__url+"?kode_anggota="+kode_anggota
        payload = {
            "kode_anggota":self.__kode_anggota,
            "nama":self.__nama,
            "jk":self.__jk,
            "prodi":self.__prodi,
            "Alamat":self.__Alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_anggota(self,kode_anggota):
        url = self.__url+"?kode_anggota="+kode_anggota
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text