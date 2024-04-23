#Siempre me gusta iniciar con un saludo y explicar brevemente la función del programa
print('\nHola! Verificaremos cuantas letras tiene una palabra')
#Iniciamos estableciendo una condición FALSE junto con el uso de un cuclo WHILE para que el programa se ejecute hasta que el usuario ingrese lo solicitado
cond = False
while cond == False: 
#Pedimos al usuario que ingrese una palabra entre 4 y 8 letras
   palabra = input('Ingresa una palabra de entre 4 y 8 letras: ')
#Ingresamos la palabra a una función que verifica el número de letras que tiene y la llamamos "longitud"
   longitud=len(palabra)
#Establecemos la condición para cuando la palabra tiene menos de 4 letras, en caso de cumplirse, mostramos en pantalla el número de letras de la palabra que ingresó el usuario
#Como la condición del ciclo while sigue siendo FALSE, nuestro programa se ejecuta desde el principio
   if longitud < 4: 
     print('\nHacen falta letras. Solo tiene', longitud,'letras')
#Establecemos la condición para cuando la palabra tiene más de 8 letras, en caso de cumplirse, mostramos en pantalla el número de letras de la palabra que ingresó el usuario
#Como la condición del ciclo while sigue siendo FALSE, nuestro programa se ejecuta desde el principio
   elif longitud > 8:
     print('\nSobran letras. Tiene', longitud,'letras')
#La última opción es que la palabra se encuentre dentro del rango, en este caso ejecutamos lo siguiente
   else:
     print('\nCorrecto. Tu palabra está dentro del rango') 
     cond=True
#Debido a que la condición cambia a TRUE, el ciclo WHILE termina y avanzamos con el siguiente bloque del programa


#Seguimos con el programa para conocer el cuadrante
print('\n\nPara continuar, ubicaremos en cual de los 4 cuadrantes del plano cartesiano se encuentra un punto de acuerdo a sus coordenadas en X,Y')
#Pedimos los datos para X y Y. Recordemos que los datos ingresados por el usuario son tomados como "str" por lo que, en este caso, debemos convertirlos 
#a enteros para que no nos muestre un error.
x = int(input('Por favor ingresa tu valor en X:'))
y = int(input('Ahora tu valor en Y:'))
#Teniendo los datos unicamente queda evaluarlos y regresar al usuario la respuesta correcta
if x>0 and y>0:
    print("\nTu punto se encuentra en el Cuadrante I")
if x<0 and y>0:
   print("\nTu punto se encuentra en el Cuadrante II")
if x<0 and y<0:
   print("\nTu punto se encuentra en el Cuadrante III")
if x>0 and y<0: 
   print("\nTu punto se encuentra en el Cuadrante IV")
elif x == 0 and y!=0:
   print("\nTu punto se encuentra sobre el eje Y")
elif x !=0 and y==0:
   print("\nTu punto se encuentra sobre el eje X")