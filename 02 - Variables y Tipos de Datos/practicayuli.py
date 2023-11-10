# 1. Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

a = "b"
print(a)

#  2. Imprimir el tipo de dato de la constante 8.5

b = 8.5
print(type(b))

# 3. Imprimir el tipo de dato de la variable creada en el punto 1

print(type(a))

# 4. Crear una variable que contenga tu nombre

mi_nombre = "yulied"

# 5. Crear una variable que contenga un número complejo

nro_complejo = 4 + 5j

# 6. Mostrar el tipo de dato de la variable creada en el punto 5

print(type(nro_complejo))

# 7. Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

pi = 3.1416

# 8. Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

pagado = True
pago= "true"
                #una es un string y la otra en un boleano

# 9. Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

print("la variable 1 es tipo", type(pagado), "y la varoable 2 es de tipo" , type(pago))

# 10. Asignar a una variable, la suma de un número entero y otro decimal

suma_int_float = 4 + 5.3

# 11. Realizar una operación de suma de números complejos

suma_comp= (3 + 3j) + (2 + 4j)
print(suma_comp)

# 12. Realizar una operación de suma de un número real y otro complejo

suma_int_com = 4 + (3j *2)
print(suma_int_com)

# 13. Realizar una operación de multiplicación

multiplicacion = 2*8

# 14. Mostrar el resultado de elevar 2 a la octava potencia

print(2**8)

# 15. Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

division = 27 / 4
print(division)

# 16. De la división anterior solamente mostrar la parte entera

parte_entera = 27 // 4
print(parte_entera)

# 17. De la división de 27 entre 4 mostrar solamente el resto

muestra_elresto = 27 % 4
print(muestra_elresto)

# 18. Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

print((4*parte_entera)+muestra_elresto)

# 19. Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

d = "hola" + " mundo"
print(d)

# 20. Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

igualdad = "2" == 2
print(igualdad)

# 21. Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

igualdad1 = 2 == int("2")
print(igualdad1)

# 22. ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
 # por que los float en python se diferencian por punto y no coma

# 23. Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

variable = 3
variable -= 1
print(variable)

# 24. Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

operacion = 1 << 2
print(operacion)

# 25. Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

#2 + "2"

# 26. Realizar una operación válida entre valores de tipo entero y string
# operacion_n = 25 + int("25")


operacion_n = 3 * "3"
print(operacion_n)
#se puede por que lo que hace es repetir es str la cantidad de veces dicha













