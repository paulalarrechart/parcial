"""punto 1: Dado un vector con personaje de las películas de la saga de Star Wars resolver las
siguientes actividades:
a. Realizar un barrido recursivo del vector.
b. Realizar una función recursiva que permita determinar si ‘Yoda’ está en el
vector y en que posición."""



personajes = ['Yoda','Luke','Han Solo','Leila','Boba']

#punto B
def funcion (personaje, pos):
    if(pos< len(personaje)):
        if(personaje[pos] == 'Yoda'):
            return pos
        else:
            return funcion(personaje, pos+1)
    else:
        return -1

print(funcion(personaje, 0))
    


"""punto 2:Dada una cola con las notificaciones de las aplicaciones de red social de un Smartphone, de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el
mensaje, resolver las siguientes actividades:
c. escribir una función que elimine de la cola todas las notificaciones de
Facebook;
d. escribir una función que muestre todas las notificaciones de Twitter, cuyo
mensaje incluya la palabra ‘Python’, si perder datos en la cola;
e. utilizar una pila para almacenar temporalmente las notificaciones de
Instagram y mostrar el contenido de dicha pila."""

from pila import Pila
from cola import Cola 

class Aplicaciones (object):
    def __init__ (self, aplicacion,horario,mensaje):
        self.aplicacion= aplicacion
        self.horario= horario
        self.mensaje= mensaje

cola_aplicaciones= Cola()
cola_auxiliar= Cola()
pila_aplicaciones= Pila()
pila_auxiliar= Pila()

aplicaciones = Aplicaciones ('Facebook', 'Haga una publicacion', '10:50')
cola_aplicaciones.arribo(aplicaciones)
aplicaciones = Aplicaciones ('Twitter', 'Python', '09:30')
cola_aplicaciones.arribo(aplicaciones)
aplicaciones = Aplicaciones ('Instagram', 'Subir historia', '16:05')
cola_aplicaciones.arribo(aplicaciones)
aplicaciones = Aplicaciones ('TikTok', 'Vivo', '12:34')
cola_aplicaciones.arribo(aplicaciones)
aplicaciones = Aplicaciones ('YouTube', 'Video nuevo', '23:15')
cola_aplicaciones.arribo(aplicaciones)

#punto C
while(not cola_aplicaciones.cola_vacia):
    x= cola_aplicaciones.atencion()
    if (x.aplicacion == 'Facebook'):
        cola_auxiliar(x)

while (not cola_auxiliar.cola_vacia):
    cola_aplicaciones.arribo(cola_auxiliar.atencion())


cantidad = 0
while(cantidad < cola_aplicaciones.tamanio()):
    datos = cola_aplicaciones.mover_final()
    print(datos.aplicacion)    
    cantidad += 1 

print ('las notificaciones de Facebook fueron eliminadas de la cola')


#punto B
while(not cola_aplicaciones.cola_vacia()):
    x = cola_aplicaciones.atencion()  
    if (x.aplicacion =='Twitter'):
        mensaje = str(x.mensaje)
        buscado = 'Python'
        if (mensaje.find(buscado) == 0):
            print(x.aplicacion, mensaje)
    cola_auxiliar.arribo(x)

#punto C
while(not pila_aplicaciones.pila_vacia()):
    x= pila_aplicaciones.atencion()
    if (x.aplicacion == 'Instagram'):
        pila_auxiliar.arribo(mensaje) 


"""punto 3: Dada una lista con nombres de personajes de la saga de Avengers, resolver las
siguientes tareas:
a. Determinar si ‘Thor’ está en la lista, de ser así indicar en qué posición de la
misma;
b. Modificar el nombre de ‘Scalet Witch’ a ‘Scarlet Witch’;
c. Dada una lista auxiliar con los siguientes personajes (‘Black Widow’, ‘Hulk’,
‘Rocket Racoonn’, ‘Loki’), agregarlos a la lista principal en el caso de no estar
cargados. 
d. Realizar un barrido ascendente y descendente de la lista.
e. Mostrar la información del personaje en la posición 7.
f. Mostrar todos los personajes que comienzan con C o S.
g. Ahora los datos cambiaron y debe incluir (año de aparición y un campo
booleano que indica si es héroe True villano False), luego realizar un barrido
ordenado por nombre y otro por año de aparición. Deberá cargar toda la
información de nuevo."""

from lista import Lista

lista_nombres= ['Thor','Iron Man','Capitan America','Ultron','Scalet Witch']
lista_aux=['Black Widow', 'Hulk','Rocket Racoonn', 'Loki']

while(not lista_nombres.lista_vacia()):
    if ('Thor' in lista_nombres):
        print ('thor se encuentra en la lista')

























