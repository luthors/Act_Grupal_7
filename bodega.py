import random
import time

#DEFINE NUMERO ALEATORIO DE PRODUCTOS
nrandom_vasos = random.randint(300, 500)
nrandom_cucharas = random.randint(300, 500)
nrandom_cuchillos = random.randint(300, 500)
nrandom_tenedores = random.randint(300, 500)

#DEFINE DESCRIPCION ALEATORIA DE PRODUCTOS
descripciones = ["plastico", "metal", "carton"]
desc_vasos = random.choice(descripciones)
desc_cucharas = random.choice(descripciones)
desc_cuchillos = random.choice(descripciones)
desc_tenedores = random.choice(descripciones)

#CREA BODEGA INICIAL
bodega = {"vasos":[nrandom_vasos, desc_vasos],
          "cucharas":[nrandom_cucharas, desc_cucharas],
          "cuchillos":[nrandom_cuchillos, desc_cuchillos],
          "tenedores":[nrandom_tenedores, desc_tenedores]}

def sumar_unidades(diccionario, producto, unidades_agregar):
    unidades_iniciales = diccionario[str(producto)][0]
    unidades_finales = unidades_agregar + unidades_iniciales
    diccionario[producto][0] = unidades_finales
    return unidades_finales

#print("SUMA")
#print(f'Estas son las unidades iniciales de cuchillos: {bodega["cuchillos"][0]}')
#sumar_unidades(bodega, "cuchillos", 6)
#print(f'Estas son las unidades finales de cuchillos: {bodega["cuchillos"][0]}')

def restar_unidades(diccionario, producto, unidades_restar):
    unidades_iniciales = diccionario[str(producto)][0]
    unidades_finales = unidades_iniciales - unidades_restar
    if unidades_finales >= 0:
        diccionario[producto][0] = unidades_finales
    else:
        print("No hay stock suficiente")
    return unidades_finales

#print("RESTAR")
#print(f'Estas son las unidades iniciales de tenedores: {bodega["tenedores"][0]}')
restar_unidades(bodega, "tenedores", 99)
#print(f'Estas son las unidades finales de tenedores: {bodega["tenedores"][0]}')

#FUNCION AGREGAR NUEVOS PRODUCTOS
def agregar_productos_bodega(diccionario, nombre_producto, cantidad, descripcion):
    str(nombre_producto)
    if nombre_producto in diccionario:
        print("Este producto ya está en la bodega. Utilice otra función")
    else:
        diccionario[nombre_producto]= [cantidad, descripcion]

agregar_productos_bodega(bodega, 'mochila', 10, 'verde')
agregar_productos_bodega(bodega, 'mochila', 10, 'verde')
agregar_productos_bodega(bodega, 'bananos', 10, 'negros')
#print(bodega)

#FUNCION DE QUITAR PRODUCTOS DE UNA BODEGA VIRTUAL
def eliminar_producto(diccionario, producto):
    str(producto)
    diccionario.pop(producto)

#eliminar_producto(bodega, 'cuchillos')
#print(bodega)

def eliminar_productos(diccionario, *producto):
    for elemento in producto:
        diccionario.pop(elemento)

eliminar_productos(bodega, "cuchillos", "tenedores")
#print(bodega)

#MOSTRAR TODOS LOS PRODUCTOS DISPONIBLES Y STOCK.
#DESFASE 1 SEG.

def mostrar_productos(diccionario):
    for producto, datos in diccionario.items():
        print(f'Producto {producto} tiene un stock de {datos[0]}')
        time.sleep(1)

#mostrar_productos(bodega)

def verificador_stock(diccionario, cantidad_verificada):
    print(f'Necesitamos reponer el stock de estos productos, tiene menos de {cantidad_verificada} unidades')
    for producto, [cantidad, descripcion] in diccionario.items():
        if cantidad < cantidad_verificada:
            print(f'El producto {producto} tiene {cantidad} unidades')
            time.sleep(1)
        else:
            continue

verificador_stock(bodega, 400)