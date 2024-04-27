datos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def cuartil(i):
    totaldedatos = len(i)
    proof = len(i)%2
    cuartiles = []
    if proof == 0:
        for x in range(1,4):
            percent = (x * totaldedatos)/4
            percent = round(percent)
            percent = int(i[percent - 1])
            cuartiles.append(percent)
        return cuartiles
    else:
        for x in range(1,4):
            percent = (x * (1 + totaldedatos))/4
            percent = round(percent)
            percent = int(i[percent- 1])
            cuartiles.append(percent)
        return cuartiles
        
pr = cuartil(datos)

print(pr)