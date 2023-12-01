#Pregunta 3 (5 puntos)

"""
Se requiere realizar un cambio en el software para que soporte un valor máximo de 200 soles a
transferir por día.
Qué cambiaría en el código (Clases / Métodos) - No implementación.
Nuevos casos de prueba a adicionar.
Cuánto riesgo hay de “romper” lo que ya funciona?
"""


"""
RESPUESTA:
--- Cambios en las Clases/Métodos:


Para que soporte un valor máximo de 200 soles a transferir por día, una opción es agregar un atributo 
que represente el limite diario de las transferencias y modificar el método pagar para que verifique
que el valor a transferir no exceda el límite diario.

Asimismo, se debe agregar un método para verificar si el límite diario ha sido excedido y otro para
reiniciar el límite diario.

--- Nuevos casos de prueba a adicionar.


1) Verificar que el límite diario se reinicie correctamente.
2) Verificar que se reciba un mensaje adecuado al intentar realizar una transferencia que exceda el límite diario.
3) Verificar que se realice correctamente una transferencia dentro del límite diario.
4) Verificar que el historial incluya correctamente las transferencias realizadas dentro del límite diario.
5) Que se reciba un mensaje de error al intentar realizar una transferencia que exceda el límite diario.

- Caso de prueba para transferencia dentro del límite diario:
Realizar una transferencia que esté dentro del límite diario y verificar que se realiza con éxito.

- Caso de prueba para historial con transferencias dentro del límite diario:
El historial debe incluir las transferencias realizadas dentro del límite diario.

--- ¿Cuánto riesgo hay de “romper” lo que ya funciona?

El riesgo suele ser relativamente bajo, si hacemos un buen uso de las pruebas unitarias y de integración.
Podemos realizar validaciones exhaustivas para asegurarnos de que la nueva funcionalidad no afecte negativamente
a la funcionalidad existente. También podemos optar por utilizar un entorno de desarrollo en ramas separadas.
"""




