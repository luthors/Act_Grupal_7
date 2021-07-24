import random

#distancia = float(input('De  cuantos kilometros es el envío?: '))

bodega_a = []
bodega_b = []

def envio_largo(distancia):
    if len(bodega_a) < 500:
        bodega_a.append(distancia)
        print(len(bodega_a))

    else:
        print("La bodega A está llena")
    
def envio_corto(distancia):
    if len(bodega_b) < 500:
        bodega_b.append(distancia)
        print("Bodega B ", len(bodega_b), distancia)

    else:
        print("La bodega B está llena")

def clasificador_envio(distancia):
    if distancia >= 1000:
        envio_largo(distancia)
        print('envio_largo ' + str(distancia))
    else:
        envio_corto(distancia)
        print('envio_corto '+ str(distancia))
        
for envio in range(1, 5000):
    clasificador_envio(random.randint(500, 2000))