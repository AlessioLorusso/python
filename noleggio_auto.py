#1
import pprint
pp=pprint.PrettyPrinter(indent=4)
diz={"AA123BB":[("Giugno",9,1293),("Luglio",7,3231),("Agosto",7,4020),("Settembre",6,3928)],
     "AB345CD":[("Giugno",8,1391),("Luglio",6,1234),("Agosto",9,4932),("Settembre",8,2872)],
     "CD456FF":[("Giugno",7,2872),("Luglio",6,3273),("Agosto",4,3211),("Settembre",8,2827)]}
pp.pprint(diz)

#2
pp=pprint.PrettyPrinter(indent=4)
diz["ZZ999LA"]=[("Giugno",10,14000),("Luglio",10,14000),("Agosto",10,1400),("Settembre",10,1400)]
pp.pprint(diz)

#3
print(f"mese : {diz['AA123BB'][1][0]}")
print(f"noleggi : {diz['AA123BB'][1][1]}")
print(f"KM : {diz['AA123BB'][1][2]}")

#4
print(f"noleggi : {diz['AA123BB'][1][1]}")

#5
#print(f"somma km di luglio per la targa AA123BB : {diz['AA123BB'][1][0]+diz['AA123BB'][1][1]+diz['AA123BB'][1][2]}")
# for chiave in diz.keys():
#   print(chiave)
#   print(diz[chiave])
lista=diz["AB345CD"]
#print(lista)
somma=0
for tupla in lista:
  #print(tupla[1])
  somma+=tupla[1]
print("la somma di tutti i km in tutti i mesi per la targa AB345CD è: ",somma)

#6
#Stampa la somma di tutti i km in tutti i mesi per tutte le macchine
somm=0
for chiave in diz.keys():
  for i in range(len(diz[chiave])):
    somm+=diz[chiave][i][2]
print("la somma di tutti i km in tutti i mesi per tutte le macchine è ", somm)

#7
#Stampa il mese in cui sono stati fatti più km per la macchina targata CD456FF
max=0
mese=""
for i in range(len(diz["CD456FF"])):
  if diz["CD456FF"][i][2]>max:
    max=diz["CD456FF"][i][2]
    mese=diz["CD456FF"][i][0]
print(max,mese)
