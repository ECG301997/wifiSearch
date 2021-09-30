import os
import time
import math
id = int(52208)
contraseña = "80225"
captcha1 = 208
captcha2 = (2*5)-2-8

opc1 = "Cambiar contraseña"
opc2 = "Ingresar coordenadas actuales"
opc3 = "Ubicar zona wifi más cercana"
opc4 = "Guardar archivo con ubicación"
opc5 = "Actualizar registros de zonas wifi desde archivo"
opc6 = "Elegir opción de menú favorita"
opc7 = "Cerrar sesión"

menu = [opc1, opc2, opc3, opc4, opc5, opc6, opc7]
contadorerrores = 0

velocidad_a_pie=  0.483 # M/S
velocidad_bus = 3.33 # M/S



def ErrorConMensaje(mensaje):
    os.system("cls")
    print(mensaje)
    time.sleep(2)


matriz2 = []
matriz1 = [[None, None],
           [None, None],
           [None, None]]
ubicacion_actual = []


def digitaCoordenadas(matriz1):
    matriz2 = list(matriz1)
    for x in range(0, 3):
        matriz2.append([])
        latitud = input("ingrese su latitud actual: ")
        while latitud == "" or latitud == " ":
            latitud = input(
                "la latitud no puede estar vacia, por favor ingrese su latitud actual: ")
        latitud = round(float(latitud), 3)
        if latitud <= -3.002 and latitud >= -4.227:
            longitud = input("ingrese su longitud actual: ")
            while longitud == "" or longitud == " ":
                longitud = input(
                    "la longitud no puede estar vacia, por favor ingrese su longitud actual: ")
            longitud = round(float(longitud), 3)

            if longitud <= -69.714 and longitud >= -70.365:
                matriz2[x].insert(0, latitud)
                matriz2[x].insert(1, longitud)
            else:
                print("Error coordenada")
                exit()
        else:
            print("Error coordenada")
            exit()
        for x in range(len(matriz2)):
            print(f"COORDENADA [LATITUD,LONGITUD] {x+1} - {matriz2[x]}")
    return matriz2


def Ordenarlatitudes(matriz1):
    print(
        f"La coordenada que está mas al sur es: {min(matriz1, key=lambda posicion: posicion[0])}")


def OrdenarLongitudes(matriz1):
    print(
        f"La coordenada que está mas al oriente es: {max(matriz1, key=lambda posicion: posicion[1])}")


def PromedioCoordenadas(matriz1):
    totalLatitudes = (matriz1[0][0]+matriz1[1][0]+matriz1[2][0])
    totalLongitudes = (matriz1[0][1]+matriz1[1][1]+matriz1[2][1])
    promedioLatitudes = totalLatitudes/3
    promedioLongitudes = totalLongitudes/3
    promedioPuntos = (totalLatitudes + totalLongitudes)/6
    print(f"El promedio de las latitudes es {promedioLatitudes}")
    print(f"El promedio de las longitudes es {promedioLongitudes}")
    print(f"El promedio de todos los puntos es {promedioPuntos}")


def ImprimirCoordenadas(matriz1):

    matriz2 = list(matriz1)
    print("Las coordenadas guardadas actualmente son: ")
    for x in range(0, len(matriz2)):
        print(
            f"{x+1}. Coordenada Latitud:'{matriz2[x][0]}' Longitud: '{matriz2[x][1]}'")
    Ordenarlatitudes(matriz2)
    OrdenarLongitudes(matriz2)
    PromedioCoordenadas(matriz2)
    choice = int(
        input("Por favor ingrese la coordenada que desea modificar: "))
    if choice != 1 and choice != 2 and choice != 3:
        ErrorConMensaje("Error actualización")
        exit()
    else:
        ActualizarCoordenadas(choice, matriz1)


