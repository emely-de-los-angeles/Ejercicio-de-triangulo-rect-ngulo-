#Lista
Lista = []

#Encabezado del programa
print ("----------------------------------------------")
print("  Bienvenidos al programa de Emely  ")
print ("----------------------------------------------")
print("              Instrucciones:                   ")
print ("----------------------------------------------")
print("")
print("por favor introduzca tres numeros enteros")
print("")
print ("----------------------------------------------")
print("")

print ("por favor inttroduzca tres numeros enteros")



#solicitud del dato 1 al usuario
print("por favor ingrese el primer numero entero:")
A = input()
A = float(A)

#Agregar numero a la lista
Lista.append(A)

#solicitud del dato 2 al usuario
print("por favor ingrese el segundo numero entero:")
B = input()
B = float(B)


#Agregar numero a la lista
Lista.append(B)

#solicitud del dato 3 al usuario
print("por favor ingrese el tercer numero entero:")
C = input()
C = float(C)


#Agregar numero a la lista
Lista.append(C)

#ordenar lista de mayor a menor
Lista.sort()
print(Lista)

C = Lista[2]
B = Lista[1]
A = Lista[0]

#condicion

A2 = A**2
B2 = B**2
C2 = C**2 

D = (C2 == A2 + B2)

if D == True:
     print ("Felicidades, los datos que colocaste forman un triangulo rectangulo!!! :3 ")
else:
      print ("lo siento, los datos que colocaste no forman un triangulo rectangulo!!! :( ")
  



