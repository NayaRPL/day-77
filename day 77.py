print("algoritma pencarian bagi dua kasusu menggunsksn rekursif")
def binarysearch(alist,value):
    if len(alist) == 0:
        return False 
    else:
        middle= len(alist) // 2
        if alist [middle] == value :
            return True
        else:
            if value < alist[middle]:
                return binarysearch (alist[:middle],value)
            else:
                return  binarysearch (alist[middle+1:],value)
data=[100,200,300,400,500]
print(data)
print(binarysearch(data,600))
print(binarysearch(data,500))
#cara kerja algoritma pencarian bagi-dua adalah dengan membagi elemen-elemen list menjadi dua
# bagian secara berulang.jika nilai yang di cari lebih besara dari nilai elemen tengah (alist[middle]),maka proses pencarian 
#dilakukan pada bagian list sebelah kiri. jika lebih besar,maka pencarian dilakuksn pada bagian list sebelah kanan; dengan asusmsi
# bahwa elemen elemen list trururut secara menaik (ascending)