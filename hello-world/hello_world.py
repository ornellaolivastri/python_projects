print ("Hello, world!")

# asi se escriben los comentarios de una linea

"""
esto es un comentario 
de multiples lineas
"""
"""
# variables

texto = "Esto es un texto guardado en la variable texto"
nombre = "mi nombre es ornella"
edad = 23
anio = 2021



print(texto)
print(f"{nombre} -y mi edad- {edad}") #edad puede traer problemas 
#                             porque print a veces no funciona bien con numeros, 
#                             entonces para parsear el tipo se escribiría
#                             { str(edad) }
print(nombre + " y mi edad es " + str(edad)) #para poder hacer esto, lo que concateno 
#                                        debe ser del mismo tipo de dato


# Ingresar datos por teclado -------------------------------

sitioweb = input("Cual es tu pagina web?: ")
print(f"{sitioweb}, oki gracias")


# Condiciones ---------------------------------------------

"""
"""
altura = int ( input("Cual es tu altura?: ") )

if altura >= 180:
    print("Eres una persona alta!!")
else:
    print("Eres una persona baja!!")
"""

"""
# Funciones -----------------------------------------------

variable_altura = int ( input("Cual es tu altura?: ") )

def mostrarAltura(altura):
    resultado = ""
    if altura >= 180:
        resultado = "Eres una persona alta!!"
    else:
        resultado = "Eres una persona baja!!"

    #es recomendable que todas las funciones tengan un return
    return resultado

print (mostrarAltura(variable_altura))

"""

# Listas --------------------------------------------------------------------------------

personas = ["Victor", "Paco", "Pepe"]
print(personas)
print("la persona de la posicion 1 es: " + personas[1])

#este bucle for recorre la lista personas creando una variable persona por cada una 

for persona in personas:
    print("usuario: " + persona)