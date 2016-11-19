'''
En python:
 0º Triple comilla(' ' ') abre y cierra comentarios multi línea, hash(#) única línea.

 1º Los delimitadores se hacen con la tabulación y con los saltos de
    línea, no con llaves o con puntos y comas.

 2º En las clases se tiene que poner self(algo parecido a this en java), porque
    necesitan la instancia donde existen.
    Es complejo, aquí lo explica muy bien: http://stackoverflow.com/questions/2709821/what-is-the-purpose-of-self
    Si sigues con dudas, me preguntas.

 3º La herencia se pone entre parentesis, después del nombre de la clase.

 4º Los dobles puntos(:) son un recurso similar a las llaves (convina esto con lo dicho en el punto 1º).

 5º No existe new, se instancian con una asignación, siendo el "constructor" lo
    contenido en la función __init__.
 '''

clients = seatQueue()
barber = Barber()

TOTALCLIENTS = 3

for x in range(0, TOTALCLIENTS):
    clients
