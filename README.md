# Hosts_Status

Este código se encarga de revisar el estado de varios hosts en una red, utilizando el comando ping.

Funcionamiento
1. El archivo IPs.txt contiene una lista de direcciones IP o nombres de host a revisar.
2. El código abre el archivo y almacena las direcciones en una lista.
3. Se crean dos listas vacías para almacenar los hosts activos y los inactivos.
4. Se establece una variable TTL_TO_BE_ACTIVE para parametrizar cuántas respuestas 'TTL' deben ser recibidas para considerar un host como activo.
5. Se itera sobre la lista de hosts y se ejecuta el comando ping para cada dirección.
6. Se cuentan las respuestas 'TTL' en la salida del comando y se comparan con el valor de TTL_TO_BE_ACTIVE.
7. Si el número de respuestas 'TTL' es igual al valor de TTL_TO_BE_ACTIVE, se considera que el host está activo y se agrega a la lista de hosts activos. En caso contrario, se considera que el host está inactivo y se agrega a la lista de hosts inactivos.
8. Finalmente, se imprime un resumen con el número de hosts activos e inactivos y las direcciones correspondientes.

Nota
Es importante modificar la ruta del archivo IPs.txt para que apunte a la ubicación correcta en su sistema.
