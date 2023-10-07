#Escribir una función que reciba como parámetros un número de día, un número de mes y un número de año y devuelva la cantidad de días que faltan hasta fin de mes. Luego desarrollar tres programas para:
#· Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir la cantidad de días que faltan hasta fin de año.
#· Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir la cantidad de días transcurridos en ese año hasta esa fecha.
#· Ingresar dos fechas formadas por tres enteros (día, mes y año) e imprimir cuánto tiempo transcurrió entre ambas, expresando el resultado en años, meses y días.
#Los tres programas deben realizar su trabajo a través de la función indicada al comienzo.



def hasta_fin_de_mes(d, m, a):

    if ((m <= 7 and m % 2 != 0) or (m >= 7 and m % 2 == 0)): #mes de 31 dias
        dias = 31 - d
    elif ((m >= 7 and m % 2 != 0) or (m <= 7 and m % 2 == 0) and m != 2): #mes 30 dias
        dias = 30 - d
    elif m == 2 and ((a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)): #bisiesto
        dias = 29 - d
    elif m == 2 and ((a % 4 != 0) or (a % 100 == 0)): # no bisiesto
        dias = 28 - d

    return dias

#· Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir la cantidad de días que faltan hasta fin de año.

def ingresar_fecha():
    d = int(input("Ingrese el dia: "))
    m = int(input("Ingrese el mes: "))
    a = int(input("Ingrese el año: "))

    return d, m, a

def hasta_fin_año(d,m,a): #no anda 

    dias_restantes = 0
    ultimo_mes = m

    while m < 12:

        if ((m <= 7 and m % 2 != 0) or (m >= 7 and m % 2 == 0)): #mes de 31 dias
            dias_restantes += 31
        elif ((m >= 7 and m % 2 != 0) or (m <= 7 and m % 2 == 0) and m != 2): #mes 30 dias
            dias_restantes += 30
        elif m == 2 and ((a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)): #bisiesto
            dias_restantes += 29
        elif m == 2 and ((a % 4 != 0) or (a % 100 == 0)): # no bisiesto
            dias_restantes += 28
    
        m += 1
    
    fin_mes = hasta_fin_de_mes(d, ultimo_mes, a)
    
    if ultimo_mes == 12:
        return fin_mes
    else:

        dias_restantes += fin_mes
        
        return dias_restantes


#· Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir la cantidad de días transcurridos en ese año hasta esa fecha.

def dias_transcurridos(): # corregir mes 11

    d, m, a = ingresar_fecha()
    transcurridos = 0
    mes_actual = m

    while m > 0:

        if ((a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)): # bisiesto
            if m == 2:
                transcurridos += 29
        elif ((a % 4 != 0) or (a % 100 == 0)): # no bisiesto
            if m == 2:
                transcurridos += 28
        if ((m <= 7 and m % 2 != 0) or (m >= 7 and m % 2 == 0)): #31 dias
            transcurridos += 31
        elif ((m >= 7 and m % 2 != 0) or (m <= 7 and m % 2 == 0) and m != 2):
            transcurridos += 30

        m -= 1

    transcurridos = transcurridos - hasta_fin_de_mes(d, mes_actual, a)

    return transcurridos

#programa principal
d, m, a = ingresar_fecha()
print(hasta_fin_año(d,m,a))
    
    