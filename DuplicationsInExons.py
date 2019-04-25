import time
t0 = time.time()

path_dupplications = "  "  #Duplikacje
path_exon = "  " #Exon


with open(path_dupplications, "r") as d: #otwórz duplikacje
    for lined in d: #dla każdej linijki
        ld = [num for num in lined.split(' ')] #duplikacje
        with open(path_exon, "r") as e:  #otwórz exony
            for linee in e: #sprawdź każdą linijkę exonów
                le = [num for num in linee.split(' ')] #exony
                if ld[0] == le[0]: #jeżeli chromosom duplikacji i exonu się zgadza sprawdzaj dalej:

                    if int(le[3]) <= int(ld[1]) <= int(le[4]) and int(le[3]) <= int(ld[2]) <= int(le[4]):  #duplikacja rozpoczyna się po rozpoczęciu exonu i kończy przed zakończeniem exonu
                        r = open("DuplikacjeWExonach.txt", "a")
                        ld[3] = 'Wewnątrz exonu' #4 kolumna jako opis
                        ld[1]=str(ld[1])
                        ld[2]=str(ld[2])
                        string = " ".join(ld[0:4])
                        print("e:", le[3], le[4])
                        print("d:", ld[1], ld[2])
                        print(ld[0:4])
                        string = string + "\n"
                        r.write(string)

                    if int(le[3]) <= int(ld[1]) < int(le[4]) < int(ld[2]):    #rozpoczyna się po rozpoczęciu exonu ale kończy się po zakończeniu exonu
                        ld[2] = le[4]  #Podmiana końca duplikacji
                        r = open("DuplikacjeWExonach.txt", "a")
                        ld[3] = 'Obcięte z prawej strony'
                        print("e:", le[3], le[4])
                        print("d:", ld[1], ld[2])
                        print(ld[0:4])
                        ld[1]=str(ld[1])
                        ld[2]=str(ld[2])
                        string = " ".join(ld[0:4])
                        string = string + "\n"
                        r.write(string)

                    if int(ld[1]) < int(le[3]) < int(ld[2]) <= int(le[4]):  #duplikacja rozpoczyna się przed rozpoczęciem exonu i kończy się przed zakończeniem exonu
                        ld[1] = le[3]  #Podmiana początku duplikacji
                        r = open("DuplikacjeWExonach.txt", "a")
                        ld[3] = 'Obcięte z lewej strony'
                        ld[1]=str(ld[1])
                        ld[2]=str(ld[2])
                        string = " ".join(ld[0:4])
                        print("e:", le[3], le[4])
                        print("d:", ld[1], ld[2])
                        print(ld[0:4])
                        string = string + "\n"
                        r.write(string)

                    if int(le[3]) > int(ld[1]) and int(le[3]) > int(ld[2]) > int(le[4]): #duplikacja rozpoczyna się przed rozpoczęciem exonu i kończy po zakończeniu exonu
                        ld[2] = le[4]  #Podmiana końca duplikacji
                        ld[1] = le[3] #Podmiana początku duplikacji
                        r = open("DuplikacjeWExonach.txt", "a")
                        ld[3] = 'Obcięte z obu stron'
                        ld[1]=str(ld[1])
                        ld[2]=str(ld[2])
                        print("e:", le[3], le[4])
                        print("d:", ld[1], ld[2])
                        string = " ".join(ld[0:4])
                        print(ld[0:4])
                        string = string + "\n"
                        r.write(string)


t1 = time.time()
t=(t1-t0)/60
print("Czas wykonania:", t, "minut")  #9 minut