def ActualizarCoordenadas(choice, matriz1):
    matriz2 = list(matriz1)
    choice = choice-1
    latitud = input("Ingrese la latitud: ")
    while latitud == "" or latitud == " ":
        latitud = input(
            "La latitud no puede estar en blanco, por favor ingrésela de nuevo:")
    latitud = float(latitud)
    if latitud <= -3.002 and latitud >= -4.227:
        longitud = input("Ingrese la longitud: ")
        while longitud == "" or longitud == " ":
            longitud = input(
                "La longitud no puede estar en blanco, por favor ingrésela de nuevo:")
        longitud = float(longitud)
        if longitud <= -69.714 and longitud >= -70.365:
            matriz2[choice][0] = latitud
            matriz2[choice][1] = longitud
        else:
            ErrorConMensaje("Error actualización")
            matriz2 = [matriz1]
            return matriz2
    else:
        ErrorConMensaje("Error actualización")
        matriz2 = [matriz1]
        return matriz2

    return matriz2


def definirzonawifi():
    zonaWifi=[[ -3.777,-70.302 ,91 ], [-4.134,-69.983,233],[-4.006,-70.132,149],[-3.846,-70.222,211]]
    validaWifi = 0
    for i in range(4):
        for j in range(2):
            if zonaWifi[i][j] <= -3.002 or zonaWifi[i][j] >= -4.227:
                print("La latitud de la coordenada", i+1,
                    "No esta dentro de los limites estipulados")
                validaWifi = 1
            else:
                if zonaWifi[i][j] <= -69.714 or zonaWifi[i][j] >= -70.365:
                    print("La longitud de la coordenada", i+1,
                          "No esta dentro de los limites estipulados")
                    validaWifi = 1
    if validaWifi == 0:
        print("Las coordenadas con los limites estipulados")
    return(zonaWifi)


def mostrar_coordenadas(matriz):
    for x in range(len(matriz)):
        print(
            f"{x+1}. Coordenada Latitud:'{matriz[x][0]}' Longitud: '{matriz[x][1]}'")


def distancia_zonas(zonas, punto):
    latitudF = math.radians(punto[0])
    longitudF = math.radians(punto[1])
    R = 6372.795477598

    for i in range(len(zonas)):
        latitudS = math.radians(zonas[i][0])
        longitudS = math.radians(zonas[i][1])

        delta_long = longitudS - longitudF

        distancia = (math.acos(math.sin(latitudF)* math.sin(latitudS) + math.cos(latitudF) * math.cos(latitudS) * math.cos(delta_long))) * R
        distancia *=1000
        distancia = round(distancia,3)
        zonas[i].append(distancia)
    
    for i in range(len(zonas)-1):
        for j in range(i+1,len(zonas)):
            if zonas[i][3] > zonas[j][3]:
                distancia_temp = zonas[i]
                zonas[i] = zonas[j]
                zonas[j] = distancia_temp
    return(zonas[:2])

def ordenar_vector(vector):
    for i in range(len(vector) - 1):
        for j in range(i+1, len(vector)):
            usuarios_promedio = vector[i]
            vector[i] = vector[j]
            vector[j] = usuarios_promedio
    return(vector)

print("Este fue mi primer programa y vamos por más, Bienvenido al sistema de ubicacion para zonas publicas WIFI\n\n")

