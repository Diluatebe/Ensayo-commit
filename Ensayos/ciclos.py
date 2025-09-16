import math

Notas=[2,3.5,3,3,2,1,5,4,3,3.4,2.3,1.8,3.4]
# notas_ord=sorted(Notas)
# print(Notas)
# print(notas_ord)
# notas_gana=[]
# for g in notas_ord:
#     if g>=3:
#         notas_gana.append(g)
# print(notas_gana)
notas_buena=[g for g in Notas if g>=3 ]
print(notas_buena)

notas_redondeadas =[math.floor(g) for g in Notas]
print(notas_redondeadas)