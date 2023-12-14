import csv
RTE_2020 =[]
with open ('RTE_2020.csv' , newline='') as f :
	l= csv.reader(f,delimiter=",")
	for i in l:
		if i != '' :
			RTE_2020.append(i)

#remplir la liste angleterre avec la somme des echange avec cette pays
#remplir la liste temps avec les dates des echanges
import numpy as np 
angleterre=[]
temps=[]
for i in range(1,len(RTE_2020)-1,100):
	angleterre.append(int(RTE_2020[i][18]) )
	temps.append(RTE_2020[i][2])

#le diagramme avec l'angleterre
from matplotlib import pyplot as plt 

plt.plot(temps , angleterre , color='b')
plt.title("les echanges avec l'angleterre en 2020")
plt.xlabel("jours")
plt.ylabel("ech_angleterre")
plt.show()


#remplir la liste espagne avec la somme des echange avec cette pays 
#remplir la liste temp avec les dates des echanges
import numpy as np 
espagne=[]
temp=[]
for i in range(1,len(RTE_2020)-1,100):
	espagne.append(int(RTE_2020[i][19]) )
	temp.append(RTE_2020[i][2])

#le diagramme avec l'espagne
from matplotlib import pyplot as plt 

plt.plot(temp , espagne , color='b')
plt.title("les echanges avec l'espagne en 2020")
plt.xlabel("jours")
plt.ylabel("ech_espagne")
plt.show()

#remplir la liste italie avec la somme des echange avec cette pays 
#remplir la liste temps avec les dates des echanges
import numpy as np 
italie=[]
temp1=[]
for i in range(1,len(RTE_2020)-1,100):
	italie.append(int(RTE_2020[i][20]) )
	temp1.append(RTE_2020[i][2])

#le diagramme avec l'italie
from matplotlib import pyplot as plt 

plt.plot(temp1 , italie , color='b')
plt.title("les echanges avec l'italie en 2020")
plt.xlabel("jours")
plt.ylabel("ech_italie")
plt.show()

#remplir la liste suisse avec la somme des echange avec cette pays 
#remplir la liste temps avec les dates des echanges
import numpy as np 
suisse=[]
temp2=[]
for i in range(1,len(RTE_2020)-1,100):
	suisse.append(int(RTE_2020[i][21]) )
	temp2.append(RTE_2020[i][2])

#le diagramme avec la suisse
from matplotlib import pyplot as plt 

plt.plot(temp2 , suisse , color='b')
plt.title("les echanges avec la suisse en 2020")
plt.xlabel("jours")
plt.ylabel("ech_suisse")
plt.show()

#remplir la liste Allemagne_Belgique avec la somme des echange avec cette pays 
#remplir la liste temps avec les dates des echanges
import numpy as np 
Allemagne_Belgique=[]
temp3=[]
for i in range(1,len(RTE_2020)-1,100):
	Allemagne_Belgique.append(int(RTE_2020[i][22]) )
	temp3.append(RTE_2020[i][2])

#le diagramme avec la suisse
from matplotlib import pyplot as plt 

plt.plot(temp3 , Allemagne_Belgique , color='b')
plt.title("les echanges avec l'Allemagne_Belgique en 2020")
plt.xlabel("jours")
plt.ylabel("ech_Allemagne_Belgique")
plt.show()

