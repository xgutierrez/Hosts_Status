import os

#Abriendo el archivo
path = r"C:\Users\dxgutiec\OneDrive - Pronaca\Practicas\PingVariosHosts\IPs.txt"
with open(path) as f:
    hosts = f.read().splitlines() 

active_hosts = []
deactive_hosts = []
number_host = 1
#Para parametrizar cuantas TTL debe tener el ping para considerar un host activo    
TTL_TO_BE_ACTIVE = 4

print(f"*** Se va a revisar {len(hosts)} hosts***")

for host in hosts:
    count_TTL = 0

    command = f"ping {host}"
    response = os.popen(command)
    list = response.readlines()
    

    for line in list:
        if "TTL" in line:
            count_TTL += 1

    #El número de TTL para saber si esta activo
    if count_TTL == TTL_TO_BE_ACTIVE:
        active_hosts.append(host)
        print(f"{number_host}. Respuesta {count_TTL}/{TTL_TO_BE_ACTIVE}, host {host} esta ACTIVO")
        number_host += 1
    else:
        deactive_hosts.append(host)
        print(f"{number_host}. Respuesta {count_TTL}/{TTL_TO_BE_ACTIVE}, host {host} esta ** INACTIVO **")
        number_host += 1

    
print(f"\n********** Resumen ***********")
print(f"ACTIVOS")
print(f"Número de hosts activos: {len(active_hosts)} ")
print(f"Listado de hosts activos: {active_hosts}")
print(f"\n**************************")
print(f"INACTIVOS")
print(f"Número de hosts inactivos: {len(deactive_hosts)}")
print(f"Listado de hosts inactivos: {deactive_hosts}")




