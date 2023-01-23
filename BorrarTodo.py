"""
Importación de librerías
"""
#Librería para pedir la contraseña al usuario
import getpass
#Librería para utilizar los métodos para conectarse a la base de datos de Oracle
import oracledb
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

#Borrar la tabla
cursor.execute("""
    drop table "TblAspirantes" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblParroquia" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblCanton" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblCarreras" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblCarrerasSedes" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblExamen" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblExamenAspirante" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblInstitucionEducativa" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblParametros" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblPermisos" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblPostular" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblPostularParametros" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblProvincia" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblRol" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblRolPermisos" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblSedes" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblUsuario" CASCADE CONSTRAINTS""")
#Borrar la tabla
cursor.execute("""
    drop table "TblUsuarioRolPermisos" CASCADE CONSTRAINTS""")