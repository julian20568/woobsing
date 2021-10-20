
################ PASO 1 ####################
Requisitos para correr proyecto
 * Instalar python3
 * Tener un entorno virtual
 * Instalar Django y Djangorestframework
 *Instalar mysql como gestor de BD
 * Instalar mysqlclient
 
################ PASO 2 ####################
1. Clonar el proyecto en local
   git clone git@github.com:julian20568/woobsing.git
2. Activar entorno virtual
   ir hasta el directorio del proyecto (woobsing) y escribir source entorno/bin/activate
3. Crear BD con el nombre de (palabras_claves) en mysql
4. Cambiar la configuracion de conexión de BD en el archivo settings del proyecto con las credenciales correspondientes a su gestor de BD mysql 
   o por defecto descomente la conexión de sqlite3 y comente la conexión de mysql

################ PASO 3 ####################
1. para agregar la lista de las palabras ingrese la siguiente dirección en un cliente REST (Postman) con el método POST y copie el contenido que 
   hay dentro del archivo PalabrasClaves.json y ejecute.
   http://127.0.0.1:8000/api/palabras
   
2. Para ver la lista de palabras claves ingrese la siguiente dirección en un cliente REST (Postman) con el método GET y listo

GRACIAS!!!
