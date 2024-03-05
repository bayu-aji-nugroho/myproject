import random
from.logic import Logic
from os import system

class Pembelian(Logic):
    status = False
    nama_orang = ["Budi", "Siti", "Lia", "Adi", "Putri", "Rina",
                  "Hadi", "Dewi", "Joko", "Ani", "Ahmad", "Rini",
                  "Eko", "Diana", "Agus", "Rita", "Hendra", "Sari",
                  "Iwan", "Rini","Andi", "Lina", "Rizki", "Dewa",
                  "Siska", "Rudi", "Maya", "Fajar", "Rini", "Joni",
                  "Fitri", "Rizal", "Dini", "Indra", "Siti", "Hendra",
                  "Anisa", "Agung", "Nina", "Arief","bayu"]

    def __init__(self) -> None:
        pass
    def blok(self,nama,barang,nilai):
        print("="*50)
        print(f"pelanggan {nama} \n membeli {barang} sebannyak {nilai}")
        print("="*50)
        data = [nama,barang,nilai]#nama,barang dan jumlah yang dibeli
        return data
    
    def __pelanggan(self):
        self.__barang = random.choice(list(self._ownItem.keys()))
        self.__orang = random.choice(self.nama_orang)
        self.__jumlah = random.randint(1,self._ownItem[self.__barang][1])
        data = self.blok(self.__orang,self.__barang,self.__jumlah)
        return data
            
            
    def cekpelanggan(self):
        dataSementara = []
        """list bersarang / nested list ([pelanggan ke i][[nama orang][barang][jumlah yang dibeli]])"""
        while True:
            print("r=refres| 0=keluar| y=melayani")
            jumlahpelanggan = random.randint(0,3)
            for i in range(jumlahpelanggan):
                dataSementara.append(self.__pelanggan())
            cek = input(": ")
            if cek=="r" or cek== "R":
                dataSementara.clear()
                system("cls")
            elif cek == "0":
                dataSementara.clear()
                break
            elif cek == "y" or cek == "Y":
                self.melayani(dataSementara)
                dataSementara.clear()#data dihapus setelah di pindah
    #ownitem adalah barang yang kita miliki
    def melayani(self,dataSementara):
        listHargaDanStok = []
        for i in range(len(dataSementara)):
            print(f"nama: {dataSementara[i][0]} barang: {dataSementara[i][1]} jumlah: {dataSementara[i][2]}")
        cek = input("ketik a untuk melayani semua: ")
        if cek == "a" or cek == "A":
            for i in range(len(dataSementara)):
                listHargaDanStok = self._ownItem[dataSementara[i][1]]#nama barang
                self._ownItem[dataSementara[i][1]] = [listHargaDanStok[0],listHargaDanStok[1]-dataSementara[i][2]]
                #self.terbeli(dataSementara[i][1],dataSementara[i][2])
                #self.Terbeli(dataSementara[i][1],dataSementara[i][2])
            
                
        
            
        