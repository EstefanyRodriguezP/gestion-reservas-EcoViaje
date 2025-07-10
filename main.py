# Mostrar la lista de excursiones disponibles con cupos limitados.
# Permitir a los usuarios reservar un cupo ingresando su nombre y el número de excursión deseada.
# Verificar si hay cupos disponibles antes de confirmar la reserva.
# Manejar condiciones como excursiones llenas o intentos inválidos de reserva.
# Utilizar ciclos para mostrar y actualizar la información en tiempo real.
# Implementar las instrucciones break y continue para controlar el flujo del programa.

excursiones = {
    1 : {
        'nombre' : 'Excursión 1',
        'cupos' : 5, 
        'usuarios': []},
    2 : {
        'nombre' : 'Excursión 2',
        'cupos' : 0, 
        'usuarios': []}}

def funcioncita():
    print('Bienvenido a EcoViaje')

    while True:
        print('\n1) Mostrar todas las excursiones')
        print('2) Mostrar solo excursiones con cupos disponibles')
        print('3) Reservar un cupo para una excursión')
        print('0) Salir')
        eleccion = int(input('Ingresa el número de tu opción: '))

        if eleccion == 0:
            print('Gracias por consultar con EcoViaje, te esperamos pronto...')
            break

        elif eleccion == 1:
            print('\n*** A continuación puedes ver la lista con todas las excursiones ***')
            for clave, datos in excursiones.items():
                print(f'{clave}.- {datos["nombre"]}: {datos["cupos"]} cupos disponibles.')

        elif eleccion == 2:
            print('\n*** A continuación se muestran solo las excursiones con cupos disponibles ***')
            for clave, datos in excursiones.items():
                if datos["cupos"] > 0:
                    print(f'{clave}.- {datos["nombre"]}: {datos["cupos"]} cupos disponibles.\n')
                elif datos["cupos"] == 0:
                    print(f'{clave}.- {datos["nombre"]}: esta excursión no tiene cupos disponibles.')
                else:
                    continue

        elif eleccion == 3:
            while True:
                nombre_usuario = input('Ingresa tu nombre para reservar el cupo: ').strip().upper()
                if nombre_usuario != "":
                    break
                else:
                    print("El nombre no puede estar vacío. Por favor, ingresa tu nombre.")
            excursion_elegida = int(input('Ingresa el número de tu excursión: '))
            if excursion_elegida in excursiones:
                datos = excursiones[excursion_elegida]
                print(f'Elegiste la excursión número {excursion_elegida}')
                if datos["cupos"] > 0:
                    datos['usuarios'].append(nombre_usuario)
                    print('Registro exitoso!')
                    datos['cupos'] -= 1
                else:
                    print('El registro no es posible, no hay cupos disponibles.')
            else:
                print('La opción no es válida, por favor intenta otra vez.')

        else:
            print('Error, por favor ingresa una opción válida.')

funcioncita()