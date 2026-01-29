def cargar_saldo(saldo):
    monto = float(input("Ingrese el monto a depositar: "))
    if monto > 0:
        nuevo_saldo = saldo + monto
        print(f"Carga exitosa. Nuevo saldo: ${nuevo_saldo}")
        return nuevo_saldo 

    else:
        print("Error: El monto debe ser mayor a cero.")
        return saldo
def retirar_pago(saldo_actual):
    monto = float(input("Ingrese el monto a retirar: "))
    if monto <= 0:
        print("Error: Monto inválido.")
    elif monto > saldo_actual:
        print("Error: Fondos insuficientes.")
    else:
        saldo_actual -= monto
        print(f"Pago realizado. Saldo restante: ${saldo_actual}")
    return saldo_actual
def menu():
    while True:
        print("\n--- BIENVENIDO A TU CAJERO AUTOMATICO---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. retirar dinero")
        print("4. salir")


def main():
    saldo = 1000 
    
    while True:
        print("\n--- BIENVENIDO A TU CAJERO AUTOMATICO---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. retirar dinero")
        print("4. salir")
        
        opcion = input("Seleccione una opción: ")


        if opcion == "1":
            saldo = print(f"Saldo actual: ${saldo}") 
        elif opcion == "2":
            saldo = cargar_saldo(saldo)
        elif opcion == "3":
            saldo = retirar_pago(saldo)
        elif opcion == "4" or "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")
            menu()

main()


# me falto hacer que solo saliera con 4 o 0 