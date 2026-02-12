# MAQUINA-AUTONOMA

INTRODUCCION

Este proyecto implementa un Autómata Finito Determinista (AFD) en Python capaz de leer cadenas binarias desde un archivo .txt y determinar si son aceptadas o rechazadas.
El autómata reconoce cadenas formadas por 0 y 1 cuya condición es: La cadena debe empezar por 0.

El programa utiliza una función de transición siguiendo la definición teórica:

A = (Q, Σ, f, q1, F)


TRANCISIONES USADAS

f(q1,0) = q2
f(q1,1) = q3
f(q2,0) = q2
f(q2,1) = q2
f(q3,0) = q3
f(q3,1) = q3

FUNCIONAMIENTO

1.Recibe como parámetro un archivo .txt.

2.Lee cada línea como una cadena binaria.

3.Simula el AFD aplicando la función de transición.

4.Imprime si la cadena es ACEPTADA o RECHAZADA.

EJECUCION

Ubícate en la carpeta del proyecto y ejecuta:

py AFD.py entrada.txt

RESULTADOS 
![Captura AFD](imagenes/Captura%20de%20pantalla%202026-02-11%20200717.png)
