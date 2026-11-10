from datetime import datetime

NUM_PLAZAS = 20
PRECIO_MINUTO = 0.05


class Plaza:
    def __init__(self, numero):
        self.numero = numero
        self.matricula = None
        self.hora_entrada = None


class Parking:
    def __init__(self):
        self.plazas = []
        for i in range(1, NUM_PLAZAS + 1):
            self.plazas.append(Plaza(i))
        self.recaudacion = 0.0

    def buscar_por_matricula(self, matricula):
        for plaza in self.plazas:
            if plaza.matricula == matricula:
                return plaza
        return None

    def entrada(self, matricula):
        matricula = matricula.strip().upper()
        if matricula == "":
            print("Error: La matrícula no puede estar vacía.")
            return

        if self.buscar_por_matricula(matricula) is not None:
            print("Error: Este vehículo ya está dentro del parking.")
            return

        for plaza in self.plazas:
            if plaza.matricula is None:
                plaza.matricula = matricula
                plaza.hora_entrada = datetime.now()
                print(f"Vehículo aparcado con éxito en la plaza {plaza.numero}")
                return

        print("Error: El parking está lleno.")

    def salida(self, matricula):
        matricula = matricula.strip().upper()
        plaza = self.buscar_por_matricula(matricula)

        if plaza is None:
            print("Error: No se encuentra ningún coche con esa matrícula.")
            return

        tiempo = datetime.now() - plaza.hora_entrada
        minutos = int(tiempo.total_seconds() / 60)
        if minutos == 0:
            minutos = 1

        importe = round(minutos * PRECIO_MINUTO, 2)
        self.recaudacion += importe

        plaza.matricula = None
        plaza.hora_entrada = None

        print(
            f"Salida registrada. Tiempo: {minutos} min. Total a pagar: {importe:.2f} €"  # importe:.2f es para mostrar solo 2 decimales, y no salga 1.33333333€
        )

    def mostrar_estado(self):
        libres = 0
        print("\n--- ESTADO DEL PARKING ---")
        for plaza in self.plazas:
            if plaza.matricula is None:
                estado = "LIBRE"
                libres += 1
            else:
                estado = f"OCUPADA ({plaza.matricula})"
            print(f"Plaza {plaza.numero}: {estado}")
        print(f"Total plazas libres: {libres}")
