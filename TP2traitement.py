from pylab import pie,legend,show,plot,figure

Nuke=list()
Fioul= list()
Charbon= list()
Eolien=list()
Gaz=list()
Solaire=list()
Hydro=list()
Bio=list()
fic = open("RTE_2020.csv","r",encoding="UTF-8")
consoJdico=[]
totalJdico=[]


for i in range(35137) :
    a= fic.readline().strip().split(",")
    if i>0 :
    
        if a[10] !='':
            Nuke.append(int(a[10]))
            Fioul.append(int(a[7]))
            Charbon.append(int(a[8]))
            Eolien.append(int(a[11]))
            Gaz.append(int(a[9]))
            Solaire.append(int(a[12]))
            Hydro.append(int(a[13]))
            Bio.append(int(a[15]))
            totalJdico.append([a[2],int(a[10])+int(a[7])+int(a[8])+int(a[11])+int(a[13])+int(a[9])+int(a[12])+int(a[15])])
            consoJdico.append([a[2],int(a[4])])
         
fic.close

totnuke=0
for i in range(len(Nuke)):

    totnuke+=Nuke[i]
print(totnuke)

totgaz=0
for i in range(len(Gaz)):

    totgaz+=Gaz[i]
print(totgaz)

totfioul=0
for i in range(len(Fioul)):

    totfioul+=Fioul[i]
print(totfioul)

tothydro=0
for i in range(len(Hydro)):

    tothydro+=Hydro[i]
print(tothydro)

totbio=0
for i in range(len(Bio)):

    totbio+=Bio[i]
print(totbio)

totcharbon=0
for i in range(len(Charbon)):

    totcharbon+=Charbon[i]
print(totcharbon)

toteolien=0
for i in range(len(Eolien)):

    toteolien+=Eolien[i]
print(toteolien)

totsolaire=0
for i in range(len(Solaire)):

    totsolaire+=Solaire[i]
print(totsolaire)


Energies=["Nucléaire","Eolien","Gaz","Solaire","Charbon","Fioul","Hydraulique","Bioenergies"]
slices=[totnuke,toteolien,totgaz,totsolaire,totcharbon,totfioul,tothydro,totbio]

pie(slices,labels=Energies,startangle=90,shadow=True,explode=(0.1, 0.1, 0.1, 0.1,0.1,0.1,0.1,0.1),radius = 1.2, autopct = "%1.1f%%")
legend()
show()




Totalannée=totsolaire+totbio+totcharbon+toteolien+totfioul+totgaz+tothydro+totnuke
consoannée=0


consopct=list()

#for i in range(len(totalJdico)):
    #consopct.append(totalJdico[i]/consoJdico[i])
b=0
Ltjour=list()
Lcjour=list()
for i in range(len(totalJdico)):
    Ltjour.append([int(0)])
    
    if totalJdico[i] == totalJdico[i-1]:
        Ltjour[b]+=int(totalJdico[i][1])
        Lcjour[b]+=int(consoJdico[i][1])

    else:
        b+=1

print(Ltjour)
