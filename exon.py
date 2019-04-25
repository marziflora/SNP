import re
import time

t0 = time.time()

path = "C:/Users/HP/Desktop/Studia/MGR/GFF3/Bos_taurus.UMD3.1.94.chr.gff3"  #plik ze wszystkimi chromosomami
with open(path, "r") as f:
    for line in f:  #wczytuj po linijce
        if line[0].isdigit() or line[0] == 'X' or line[0:2] == 'MT':  #jeżeli 1 znak jest cyfrą (chromosom) / X / MT
            p = bool(re.search("exon", line))  #logiczna zmienna: Czy jest exon w linijce?
            if p == True:  #jeżeli znajdzie:
                r = open("Bos_taurus.UMD3.1.94.chr.gff3-exon.txt", "a") #Zapisz w nowym pliku
                l = [num for num in line.split('\t')]  #dzieli linijkę na wyrazy przedzielone tabulatorem
                string = " ".join(l[0:8])  #wybór pierwszych 8 słów
                string = string + "\n"
                r.write(string) #niech zapisuje tylko kolumny 1-8

t1 = time.time()
t=t1-t0
print("Czas wykonania:", t)  #16 minut


