from maincode.logic import Logic
from os import system
import time
        
class Ui():
    def __init__(self,dataBarang:dict) -> None:
        self.databarang = dataBarang
        self.objectLogic = Logic(Data=dataBarang)
        
    def _close(self):
        system("cls")
        print("---exit---")
        print("apakah anda yakin inggin keluar?(y)(semua data akan hilang)")
        cek = self._Input()
        if (cek == "y") or (cek == "Y"):
            print("program sedang dihentikan semua data hilang!")
            print("...")
            time.sleep(2)
            exit()
        else:
            system("cls")
        
    def bar(self):
        print("="*50)
        print(f"nama penjual: {self.NamaPengguna}| umur: {self.UmurPengguna}")
        print("="*50)
        print(f"nama toko :{self.namaToko}  | uang : Rp{self.objectLogic.uang()} ")
        print("="*50)
        
    def _secondBar(self):
        system("cls")
        print("="*50)
        print(f"uang: {self.objectLogic.uang()}")
        print("="*50)  
        
              
    def _Input(self,text=": "):
        print("="*20)
        a = input(text)
        print("="*20)
        return a
    
    def _keyerror(self,value = 0,text =""):
        """digunakan saat jika user salah memasukkan input"""
        if(text == ""):
            system("cls")
            print("="*20)
            print(f"oops!, {value} tidak ada dalam daftar silakan coba lagi ")
            print("="*20)
        elif(text != ""):
            system("cls")
            print("="*20)
            print(text)
            print("="*20)
        else:
            print("cek kode!")
        
        
   
                
               
    
        
            
    