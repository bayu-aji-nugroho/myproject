class Logic:
    _ownItem = {} 
    """barang:[harga barang,stok]"""
    __uangToko = 0
    def __init__(self,Data) -> None:
        self.Data = Data
    
    def setterOwnitem(self):
        pass
        
    def setterUangtToko(self,value):
        self.__uangToko = value
        
    def pembelian(self,namaBarang,harga,jumlah):
        for i in self.Data:
            if ((namaBarang == i) and (self.__uangToko >= (self.Data[i]*jumlah))):#mengecek apakahh barang ada atau tidak
                self.__uangToko -= harga*jumlah
                if (f"{namaBarang}" in self._ownItem ): #jika barang sudah ada
                    self._ownItem[namaBarang] = [harga,jumlah+self._ownItem[namaBarang][1]]
                else:
                    self._ownItem[namaBarang] = [harga,jumlah]
                print(f"barang: {namaBarang} harga total: Rp{harga*jumlah:,} jumlah: {jumlah} berhasil dibeli(:")
                
                
            elif((self.Data[i]*jumlah > self.__uangToko) and (namaBarang == i)):#jika uang kurang
                print(f"uang untuk membeli {namaBarang} {jumlah}x kurang Rp.{((self.Data[i]*jumlah) - self.__uangToko):,}")
        input("klik enter untuk lanjut")
                
    def stok(self):
        """untuk melihat stok tersedia dan mengedit harga"""
        if (len(self._ownItem) == 0):
            print("tidak ada barang apapun sekarang")
        elif (len(self._ownItem) != 0):
            for index,data in enumerate(self._ownItem):
                print(f"{index}. {data}| harga: Rp {self._ownItem[data][0]:,} stok: {self._ownItem[data][1]}")      
        input()
        
    def Terbeli(self,namaBarang,jumlah):
        print(float(self._ownItem[namaBarang][0])*jumlah)
        self.__uangToko += (float(self._ownItem[namaBarang][0])*jumlah)
        print(self.__uangToko)
        input()
                

    def uang(self):
        return f"{self.__uangToko:,}"
    
    
    
        
                
        
        
        
        
    