datos_clientes = {'1':['Marcela', 'Reveco', 59, "12345hh"],
                  '2': ['Juan', 'Guerra', 64, "juanguerra54"],
                  '3': ['Luis', 'Toro', 20, "luis20"],
                  '4': ['Francisca', 'Jerez', 25, 'fjerez1992']}


#AGREGAR NUEVOS CLIENTES
#Pide por parametros cuatro datos y los retorna en una lista
def generador_lista(nombre, apellido, edad, contraseña):
    return([nombre, apellido, edad, contraseña])

#Genera automaticamente un id a un elemento del diccionario. 
# #Recoje la ultima key y va comparando las llaves de los diccionarios.
#Identifica la ultima y le suma una más.
def generador_id(diccionario):
    ultima_key = "1"
    for llave in diccionario.keys():
        ultima_key = llave
    nuevo_id = int(ultima_key)+1
    return str(nuevo_id)


#Desde el ID trae una lista con los datos del cliente. 
def agregar_clientes(diccionario, lista):
    id = generador_id(diccionario)
    diccionario[id] = lista

datos_gilberto = generador_lista("gilberto", "boada", 31, 'gboada21')
agregar_clientes(datos_clientes, datos_gilberto)
print(datos_clientes)

#ELIMINAR CLIENTES SEGÚN ID

def eliminar_clientes_id_pop(diccionario, id):
    diccionario.pop(id)
    
def eliminar_clientes_id_del(diccionario, id):
    del diccionario[id]

#eliminar_clientes_id_pop(datos_clientes, "1")
#eliminar_clientes_id_del(datos_clientes, "3")

#print(datos_clientes)


#MOSTRAR INFORMACION POR CLIENTE

def mostrar_info_cliente(diccionario, *id):
    for i in id:
        print(diccionario[i])

mostrar_info_cliente(datos_clientes, '1', '2', '3', '4')

