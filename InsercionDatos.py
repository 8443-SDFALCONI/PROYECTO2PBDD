"""
Importación de librerías
"""
#Librería para pedir la contraseña al usuario
import getpass
#Librería para utilizar los métodos para conectarse a la base de datos de Oracle
import oracledb
#Librería para poder leer los archivos CSV
import csv
#Pedir la contraseña de la base de datos y guardar en una variable
pw = getpass.getpass("Ingresa la contraseña de administrador: ")
#Crear la variable de conexión con los datos de la base de datos
connection = oracledb.connect(
    user="sebastian",
    password=pw,
    dsn="localhost:1521/xe")
print("Conexión Exitosa")
#Crear un cursor de conexión
cursor = connection.cursor()
#Leer los datos del CSV
reader = csv.reader(open("csv/examen.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)
#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblExamen" values (:1, :2, :3, :4)"""
    cur.execute(query, linea)
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/provincia.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblProvincia" values (:1, :2, :3)"""
    cur.execute(query, linea)
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/canton.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblCanton" values (:1, :2, :3, :4)"""
    cur.execute(query, linea)
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/permisos.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblPermisos" values (:1, :2, :3, :4)"""
    cur.execute(query, linea)
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/rol.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblRol" values (:1, :2, :3, :4)"""
    cur.execute(query, linea)
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/parametros.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblParametros" values (:1, :2, :3, :4, :5, :6, :7, :8, :9)"""
    cur.execute(query, linea)
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/usuario.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblUsuario" values (:1, :2, :3, :4, :5, :6, :7, :8, :9)"""
    cur.execute(query, linea)
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/parroquia.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblParroquia" values (:1, :2, :3, :4, :5)"""
    cur.execute(query, linea)
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/institucioneducativa.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblInstitucionEducativa" values (:1, :2, :3, :4, :5, :6, :7)"""
    cur.execute(query, linea)
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/sedes.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblSedes" values (:1, :2, :3, :4, :5, :6, :7, :8, :9)"""
    cur.execute(query, linea)
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/carreras.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblCarreras" values (:1, :2, :3, :4, :5, :6, :7)"""
    cur.execute(query, linea)
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/carrerassedes.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblCarrerasSedes" values (:1, :2, :3, :4, :5, :6, :7)"""
    cur.execute(query, linea)
    #Guardar los cambios en la base de datos de oracle
    connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/aspirantes.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblAspirantes" values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)"""
    cur.execute(query, linea)
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/examenaspiante.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblExamenAspirante" values (:1, :2, :3)"""
    cur.execute(query, linea)
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/postular.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblPostular" values (:1, :2, :3, :4, :5, :6, :7)"""
    cur.execute(query, linea)
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/postularparametros.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblPostularParametros" values (:1, :2, :3, :4, :5, :6)"""
    cur.execute(query, linea)
    connection.commit()
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/rolpermisos.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblRolPermisos" values (:1, :2)"""
    cur.execute(query, linea)
    connection.commit()
#Guardar los cambios en la base de datos de oracle
connection.commit()

#Leer el archivo CSV
reader = csv.reader(open("csv/usuariorolpermisos.csv", "r"))
#Omitir la fila de los nombres de los atributos en el CSV
next(reader)
#Crear un arreglo o lista
columna = []
#Crear un for para recorrer entre cada linea del archivo
for line in reader:
    #Agregar al array cada linea del archivo CSV
    columna.append(line)
    #Mostrar la línea del archivo CSV
    print(line)

#Crear un cursor de conexión
cur = connection.cursor()
#Recorrer cada línea en la lista
for linea in columna:
    #Insertar el dato
    print("Se insertó el dato")
    query = """insert into "TblUsuarioRolPermisos" values (:1, :2, :3)"""
    cur.execute(query, linea)
#Guardar los cambios en la base de datos de oracle
connection.commit()

