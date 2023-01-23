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
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblProvincia"(
        "VarIdentificadorProvincia" VARCHAR(50) PRIMARY KEY NOT NULL,
        "VarNombreProvincia" VARCHAR(40) NOT NULL,
        "VarEstadoProvincia" VARCHAR(10) NOT NULL)""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblCanton"(
        "VarIdentificadorCanton" VARCHAR(50) NOT NULL,
        "VarNombreCanton" VARCHAR(30) NOT NULL,
        "VarEstadoCanton" VARCHAR(10) NOT NULL,
        "VarIdentificadorProvincia" VARCHAR(50) NOT NULL,
        CONSTRAINT "VarPkCanton" PRIMARY KEY ("VarIdentificadorCanton","VarIdentificadorProvincia"),
        FOREIGN KEY ("VarIdentificadorProvincia") REFERENCES "TblProvincia"("VarIdentificadorProvincia")
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblPermisos"(
        "VarIdentificadorPermisos" VARCHAR(50) PRIMARY KEY,
        "VarTipoPermisos" VARCHAR(20) NOT NULL,
        "VarEstadoPermisos" VARCHAR(10) NOT NULL,
        "VarDescripcionPermisos" VARCHAR(500) NOT NULL
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblRol"(
        "VarIdentificadorRol" VARCHAR(50) PRIMARY KEY NOT NULL,
        "VarTipoRol" VARCHAR(20) NOT NULL,
        "VarEstadoRol" VARCHAR(20) NOT NULL,
        "VarDescripcionRol" VARCHAR(500) NOT NULL
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblParametros"(
        "VarIdentificadorParametros" VARCHAR(50) PRIMARY KEY NOT NULL,
        "VarAccionAfirSocioecoParametros" VARCHAR(20) NOT NULL,
        "VarAccionAfirTerriParametros" VARCHAR(20) NOT NULL,
        "VarAccionAfirRuralParametros" VARCHAR(20) NOT NULL,
        "VarAccionAfirVulneraParametros" VARCHAR(5) NOT NULL,
        "VarAccionAfirPueblosNacionParametros" VARCHAR(20) NOT NULL,
        "VarCuposOfertaCarParametros" VARCHAR(10) NOT NULL,
        "DtCuposOfertaCarParametros" DATE NOT NULL,
        "VarNotaReferCarParametros" VARCHAR(4) NOT NULL
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblExamen"(
        "VarIdentificadorExamen" VARCHAR(50) PRIMARY KEY NOT NULL,
        "DtFechaExamen" DATE NOT NULL,
        "VarEstadoExamen" VARCHAR(10) NOT NULL,
        "VarNotaExamen" VARCHAR(4) NOT NULL
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblUsuario"(
        "VarIdentificadorUsuario" VARCHAR(50) PRIMARY KEY NOT NULL,
        "VarNombresUsuario" VARCHAR(50) NOT NULL,
        "VarApellidosUsuario" VARCHAR(50) NOT NULL,
        "VarCorreoUsuario" VARCHAR(50) NOT NULL,
        "VarEstadoUsuario" VARCHAR(10) NOT NULL,
        "VarContraseniaUsuario" VARCHAR(20) NOT NULL,
        "VarNicknameUsuario" VARCHAR(30) NOT NULL,
        "VarGeneroUsuario" VARCHAR(5) NOT NULL,
        "NbrTelefonoUsuario" NUMBER NOT NULL
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblCarreras"(
        "VarIdentificadorCarreras" VARCHAR(50) PRIMARY KEY NOT NULL,
        "VarNombreCarreras" VARCHAR(120) NOT NULL,
        "VarDescripcionCarreras" VARCHAR(500) NOT NULL,
        "VarEstadoCarreras" VARCHAR(10) NOT NULL,
        "DtFechaVigenciaCarreras" DATE NOT NULL,
        "VarModalidadCarreras" VARCHAR(20) NOT NULL,
        "VarJornadaCarreras" VARCHAR(20) NOT NULL
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblParroquia"(
        "VarIdentificadorParroquia" VARCHAR(50) NOT NULL,
        "VarNombreParroquia" VARCHAR(50) NOT NULL,
        "VarEstadoParroquia" VARCHAR(10) NOT NULL,
        "VarIdentificadorProvincia" VARCHAR(50) NOT NULL,
        "VarIdentificadorCanton" VARCHAR(50) NOT NULL,
        CONSTRAINT "VarPkParro" PRIMARY KEY("VarIdentificadorParroquia","VarIdentificadorCanton","VarIdentificadorProvincia"),
        FOREIGN KEY("VarIdentificadorCanton", "VarIdentificadorProvincia") REFERENCES "TblCanton"("VarIdentificadorCanton", "VarIdentificadorProvincia")
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblInstitucionEducativa"(
        "VarIdentificadorInstitucionEducativa" VARCHAR(50) PRIMARY KEY NOT NULL,
        "VarNombreInstitucionEducativa" VARCHAR(50) NOT NULL,
        "VarCorreoInstitucionEducativa" VARCHAR(50) NOT NULL,
        "NbrTelefonoInstitucionEducativa" NUMBER NOT NULL,
        "VarDescripcionInstitucionEducativa" VARCHAR(500) NOT NULL,
        "VarEstadoInstitucionEducativa" VARCHAR(10) NOT NULL,
        "VarTipoInstitucionEducativa" VARCHAR(10) NOT NULL
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblSedes"(
        "VarIdentificadorSedes" VARCHAR(50) NOT NULL,
        "VarNombreSedes" VARCHAR(50) NOT NULL,
        "VarDescripcionSedes" VARCHAR(500) NOT NULL,
        "NbrTelefonoSedes" NUMBER NOT NULL,
        "VarEstadoSedes" VARCHAR(10) NOT NULL,
        "VarIdentificadorProvincia" VARCHAR(50) NOT NULL,
        "VarIdentificadorParroquia" VARCHAR(50) NOT NULL,
        "VarIdentificadorCanton" VARCHAR(50) NOT NULL,
        "VarIdentificadorInstitucionEducativa" VARCHAR(50) NOT NULL,
        CONSTRAINT "VarPkSe" PRIMARY KEY("VarIdentificadorSedes","VarIdentificadorInstitucionEducativa","VarIdentificadorParroquia","VarIdentificadorCanton","VarIdentificadorProvincia"),
        FOREIGN KEY ("VarIdentificadorCanton","VarIdentificadorProvincia","VarIdentificadorParroquia") 
        REFERENCES "TblParroquia"("VarIdentificadorCanton","VarIdentificadorProvincia","VarIdentificadorParroquia"),
        FOREIGN KEY ("VarIdentificadorInstitucionEducativa") 
        REFERENCES "TblInstitucionEducativa"("VarIdentificadorInstitucionEducativa")
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblCarrerasSedes"(
        "VarIdentificadorCarrerasSedes" VARCHAR(50) NOT NULL,
        "VarIdentificadorInstitucionEducativa" VARCHAR(50) NOT NULL,
        "VarIdentificadorCarreras" VARCHAR(50) NOT NULL,
        "VarIdentificadorSedes" VARCHAR(50) NOT NULL,
        "VarIdentificadorParroquia" VARCHAR(50) NOT NULL,
        "VarIdentificadorCanton" VARCHAR(50) NOT NULL,
        "VarIdentificadorProvincia" VARCHAR(50) NOT NULL,
        CONSTRAINT "VarPkCarSe" PRIMARY KEY("VarIdentificadorSedes","VarIdentificadorCanton","VarIdentificadorProvincia","VarIdentificadorParroquia","VarIdentificadorInstitucionEducativa","VarIdentificadorCarreras","VarIdentificadorCarrerasSedes"),
        FOREIGN KEY ("VarIdentificadorSedes","VarIdentificadorCanton","VarIdentificadorProvincia","VarIdentificadorParroquia","VarIdentificadorInstitucionEducativa") 
        REFERENCES "TblSedes"("VarIdentificadorSedes","VarIdentificadorCanton","VarIdentificadorProvincia","VarIdentificadorParroquia","VarIdentificadorInstitucionEducativa"),
        FOREIGN KEY ("VarIdentificadorCarreras") REFERENCES "TblCarreras"("VarIdentificadorCarreras")
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblAspirantes"(
        "VarCedulaAspirantes" VARCHAR(10) NOT NULL,
        "VarNombresAspirantes" VARCHAR(50) NOT NULL,
        "VarApellidosAspirantes" VARCHAR(50) NOT NULL,
        "VarCorreoAspirantes" VARCHAR(50) NOT NULL,
        "VarGeneroAspirantes" VARCHAR(5) NOT NULL,
        "NbrTelefonoAspirantes" NUMBER NOT NULL,
        "DtFechaNacimientoAspirantes" DATE NOT NULL,
        "NbrEdadAspirantes" NUMBER NOT NULL,
        "VarEstadoAspirantes" VARCHAR(10) NOT NULL,
        "VarEstadoGratuidadAspirantes" VARCHAR(30) NOT NULL,
        "VarEstadoCivilAspirantes" VARCHAR(30) NOT NULL,
        "VarIdentificadorUsuario" VARCHAR(50) NOT NULL,
        CONSTRAINT "VarPkAs" PRIMARY KEY("VarCedulaAspirantes","VarIdentificadorUsuario"),
        FOREIGN KEY("VarIdentificadorUsuario") REFERENCES "TblUsuario"("VarIdentificadorUsuario")
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblExamenAspirante"(
        "VarIdentificadorUsuario" VARCHAR(50) NOT NULL,
        "VarCedulaAspirantes" VARCHAR(10) NOT NULL,
        "VarIdentificadorExamen" VARCHAR(50) NOT NULL,
        CONSTRAINT "VarPkExamenAspirante" PRIMARY KEY("VarCedulaAspirantes","VarIdentificadorUsuario","VarIdentificadorExamen"),
        FOREIGN KEY("VarIdentificadorUsuario","VarCedulaAspirantes") REFERENCES "TblAspirantes"("VarIdentificadorUsuario","VarCedulaAspirantes"),
        FOREIGN KEY ("VarIdentificadorExamen") REFERENCES "TblExamen"("VarIdentificadorExamen")
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblPostular"(
        "VarIdentificadorPostular" VARCHAR(50) NOT NULL,
        "VarEstadoPostular" VARCHAR(10) NOT NULL,
        "VarPuntajePostular" VARCHAR(4) NOT NULL,
        "VarIdentificadorExamen" VARCHAR(50) NOT NULL,
        "VarIdentificadorCarreras" VARCHAR(50) NOT NULL,
        "VarIdentificadorUsuario" VARCHAR(50) NOT NULL,
        "VarCedulaAspirantes" VARCHAR(10) NOT NULL,
        CONSTRAINT "VarPkPos" PRIMARY KEY ("VarIdentificadorCarreras","VarCedulaAspirantes","VarIdentificadorUsuario","VarIdentificadorExamen","VarIdentificadorPostular"),
        FOREIGN KEY ("VarIdentificadorCarreras") REFERENCES "TblCarreras"("VarIdentificadorCarreras"),
        FOREIGN KEY ("VarCedulaAspirantes","VarIdentificadorUsuario","VarIdentificadorExamen") REFERENCES "TblExamenAspirante"("VarCedulaAspirantes","VarIdentificadorUsuario","VarIdentificadorExamen")
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblPostularParametros"(
        "VarIdentificadorPostular" VARCHAR(50) NOT NULL,
        "VarIdentificadorExamen" VARCHAR(50) NOT NULL,
        "VarIdentificadorCarreras" VARCHAR(50) NOT NULL,
        "VarIdentificadorUsuario" VARCHAR(50) NOT NULL,
        "VarCedulaAspirantes" VARCHAR(10) NOT NULL,
        "VarIdentificadorParametros" VARCHAR(50) NOT NULL,
        CONSTRAINT "PkRige" PRIMARY KEY("VarIdentificadorCarreras","VarCedulaAspirantes","VarIdentificadorUsuario","VarIdentificadorExamen","VarIdentificadorPostular","VarIdentificadorParametros"),
        FOREIGN KEY ("VarIdentificadorCarreras","VarCedulaAspirantes","VarIdentificadorUsuario","VarIdentificadorExamen","VarIdentificadorPostular")
        REFERENCES "TblPostular"("VarIdentificadorCarreras","VarCedulaAspirantes","VarIdentificadorUsuario","VarIdentificadorExamen","VarIdentificadorPostular"),
        FOREIGN KEY ("VarIdentificadorParametros") REFERENCES "TblParametros"("VarIdentificadorParametros")
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblRolPermisos"(
        "VarIdentificadorRol" VARCHAR(50) NOT NULL,
        "VarIdentificadorPermisos" VARCHAR(50) NOT NULL,
        CONSTRAINT "VarPkRolPermisos" PRIMARY KEY("VarIdentificadorRol","VarIdentificadorPermisos"),
        FOREIGN KEY ("VarIdentificadorRol") REFERENCES "TblRol"("VarIdentificadorRol"),
        FOREIGN KEY ("VarIdentificadorPermisos") REFERENCES "TblPermisos"("VarIdentificadorPermisos")
        )""")
#Utilizando el cursor se ejecutará el código SQL para crear la tabla
cursor.execute("""
    create table "TblUsuarioRolPermisos"(
        "VarIdentificadorUsuario" VARCHAR(50) NOT NULL,
        "VarIdentificadorRol" VARCHAR(50) NOT NULL,
        "VarIdentificadorPermisos" VARCHAR(50) NOT NULL,
        CONSTRAINT "VarPkUsuarioRolPermisos" PRIMARY KEY ("VarIdentificadorUsuario","VarIdentificadorRol","VarIdentificadorPermisos"),
        FOREIGN KEY ("VarIdentificadorUsuario") REFERENCES "TblUsuario"("VarIdentificadorUsuario"),
        FOREIGN KEY ("VarIdentificadorRol","VarIdentificadorPermisos") REFERENCES "TblRolPermisos"("VarIdentificadorRol","VarIdentificadorPermisos")
        )""")
#Guardar los cambios
connection.commit()