if int(input("ingrese su usuario:\n")) == id:

    if input("ingrese su contraseña:\n") == contraseña:

        if int(input(f"realice la siguiente suma: {captcha1} +  {captcha2}\n")) == captcha1 + captcha2:

            print("Sesion iniciada")
            os.system("cls")

            while contadorerrores < 3:
                for x in range(len(menu)):
                    print(f"{x+1} - {menu[x]}")
                opcionelegida = int(input("por Favor seleccione una opcion: "))
                os.system("cls")
                print(f"Usted ha elegido la opción {opcionelegida}")
                time.sleep(2)
                if opcionelegida > 0 and opcionelegida < 8:
                    opcionelegida = menu[opcionelegida-1]
                    if opcionelegida == opc1:
                        print(opc1)
                        os.system("cls")
                        contra = input("Ingrese su contraseña actual: ")
                        os.system("cls")
                        if contra == contraseña:
                            new_pass = input("ingrese su nueva contraseña: ")
                            if new_pass == contraseña:
                                print(
                                    "La contraseña nueva no puede ser igual a la actual")
                                print("Error")
                                pass
                            else:
                                new_pass_confirm = input(
                                    "Repita su nueva contraseña: ")
                                os.system("cls")
                                if new_pass == new_pass_confirm:
                                    print("Contraseña actualizada con exito")
                                    time.sleep(1)
                                    os.system("cls")
                                    contraseña = new_pass
                                    pass
                                else:
                                    print("Las contraseñas no coinciden")
                                    print("Error")
                                    exit()
                        else:
                            print("Error")
                            exit()
                        time.sleep(2)
                        os.system("cls")
                    elif opcionelegida == opc2:
                        print(opc2)
                        if matriz2 == []:
                            matriz2 = digitaCoordenadas(matriz2)
                        else:
                            ImprimirCoordenadas(matriz2)
                    elif opcionelegida == opc3:
                        print(opc3)
                        zonasWifi = definirzonawifi()
                        os.system("cls")
                        if len(matriz2) == 0:
                            print('"Error sin registro de coordenadas"')
                            time.sleep(2)
                            exit()
                        mostrar_coordenadas(matriz2)
                        try:
                            submenu2 = int(input("Por favor elija su ubicación actual(1,2 o 3) para calcular la distancia a los puntos de conexión "))
                            if submenu2 >= 1 and submenu2 <= 3:
                                cordistancia = distancia_zonas(zonasWifi,matriz2[submenu2 -1])
                                ubicacion_actual = matriz2[submenu2 -1].copy()
                                cordistancia = ordenar_vector(cordistancia)
                                print("Zonas wifi cercanas con menos usuarios")
                                for i in range(len(cordistancia)):
                                    print("La zona wifi", i +1,"ubicada en [",cordistancia[i][:2], "]a", cordistancia[i][3],"metros, tiene en promedio", cordistancia[i][2],"usuarios")
                                try:
                                    guia ="para llegar a la zona wifi dirigirse hacia"
                                    indicaciones = int(input("elija a que zona wifi desea dirigirse: "))
                                    if indicaciones >= 1 and indicaciones <= 2:
                                        if matriz2[submenu2 -1][1] < cordistancia[indicaciones-1][1]:
                                            guia = guia , "primero al oriente "
                                        elif matriz2[submenu2 -1][1] > cordistancia[indicaciones-1][1]:
                                            guia = guia, "occidente"
                                        if matriz2[submenu2-1][0] < cordistancia[indicaciones-1][0]:
                                            guia = guia, "norte"
                                        elif matriz2[submenu2-1][0] > cordistancia[indicaciones-1][0]:
                                            guia = guia, "sur"
                                        tiempo_a_pie = cordistancia[indicaciones-1][3] / velocidad_a_pie
                                        tiempoBicicleta = cordistancia[indicaciones-1][3] / velocidad_bus
                                        tiempo_a_pie = round((tiempo_a_pie/60),2)
                                        tiempoBicicleta = round((tiempoBicicleta/60),2)
                                        print(guia)
                                        print(f"El tiempo estimado en bus es {tiempo_a_pie} minutos")
                                        print(f"El tiempo estimado en bicicleta es {tiempoBicicleta} minutos")
                                        time.sleep(2)
                                        while True:
                                            salirMenu = input("presione 0 para salir ")
                                            if salirMenu ==  "0":
                                                print("Hasta pronto")
                                                break
                                    else:
                                        print("Error zona wifi")
                                        time.sleep(2)
                                        exit()
                                except ValueError:
                                    print("Error zona wifi")
                            else:
                                print("Error ubicación")
                                time.sleep(2)
                                exit()
                        except ValueError:
                            print("Error ubicación")
                            time.sleep(2)
                            exit()
                    elif opcionelegida == opc4:
                        print(opc4)
                        if matriz2 == []:
                            print("Error de alistamiento")
                            time.sleep(2)
                            exit()
                        if ubicacion_actual == []:
                            print("Error de alistamiento")
                            time.sleep(2)
                            exit()
                        wifi_cercanas ={"actual": ubicacion_actual, "zona Wifi":[cordistancia[0][0:3]],"recorrido":[cordistancia[0][3],"a pie",tiempo_a_pie]}
                        print(wifi_cercanas)
                        while True:
                            opcion_menu = input ("¿Esta de acuerdo con la información a exportar? presione 1 para confirmar, 0 para regresar al menú principal")
                            if opcion_menu == "1":
                                try:
                                    archivo = open(r"C:\Users\Lenovo\Desktop\DESARROLLO_DE_ SOFTWARE\UPB\CICLO_1\FUNDAMENTOS_DE_PROGRAMACION\RETOS\RETO_5\wificercano.txt","w")
                                    archivo.write(str(wifi_cercanas))
                                    print("Exportando archivo")
                                    time.sleep(2)
                                    exit()
                                except IOError:
                                    print("Exportando archivo")
                                    time.sleep(2)
                                    exit()
                            elif opcion_menu == "0":
                                break
                    elif opcionelegida == opc5:
                        print(opc5)
                        try:
                            archivo = open(r"C:\Users\Lenovo\Desktop\DESARROLLO_DE_ SOFTWARE\UPB\CICLO_1\FUNDAMENTOS_DE_PROGRAMACION\RETOS\RETO_5\actualizarZonas.txt")
                            indice = 0
                            for i in archivo.readlines():
                                zonasWifi[indice] = i.strip().split(',')
                                zonasWifi[indice][0] = float(zonasWifi[indice][0])
                                zonasWifi[indice][1] = float(zonasWifi[indice][1])
                                zonasWifi[indice][2] = int(zonasWifi[indice][2])
                                indice +=1
                            print("Estas son las zonas wifi actualizadas")
                            print(zonasWifi)

                            while True:
                                opcionMenu = input("Datos de coordenadas para zonas Wifi actualizados, presione 0 para regresar al menú principal")
                                if opcionMenu == 0:
                                    break
                        except IOError:
                            while True:
                                opcionMenu =input("Datos de coordenadas para zonas Wifi actualizados, presione 0 para regresar al menú principal")
                                if opcionMenu == "0":
                                    break
                    elif opcionelegida == opc6:
                        print(opc6)
                        nuevofavorito = int(
                            input("Ingrese el número de la opción que desea mover: "))
                        if nuevofavorito == 1 or nuevofavorito == 2 or nuevofavorito == 3 or nuevofavorito == 4 or nuevofavorito == 5:
                            print("Usted ha elegido la opción", nuevofavorito)

                            print(
                                "por favor resuelva las siguientes preguntas para continuar")
                            if int(input("Si multiplicas por mi no da nada, pero si divides por mi lo da todo ¿Quien soy?\n")) == 0:
                                if int(input("Si me pones de lado soy todo, si me partes por la mitad no soy nada ¿quien soy?\n")) == 8:
                                    reordenar = menu[nuevofavorito-1]
                                    menu.remove(reordenar)
                                    menu.insert(0, reordenar)
                                else:
                                    print("Error comprobación 2.")
                            else:
                                print("Error comprobación 1.")
                        else:
                            print("Error")
                            exit()
                    elif opcionelegida == opc7:

                        print("Sesión Cerrada")
                        print("Hasta pronto")
                        exit()
                else:
                    contadorerrores += 1
                    if contadorerrores == 3:
                        print("Error")
                        exit()
                    continue
        else:
            print("Error")
            exit()
    else:
        print("Error")
        exit()
else:
    print("Error")
    exit()
