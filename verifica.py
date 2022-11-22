#1
import pprint
pp=pprint.PrettyPrinter(indent=4)
diz={"Giuseppe Gullo":[("Corsa Campestre",(40,21,0),"Allievi"),("Corsa 100mt",(0,12,0),"Juniores mas"), ("Corsa 200mt",(0,29,19),"Juniores mas")],
     "Antonia Barbera":[("Corsa Campestre",(0,39,11),"Juniores fem"),("Corsa 100mt",(0,18,0),"Juniores mfem"), ("Corsa 200mt",(0,0,0),"Juniores fem")],
     "Nicola Esposito":[("Corsa Campestre",(0,43,22),"Allievi"),("Corsa 100mt",(0,14,0),"Juniores mas"), ("Corsa 200mt",(0,36,19),"Juniores mas")],}
pp.pprint(diz)
#2
import pprint
pp=pprint.PrettyPrinter(indent=4)
diz["Lorusso Alessio"]=[("Corsa Campestre",(2,20,0),"Allievi"),("Corsa 100mt",(0,20,0),"Juniores mas"), ("Corsa 200mt",(0,30,9),"Juniores mas")]
pp.pprint(diz)
#3
vAllievi=diz["Giuseppe Gullo"]
vAllievi.append(("Corsa ad ostacoli 400 mt",(0,40,34),"Allievi"))
diz["Giuseppe Gullo"]=vAllievi


vAllievi=diz["Antonia Barbera"]
vAllievi.append(("Corsa ad ostacoli 400 mt",(0,39,10),"Allievi"))
diz["Antonia Barbera"]=vAllievi


vAllievi=diz["Nicola Esposito"]
vAllievi.append(("Corsa ad ostacoli 400 mt",(0,40,10),"Allievi"))
diz["Nicola Esposito"]=vAllievi


vAllievi=diz["Lorusso Alessio"]
vAllievi.append(("Corsa ad ostacoli 400 mt",(0,40,26),"Allievi"))
diz["Lorusso Alessio"]=vAllievi
pp.pprint(diz)
#9:27 spinarelli
#4
print(f"disciplina: {diz['Giuseppe Gullo'][0][0]} ")
print(f"tempo: {diz['Giuseppe Gullo'][0][1]} ")
print(f"categoria: {diz['Giuseppe Gullo'][0][2]} ")
#9:33 Spinarelli
#5
print("il tempo di Nicola Esposito è: ")
print(f"minuti {diz['Nicola Esposito'][2][1][0]} ")
print(f"secondi {diz['Nicola Esposito'][2][1][1]} ")
print(f"centesimi {diz['Nicola Esposito'][2][1][2]} ")
#9:43 Spinarelli
#6
print(f"Antonia barbera nella corsa dei 100 mt ci ha messo  {diz['Antonia Barbera'][1][1][1]}, secondi e {diz['Antonia Barbera'][1][1][2]} centesimi")
#9:48 Spinarelli
#7
tMin=diz['Giuseppe Gullo'][1][1]
for i in diz.keys():
  if diz[i][1][1]=="Juniores mas":
    if tMin<diz[i][1][1]:
      tMin=diz[i][1][1]
      print(tMin)
print(f"il tempo minimo riportato nella corsa 100mt della categoria Juniores mas: {tMin}")
#10:45 Spinarelli
#8
tMax=diz['Giuseppe Gullo'][2][1][1]
for i in diz.keys():
  if diz[i][2][2]=="Juniores mas":
    if tMax>diz[i][2][1][1]:
      tMax=diz[i][2][1][1]
print(f"il tempo massimo riportato nella corsa 200mt della categoria Juniores mas: {tMax}")
