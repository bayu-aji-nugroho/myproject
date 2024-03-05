from .ui import Ui
from .pembelian import Pembelian
import os 
import time

class UImainmenu(Ui):
    def __init__(self, dataBarang: dict) -> None:
        super().__init__(dataBarang)
        self.penjual = Pembelian()
        self.login()
        
    def Login(self):
            print("masukkan nama anda")
            self.NamaPengguna = self._Input()
            print("masukkan umur anda")
            self.UmurPengguna = self._Input()
            print("masukkan nama toko")
            self.namaToko = self._Input()
            print("terima kasih telah login (mohon tunggu 2 detik)")
            self.objectLogic.setterUangtToko(1000000)
            time.sleep(2)
            self.mainMenu()
            
    def login(self):
        while True:
                os.system("cls")
                print("1.anda baru")
                print("2.anda sudah bermain sebelumnya")
                try:
                    cek = int(self._Input())
                    if(int(cek) == 1):
                        self.Login()
                        break
                    elif(int(cek) == 2):
                        print("masukkan password")
                        time.sleep(2)
                        self.mainMenu()
                        break
                    elif(int(cek) == 0):
                        break
                    elif(cek == 888):
                        self.objectLogic.setterUangtToko(10**10)
                        self.NamaPengguna = "developer"
                        self.UmurPengguna = "developer"
                        self.namaToko = "developer"
                        self.mainMenu()
                        break
                    elif(type(cek)==str()):
                        self._keyerror(text=f"yang anda masukkan {cek} bukan angka")
                    else:
                        self._keyerror(cek)
                        time.sleep(2)
                    os.system("cls")
                except ValueError:
                    self._keyerror(text="bukan angka")
                    tryagain = self._Input(text="coba lagi?(y/n): ")
                    match tryagain:
                        case "y":
                            continue
                        case "n":
                            break
        
        
    def pasar(self):
        while True:
            self._secondBar()
            for indext,data in enumerate(self.databarang):
                print(f"{indext}.barang: {data:{20}}|harga: Rp {self.databarang[data]:,}")
            print("0 untuk keluar")
            try:
                barang = input("masukkan nama barang untuk membeli : ")
                if barang == "0":
                    break
                jumlah = int(input("masukkan jumlah: "))
            except EOFError:
                barang = ""
                jumlah = 0
                self._close()
            except ValueError:
                self._keyerror(text="yang anda masukkan bukan angka")
                self._Input("klik enter untuk kembali ke pasar")
                
                
            
            try:
                self.objectLogic.pembelian(barang,self.databarang[barang],jumlah)
                break
            except KeyError:
                self._keyerror(text="barang tidak ada")
            self._Input("klik enter untuk kembali ke pasar")
            
    def mainMenu(self):
        while True:
            os.system("cls")
            self.bar()
            print("1.cek pembeli\n2.cek stok\n3.beli stok")
            try:
                cek = int(self._Input())
                if cek == 3:
                    self.pasar()
                elif cek == 2:
                    self.stok()
                elif cek == 0:
                    break
                elif cek == 1:
                    self.cekPembeli()
            except ValueError:
                pass
            except EOFError:
                self._close()
    def cekPembeli(self):
        self._secondBar()
        self.penjual.cekpelanggan()
        
           
            
    def stok(self):
        self._secondBar()
        self.objectLogic.stok()
           