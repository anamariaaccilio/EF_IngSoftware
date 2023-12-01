
#Pregunta 1 (10 puntos)

"""
En un repositorio Github, desarrollar el código fuente (se recomienda usar Python, pero no es
obligatorio) que implemente los endpoints:
/billetera/contactos?minumero=XXXX
/billetera/pagar?minumero=XXXX&numerodestino=YYYY&valor=ZZZZ
/billetera/historial?minumero=XXXX
Guardar la información en memoria, inicializar la aplicación con un conjunto de cuentas y
contactos, sin operaciones. Ejemplo:
List<Cuenta> BD = new List<Cuenta>();
BD.add( new Cuenta(“21345”, “Arnaldo”, 200, [“123”, “456”]));
BD.add( new Cuenta(“123”, “Luisa”, 400, [“456”]));
BD.add( new Cuenta(“456”, “Andrea”, 300, [“21345”]));
Ejemplo de resultados a los endpoint:
/billetera/contactos?minumero=21345
123: Luisa
456: Andrea
/billetera/pagar?minumero=21345&numerodestino=123&valor=100
Realizado en 11/07/2023.
/billetera/pagar?minumero=123&numerodestino=456&valor=50
Realizado en 11/07/2023.
/billetera/historial?minumero=123
Saldo de Luisa: 450
Operaciones de Luisa
Pago recibido de 100 de Christian
Pago realizado de 50 a Andrea

"""

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

class Cuenta:
    def __init__(self, numero, nombre, saldo, contactos):
        self.numero = numero
        self.nombre = nombre
        self.contactos = contactos
        self.saldo = saldo
        self.operaciones = []

    def agregar_operacion(self, operacion):
        self.operaciones.append(operacion)

    def obtener_contactos(self):
        return {contacto: cuenta.nombre for contacto, cuenta in BaseDatos.items() if contacto in self.contactos}

    def transferir(self, destino, valor):
        if self.saldo >= valor:
            if destino in self.contactos:
                self.saldo -= valor
                self.agregar_operacion(Operacion(destino, datetime.now(), valor))
                BaseDatos[destino].saldo += valor
                BaseDatos[destino].agregar_operacion(Operacion(self.numero, datetime.now(), valor))
                return f"Realizado en {datetime.now()}"
            else:
                return "El número de destino no es un contacto. (No se puede realizar la operación)"
        else:
            return "No tiene saldo suficiente, vuelva a intentar"

    def obtener_historial(self):
        return {
            "saldo": self.saldo,
            "operaciones": [str(operacion) for operacion in self.operaciones]
        }

class Operacion:
    def __init__(self, numerodestino, fecha, valor):
        self.numero_destino = numerodestino
        self.fecha = fecha
        self.valor = valor

    def __str__(self):
        return f"Numero destino: {self.numero_destino}, fecha: {self.fecha}, valor: {self.valor}"

BaseDatos = {
    "21345": Cuenta("21345", "Arnaldo", 200, ["123", "456"]),
    "123": Cuenta("123", "Luisa", 400, ["456"]),
    "456": Cuenta("456", "Andrea", 300, ["21345"]),
}

# Endpoint
# Billetera/contactos?minumero=XXXX
@app.route('/billetera/contactos', methods=['GET'])
def contactos():
    numero = request.args.get('minumero')
    cuenta = BaseDatos.get(numero)
    if cuenta:
        return jsonify(cuenta.obtener_contactos())
    else:
        return jsonify({"Error": "No se encontro el numero"}), 404

    #EJEMPLO: 
    # ENDPONIT: http://127.0.0.1:5000/billetera/contactos?minumero=21345
    # RESULT: {"123": "Luisa","456": "Andrea"}



# Billetera/pagar?minumero=XXXX&numerodestino=YYYY&valor=ZZZZ
@app.route('/billetera/pagar', methods=['GET'])
def pagar():
    numero = request.args.get('minumero')
    numerodestino = request.args.get('numerodestino')
    valor = int(request.args.get('valor'))

    cuenta =BaseDatos.get(numero)
    if cuenta:
        resultado = cuenta.transferir(numerodestino, valor)
        return jsonify({"Mensaje": resultado})
    else:
        return jsonify({"Error": "No se encontro el numero"}), 404
    
    #EJEMPLO: 
    # ENDPONIT: http://127.0.0.1:5000/billetera/pagar?minumero=21345&numerodestino=123&valor=100
    # RESULT: {"Mensaje": "Realizado en 2023-11-30 19:58:31.509299"}
    # ENDPONIT: http://127.0.0.1:5000/billetera/pagar?minumero=123&numerodestino=456&valor=50
    # RESULT: {"Mensaje": "Realizado en 2023-11-30 19:59:26.689523"}


# Billetera/historial?minumero=XXXX

@app.route('/billetera/historial', methods=['GET'])
def historial():
    numero = request.args.get('minumero')
    cuenta = BaseDatos.get(numero)
    if cuenta:
        resultado = cuenta.obtener_historial()
        # Formato de salida deseado
        output = (
            f"Saldo de {cuenta.nombre}: {resultado['saldo']} "
            f"Operaciones de {cuenta.nombre} "
            f"{' '.join(resultado['operaciones'])}"
        )
        return output
    else:
        return jsonify({"Error": "No se encontró el numero"}), 404

        
    #EJEMPLO: 
    # ENDPONIT: http://127.0.0.1:5000/billetera/historial?minumero=123
    # RESULT: Saldo de Luisa: 450, Operaciones de Luisa, Pago recibido de 100 de Christian, Pago realizado de 50 a Andrea

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
#Ana Maria Acilio Villanueva 
