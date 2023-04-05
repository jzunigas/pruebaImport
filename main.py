# imprimir 
print("Hola Mundo!! Soy jonathan zuñiga")
"""
variables
"""
texto = "Repaso de Python"
nombre = "Jonathan Zuñiga"
year = 2020

print(texto)

#concatenacion, siempre hacerlo con mismo tipo de datos
print(f"{texto} - {nombre} - {str(year)}")
#con str(year) convertimos el valor a un string. 
print(texto + " - " + nombre + " - " + str(year))


#Entrada
# sitioweb = input("¿Cual es tu pagina web?:")
# print("El sitio web es " + sitioweb)


#condiciones
# altura = int(input("¿Cual es tu altura?:"))
# if altura >= 180:
#     print("Eres una persona alta!!")
# else:
#     print("Eres bajito")


#funciones, se declara con def que es una funcion
def mostrarAltura():
    altura = int(input("¿Cual es tu altura?:"))
    if altura >= 180:
        print("Eres una persona alta!!")
    else:
        print("Eres bajito")
#llamar a la funcion
mostrarAltura()

#funciones ejemplo2
var_altura = int(input("¿Cual es tu altura?:"))
def mostrarAltura(altura):    
    if altura >= 180:
        print("Eres una persona alta!!")
    else:
        print("Eres bajito")
#llamar a la funcion
mostrarAltura(var_altura)


#funciones ejemplo3
var_altura = int(input("¿Cual es tu altura?:"))
def mostrarAltura(altura):    
    resultado = ""
    if altura >= 180:
        resultado = "Eres una persona alta!!"
    else:
        resultado = "Eres bajito"
    
    return resultado
#llamar a la funcion
print(mostrarAltura(var_altura))


#listas
personas = ["Jonathan", "Marcela", "Ambar"]
print(personas[0])

for persona in personas:
    print("- " + persona)
