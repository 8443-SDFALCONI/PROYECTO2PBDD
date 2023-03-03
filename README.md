# Proyecto de Base de Datos Segundo Parcial
## Integrantes:
Sebastian Falconi

Emilio Ñacato
### NRC: 8393

### _Proyecto 2do Parcial_

En el presente repositorio se almacena el código de PYTHON para crear las tablas, cargar datos en la base de datos de Oracle y ejecutar el sitio web

### 1. CreacionTablas.py
```
En este archivo se podrá encontrar el código utilizado para crear la base de datos y las tablas de la base de datos relacional del tema de Senescyt
```

### 2. InsercionDatos.py
```
En este archivo se podrá encontrar el código utilizado para cargar los datos en la base de datos relacional del tema de Senescyt
```

### 3. BorrarTodo.py (OPCIONAL)
```
En este archivo se podrá encontrar el código utilizado para borrar los datos y la tabla en la base de datos relacional del tema de Senescyt
```

### CSV
```
En esta carpeta se encontrarán los archivos CSV para cargar los datos generados sintéticamente para cada una de las 18 entidades de la base de datos relacional
```

### GLIFFY
```
En esta carpeta se encontrarán los archivos de los diagramas DER, Lógico, y Físico de la base de datos relacional
```

### web-flask
```
En esta carpeta se encontrarán los archivos de la web que se implementa con Flask en Python y que realiza consultas SQL a la base de datos de Oracle
```



- Código desarrollado en Colab Google
- Archivos por cada una de las entidades consideradas en la base de datos relacional
- Imágenes de ejecución del código con tablas de resultados
- Archivos de Excel requeridos para cargar los cantones y sedes del Ecuador
- Archivos CSV con los datos generados por cada una de las entidades

## Archivos de Código

En el presente repositorio se cargó cada uno de los archivos de Python que permiten generar los datos sintéticos para las dieciocho entidades consideradas en el proyecto de base de datos.

### 1. Aspirante
```
En este archivo se podrá encontrar el código necesario para generar datos sintéticos de un aspirante a la educación superior. Se consideraron como atributos: la cédula del aspirante, sus nombres y apellidos, el correo, su género, un teléfono, la fecha de nacimiento, la edad, el estado del aspirante, el estado de gratuidad (para el acceso a la educación superior) del aspirante, el estado civil, y un ID como clave foránea.
```

### 2. Cantón
```
En este archivo se podrá encontrar el código necesario con los datos para cargar los nombres de los cantones del Ecuador. Para esta entidad se consideraron como atributos: el id del cantón, el nombre del cantón, su estado, y la clave foránea del ID de la provincia.
```

### 3. Carrera
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos de las carreras ofertadas del sistema de educación. Para esta entidad se consideraron como atributos: el id de la carrera, su nombre, la descripción, el estado, la fecha de inicio de vigencia de la carrera, la modalidad, y la jornada.
```

### 4. Consta
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos la entidad consta, la cual surge de una relación n a n entre dos entidades. Para esta entidad se consideraron como atributos las claves foráneas: ID de la institución educativa, ID de la carrera, ID de la sede, ID de la parroquia, ID del cantón, e ID de la provincia.
```

### 5. Contiene
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos la entidad contiene, la cual surge de una relación n a n entre dos entidades. Para esta entidad se consideraron como atributos las claves foráneas: ID del usuario, ID del rol, e ID del permiso.
```

### 6. Establece
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos la entidad establece, la cual surge de una relación n a n entre dos entidades. Para esta entidad se consideraron como atributos las claves foráneas: ID del rol, e ID del permiso.
```

### 7. Examen 
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos de los examenes aplicados a los estudiantes del sistema de educación. Para esta entidad se consideraron como atributos: el id del examen, la fecha de aplicación del examen, el estado, y el puntaje que obtuvo el estudiante.
```

### 8. Institucion Educativa
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos de las instituciones educativas que pertenecen al sistema de educación. Para esta entidad se consideraron como atributos: el id de la institución educativa, su nombre, el correo, el teléfono, su descripción, el estado de la institución, y el tipo.
```

### 9. Parámetros
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos de los parámetros considerados por parte de la base legal que pertenecen al sistema de educación. Para esta entidad se consideraron como atributos: el id del parámetro, los puntajes de acción afirmativa socioeconómicos, de territorialidad, de ruralidad, de vulnerabilidad, así como el puntaje de acción afirmativa de pueblos y nacionalidades. Además se incluye los atributos del número de cupos que oferta una carrera, la fecha en la que fue ofertado un cupo, y el puntaje referencial de la carrera.
```

### 10. Parroquia
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos de las parroquias para cada una de las instituciones educativas que pertenecen al sistema de educación. Para esta entidad se consideraron como atributos: el id de la parroquia, el nombre de la parroquia, el estado, el id de la provincia como clave foránea, y el id del cantón de igual forma como clave foránea.
```

### 11. Permisos
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos de los permisos de los usuarios que pertenecen al sistema de educación. Para esta entidad se consideraron como atributos: el id del permiso, el tipo del permiso, su estado, y la descripción.
```

### 12. Pertenece
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos de la entidad pertenece, la cual surge de una relación n a n entre dos entidades. Para esta entidad se consideraron como atributos las claves foráneas: ID del usuario, la cédula de ciudadanía del aspirante, y el id del examen.
```

### 13. Postular
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos de la entidad postular, la cual surge de una relación n a n entre dos entidades. Para esta entidad se consideraron como atributos las claves foráneas: ID de postular, su estado, el puntaje; las claves foráneas: id examen, el id de carrera, id de usuario, y la cédula de ciudadanía del aspirante.
```

### 14. Provincia
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos de la entidad de Provincia. Para esta entidad se consideraron como atributos: ID de provincia, su nombre de provincia, y el estado.
```

### 15. Rige
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos de la entidad rige, la cual surge de una relación n a n entre dos entidades. Para esta entidad se consideraron como atributos las claves foráneas: ID de postular, id de examen, id de carrera, id de usuario, cédula de ciudadanía del aspirante, y el id de Parametro.
```

### 16. Rol
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos de la entidad de rol. Para esta entidad se consideraron como atributos: ID de rol, tipo de rol, estado de rol, y su descripción.
```

### 17. Sede
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos de la entidad de sede. Para esta entidad se consideraron como atributos las claves foráneas: ID de sede, nombre de la sede, su descripción, el teléfono, su estado, y las claves foráneas: id provincia, id parroquia, id cantón, id institución educativa.
```

### 18. Usuario
```
En este archivo se podrá encontrar el código necesario para crear datos sintéticos de la entidad de Usuario. Para esta entidad se consideraron como atributos las claves foráneas: ID de usuario, nombres, apellidos, correo, estado, contraseña, nickname, genero, y telefono.
```
