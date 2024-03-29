# Dynamic Programming (Programación Dinámica.)

"La idea de la programación dinámica es evitar recalcular
subsoluciones parciales que son necesarias para alcanzar las solución
final, almacenandolas en memoria."

### Características:

- Compromiso  tiempo-espacio, se sacrifica espacio para 
ganar tiempo.
- La estructura de datos en las que se almacenan las subsoluciones
se llama *tabla de subproblemas resueltos.*
- La programación dinamica es una técnica ascendente, la mayor
dificultad está en elegir orden en el que resuelven los
subejemplares.

- Hay que fijar el orden en que se debe de rellenar 
la tabla. Al cumplar el subejemplar, aquéllos implicados
ya deben de estar almacenados.


# The Knapsack problem (El problema de la mochila.)

Dados  *n* objetos, cada uno con un valor *vi* y 
*pi* y una mochila con una capacidad *c*, se desea hallar la composición de la mochila
que maximiza el valor de la carga.

### Características:

### Elementos:

# The Coin Change problem (El problema del cambio de moneda.)

 Disponemos de *n* tipos de monedas de valor *vi* y deseamos devolver
 un cambio de *c* unidades monetarias empleando el mínimo número posible
 de monedas de cada tipo.
 
 ### Características:
 
 - Como simplificación supondremos  que disponemos una cantidad ilimitada
 de monedas de cada tipo.
 
 - La resolución de este problema puede contemplarse como un problema de decisión
 donde hay que decidir para cada tipo de moneda cúantas incluimos para
 devolver el cambio.
 
 - El principio de optimalidad se cumple para este problema.
 
 ### Elementos:

# Fuentes:

A. Salguero, F. Palomo, I. Medina.<br>
Universidad de Cádiz.

Aho, Alfred; Hopcroft, John & Ullman, Jeffrey.<br>
The Design and Analysis of Computer Algorithms.<br>
Addison-Wesley. 1974.

Brassard, Gilles & Bratley, Paul.<br>
Fundamentos de Algoritmia.<br>
Prentice-Hall. 1997.<br>

Cormen, Thomas H.; Leiserson, Charles E.; Rivest, Ronald L. &
Stein, Cliford.<br>
Introduction to Algorithms.<br>
MIT Press. 2001. 2a ed.<br>

Horowitz, Ellis & Sahni, Sartaj.<br>
Fundamentals of Computer Algorithms.<br>
Pitman. 1978.<br>