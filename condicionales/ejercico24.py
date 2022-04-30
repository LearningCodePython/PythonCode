# Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año 
# o cuántos años faltan para llegar a ese año.

fecha1 = int(input("Introduce el año actual "))
fecha2 = int(input("Introduce el año acalcular "))

if fecha1 > fecha2:
    print (f"Han pasado {fecha1 - fecha2} desde el año {fecha1}")
elif fecha1 < fecha2:
    print (f"Faltasn {fecha2 - fecha1} años para llegar al año {fecha2}")
else: 
    print (f"Son el mismo año")
