from parking import Parking, ParkingError


def main():
    parking = Parking()
    opcion = ""

    while opcion != "4":
        print("\n=== MENÚ PARKING ===")
        print("1. Entrada de vehículo")
        print("2. Salida de vehículo")
        print("3. Ver estado de plazas")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            mat = input("Introduce la matrícula: ")
            parking.entrada(mat)
        elif opcion == "2":
            mat = input("Introduce la matrícula: ")
            parking.salida(mat)
        elif opcion == "3":
            parking.mostrar_estado()
        elif opcion == "4":
            print(f"Recaudación final del día: {parking.recaudacion:.2f} €")
            print("Cerrando programa...")
        else:
            print("Opción no válida, vuelve a intentarlo.")


if __name__ == "__main__":
    main()
