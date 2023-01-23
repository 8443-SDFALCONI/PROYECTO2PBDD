#!/usr/bin/env python
from __future__ import print_function
from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin
import logging
import os
import oracledb
from waitress import serve
from flask import render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import os
from flask import render_template, request, redirect, url_for, flash

os.environ["PYTHON_USERNAME"] = "sebastian"
os.environ["PYTHON_PASSWORD"] = "123123Oracle"
os.environ["PYTHON_CONNECTSTRING"] = "localhost:1521/xe"

app = Flask(__name__)
app.secret_key = '123123Flask'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

CORS(app)
cors = CORS(app, resources={
            r"/api/*": {"origins": "*", "methods": "POST,DELETE,PUT,GET,OPTIONS"}})


def start_pool():

    # Generally a fixed-size pool is recommended, i.e. pool_min=pool_max.
    # Here the pool contains 4 connections, which is fine for 4 conncurrent
    # users and absolutely adequate for this demo.

    pool_min = 4
    pool_max = 4
    pool_inc = 0

    print("Connecting to", os.environ.get("PYTHON_CONNECTSTRING"))

    pool = oracledb.create_pool(
        user=os.environ.get("PYTHON_USERNAME"),
        password=os.environ.get("PYTHON_PASSWORD"),
        dsn=os.environ.get("PYTHON_CONNECTSTRING"),
        min=pool_min,
        max=pool_max,
        increment=pool_inc
    )

    return pool


def create_schema():
    with pool.acquire() as connection:
        with connection.cursor() as cursor:

            try:
                cursor.execute(
                    """
                    select * from "TblRol"
                    """
                )
            except oracledb.Error as err:
                error_obj, = err.args
                print(f"Conexión no extiosa: {error_obj.message}")


pool = start_pool()

# Try to create the demo table
create_schema()

# aplicacion principal - login


@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for("login"))
    return render_template('web.html')

# Portal de administracion


@app.route('/sistema/')
def sistema():
    id = current_user.get_id()
    return render_template('/sistema.html')

# Portal de administracion


@app.route('/administracion/')
def administracion():
    id = current_user.get_id()
    return render_template('/administracion.html')




@app.route("/ver_queries")
def ver_queries():
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    '''
                    SELECT asp."VarCedulaAspirantes" AS "CedulaAspirantes", asp."VarNombresAspirantes" AS "NombresAspirantes", asp."VarApellidosAspirantes" AS "ApellidosAspirantes", exa."VarEstadoExamen" AS "EstadoExamen", asp."VarGeneroAspirantes" AS "GeneroAspirantes", exa."VarNotaExamen" AS "NotaExamen", exa."DtFechaExamen" AS "FechaExamen" FROM "TblExamenAspirante" exas
INNER JOIN "TblAspirantes" asp ON asp."VarCedulaAspirantes" = exas."VarCedulaAspirantes"
INNER JOIN "TblExamen" exa ON exa."VarIdentificadorExamen" = exas."VarIdentificadorExamen"
WHERE asp."VarGeneroAspirantes" LIKE 'M' AND exa."VarEstadoExamen" LIKE 'Activo'
GROUP BY asp."VarCedulaAspirantes",asp."VarNombresAspirantes", asp."VarApellidosAspirantes", exa."VarEstadoExamen", asp."VarGeneroAspirantes", exa."VarNotaExamen", exa."DtFechaExamen"
HAVING exa."VarNotaExamen">=875
                    ''')
                resultado = cursor.fetchall()
            except oracledb.Error as err:
                error_obj, = err.args
                print(f"Conexión no exitosa: {error_obj.message}")
    return render_template('/sistema/ver_queries.html', resultado=resultado)


@app.route("/ver_queries2")
def ver_queries2():
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    '''
                    SELECT asp."VarCedulaAspirantes" AS "CedulaAspirantes", asp."VarNombresAspirantes" AS "NombresAspirantes", asp."VarApellidosAspirantes" AS "ApellidosAspirantes", asp."NbrTelefonoAspirantes" AS "NumeroTelefonoAspirantes", exa."VarNotaExamen" AS "NotaExamen", car."VarNombreCarreras" AS "NombreCarrera", car."VarModalidadCarreras" AS "ModalidadCarrera", car."VarJornadaCarreras" AS "JornadaCarrera" FROM "TblExamenAspirante" exas
INNER JOIN "TblAspirantes" asp ON asp."VarCedulaAspirantes" = exas."VarCedulaAspirantes"
INNER JOIN "TblExamen" exa ON exa."VarIdentificadorExamen" = exas."VarIdentificadorExamen"
INNER JOIN "TblPostular" post ON post."VarCedulaAspirantes" = exas."VarCedulaAspirantes"
INNER JOIN "TblCarreras" car ON car."VarIdentificadorCarreras" = post."VarIdentificadorCarreras"
WHERE car."VarNombreCarreras" LIKE 'Licenciatura%'
GROUP BY car."VarIdentificadorCarreras",asp."VarCedulaAspirantes", asp."VarNombresAspirantes", asp."VarApellidosAspirantes", asp."NbrTelefonoAspirantes", exa."VarNotaExamen", car."VarNombreCarreras", car."VarModalidadCarreras", car."VarJornadaCarreras"
ORDER BY exa."VarNotaExamen" DESC
FETCH FIRST 50 ROWS ONLY
                    ''')
                resultado = cursor.fetchall()
            except oracledb.Error as err:
                error_obj, = err.args
                print(f"Conexión no exitosa: {error_obj.message}")
    return render_template('/sistema/ver_queries2.html', resultado=resultado)


@app.route("/ver_queries3")
def ver_queries3():
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    '''
                    SELECT par."VarIdentificadorParroquia" AS "IdParroquia",par."VarNombreParroquia" AS "NombreParroquia", COUNT(car."VarIdentificadorCarreras") AS "NumeroCarreras", par."VarEstadoParroquia" AS "EstadoParroquia" FROM "TblCarrerasSedes" carse
INNER JOIN "TblCarreras" car ON car."VarIdentificadorCarreras" = carse."VarIdentificadorCarreras"
INNER JOIN "TblSedes" se ON se."VarIdentificadorSedes" = carse."VarIdentificadorSedes"
INNER JOIN "TblParroquia" par ON par."VarIdentificadorParroquia" = se."VarIdentificadorParroquia"
WHERE par."VarEstadoParroquia" LIKE 'Activo'
GROUP BY par."VarIdentificadorParroquia",par."VarNombreParroquia",par."VarEstadoParroquia"
HAVING COUNT(car."VarIdentificadorCarreras") >=4
                    ''')
                resultado = cursor.fetchall()
            except oracledb.Error as err:
                error_obj, = err.args
                print(f"Conexión no exitosa: {error_obj.message}")
    return render_template('/sistema/ver_queries3.html', resultado=resultado)


@app.route("/ver_queries4")
def ver_queries4():
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    '''
                    SELECT asp."VarCedulaAspirantes" AS "CedulaAspirante", asp."VarNombresAspirantes" AS "NombresAspirante", asp."VarApellidosAspirantes" AS "ApellidosAspirante", asp."VarCorreoAspirantes" AS "CorreoAspirante", asp."VarGeneroAspirantes" AS "GeneroAspirante", asp."NbrTelefonoAspirantes" AS "TelefonoAspirante", exa."VarNotaExamen" AS "NotaExamen", exa."VarEstadoExamen" AS "EstadoExamen",('BECADO') AS "Mensaje" FROM "TblExamenAspirante" exas
INNER JOIN "TblAspirantes" asp ON asp."VarCedulaAspirantes" = exas."VarCedulaAspirantes"
INNER JOIN "TblExamen" exa ON exa."VarIdentificadorExamen" = exas."VarIdentificadorExamen"
WHERE exa."VarNotaExamen" >= 975 AND exa."VarEstadoExamen" = 'Activo'
ORDER BY exa."VarNotaExamen" DESC
                    ''')
                resultado = cursor.fetchall()
            except oracledb.Error as err:
                error_obj, = err.args
                print(f"Conexión no exitosa: {error_obj.message}")
    return render_template('/sistema/ver_queries4.html', resultado=resultado)


@app.route("/ver_queries5")
def ver_queries5():
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    '''
                    SELECT asp."VarCedulaAspirantes" AS "CedulaAspirante", asp."VarNombresAspirantes" AS "NombresAspirante", asp."VarApellidosAspirantes" AS "ApellidosAspirante", asp."VarGeneroAspirantes" AS "GeneroAspirante", asp."NbrEdadAspirantes" AS "EdadAspirante", us."VarNombresUsuario" AS "NombresUsuario", us."VarApellidosUsuario" AS "ApellidosUsuario", rol."VarTipoRol" AS "TipoRol" FROM "TblAspirantes" asp
INNER JOIN "TblUsuario" us ON us."VarIdentificadorUsuario" = asp."VarIdentificadorUsuario"
INNER JOIN "TblUsuarioRolPermisos" usrolper ON usrolper."VarIdentificadorUsuario" = us."VarIdentificadorUsuario"
INNER JOIN "TblRolPermisos" rolper ON rolper."VarIdentificadorRol" = usrolper."VarIdentificadorRol"
INNER JOIN "TblRol" rol ON rol."VarIdentificadorRol" = rolper."VarIdentificadorRol" 
WHERE rol."VarTipoRol" LIKE 'Administrador/a' AND asp."NbrEdadAspirantes" BETWEEN 20 and 25
GROUP BY asp."VarCedulaAspirantes",asp."VarNombresAspirantes", asp."VarApellidosAspirantes", asp."VarGeneroAspirantes", asp."NbrEdadAspirantes", us."VarNombresUsuario", us."VarApellidosUsuario", rol."VarTipoRol"
ORDER BY asp."NbrEdadAspirantes" ASC
                    ''')
                resultado = cursor.fetchall()
            except oracledb.Error as err:
                error_obj, = err.args
                print(f"Conexión no exitosa: {error_obj.message}")
    return render_template('/sistema/ver_queries5.html', resultado=resultado)


@app.route("/ver_queries6")
def ver_queries6():
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    '''
                    SELECT asp."VarCedulaAspirantes" AS "CedulaAspirante", asp."VarNombresAspirantes" AS "NombresAspirante", asp."VarApellidosAspirantes" AS "ApellidosAspirante", asp."VarCorreoAspirantes" AS "CorreoAspirantes",asp."VarGeneroAspirantes" AS "GeneroAspirante", para."VarAccionAfirSocioecoParametros" AS "AccionAfirSocioecoParametros", para."VarAccionAfirTerriParametros" AS "AccionAfirTerriParametros", para."VarAccionAfirRuralParametros" AS "AccionAfirRuralParametros", para."VarAccionAfirVulneraParametros" AS "AccionAfirVulneraParametros", para."VarAccionAfirPueblosNacionParametros" AS "AccionAfirPueblosNacionParametros" FROM "TblPostularParametros" pospa
INNER JOIN "TblParametros" para ON para."VarIdentificadorParametros" = pospa."VarIdentificadorParametros"
INNER JOIN "TblPostular" pos ON pos."VarIdentificadorPostular" = pospa."VarIdentificadorPostular"
INNER JOIN "TblExamenAspirante" exas ON exas."VarCedulaAspirantes" = pos."VarCedulaAspirantes"
INNER JOIN "TblAspirantes" asp ON asp."VarCedulaAspirantes" = exas."VarCedulaAspirantes"
WHERE para."VarAccionAfirSocioecoParametros" LIKE 'Verdadero' AND para."VarAccionAfirTerriParametros" LIKE 'Verdadero' AND para."VarAccionAfirRuralParametros" LIKE 'Verdadero' AND para."VarAccionAfirVulneraParametros" LIKE '6' AND para."VarAccionAfirPueblosNacionParametros" LIKE 'Verdadero'
                    ''')
                resultado = cursor.fetchall()
            except oracledb.Error as err:
                error_obj, = err.args
                print(f"Conexión no exitosa: {error_obj.message}")
    return render_template('/sistema/ver_queries6.html', resultado=resultado)


@app.route("/ver_queries7")
def ver_queries7():
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    '''
                    SELECT asp."VarCedulaAspirantes" AS "CedulaAspirante", asp."VarNombresAspirantes" AS "NombresAspirante", asp."VarApellidosAspirantes" AS "ApellidosAspirante",car."VarNombreCarreras" AS "NombreCarrera", pos."VarPuntajePostular" AS "PuntajePostular", para."VarNotaReferCarParametros" AS "NotaReferencialCarreras", para."VarCuposOfertaCarParametros" AS "CuposOfertadosCarreras", car."VarJornadaCarreras" AS "JornadaCarreras", car."VarModalidadCarreras" AS "ModalidadCarreras", asp."VarEstadoAspirantes" AS "EstadoAspirante", car."VarEstadoCarreras" AS "EstadoCarreras", ('Posible asignacion de cupo') AS "Mensaje" FROM "TblPostularParametros" pospa
INNER JOIN "TblParametros" para ON para."VarIdentificadorParametros" = pospa."VarIdentificadorParametros"
INNER JOIN "TblPostular" pos ON pos."VarIdentificadorPostular" = pospa."VarIdentificadorPostular"
INNER JOIN "TblExamenAspirante" exas ON exas."VarCedulaAspirantes" = pos."VarCedulaAspirantes"
INNER JOIN "TblAspirantes" asp ON asp."VarCedulaAspirantes" = exas."VarCedulaAspirantes"
INNER JOIN "TblCarreras" car ON car."VarIdentificadorCarreras" = pos."VarIdentificadorCarreras"
WHERE pos."VarPuntajePostular" >= para."VarNotaReferCarParametros" AND para."VarCuposOfertaCarParametros" >= 1 AND asp."VarEstadoAspirantes" LIKE 'Activo' AND car."VarEstadoCarreras" LIKE 'Activo'
GROUP BY asp."VarCedulaAspirantes", asp."VarNombresAspirantes", asp."VarApellidosAspirantes",car."VarNombreCarreras", pos."VarPuntajePostular", para."VarNotaReferCarParametros", para."VarCuposOfertaCarParametros", car."VarJornadaCarreras", car."VarModalidadCarreras", asp."VarEstadoAspirantes", car."VarEstadoCarreras", ('Posible asignacion de cupo')
                    ''')
                resultado = cursor.fetchall()
            except oracledb.Error as err:
                error_obj, = err.args
                print(f"Conexión no exitosa: {error_obj.message}")
    return render_template('/sistema/ver_queries7.html', resultado=resultado)


@app.route("/ver_queries8")
def ver_queries8():
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    '''
                    SELECT car."VarNombreCarreras" AS "NombreCarreras", se."VarNombreSedes" AS "NombreSede", ie."VarNombreInstitucionEducativa" AS "NombreInstitucionEducativa", par."VarNombreParroquia" AS "NombreParroquia", can."VarNombreCanton" AS "NombreCanton", pro."VarNombreProvincia" AS "NombreProvincia" FROM "TblCarrerasSedes" carrese
INNER JOIN "TblSedes" se ON se."VarIdentificadorSedes" = carrese."VarIdentificadorSedes"
INNER JOIN "TblInstitucionEducativa" ie ON ie."VarIdentificadorInstitucionEducativa" = se."VarIdentificadorInstitucionEducativa"
INNER JOIN "TblParroquia" par ON par."VarIdentificadorParroquia" = se."VarIdentificadorParroquia"
INNER JOIN "TblCanton" can ON can."VarIdentificadorCanton" = par."VarIdentificadorCanton"
INNER JOIN "TblProvincia" pro ON pro."VarIdentificadorProvincia" = can."VarIdentificadorProvincia"
INNER JOIN "TblCarreras" car ON car."VarIdentificadorCarreras" = carrese."VarIdentificadorCarreras"
WHERE car."VarEstadoCarreras" LIKE 'Activo' AND ie."VarEstadoInstitucionEducativa" LIKE 'Activo' AND se."VarEstadoSedes" LIKE 'Activo' AND par."VarEstadoParroquia" LIKE 'Activo' AND can."VarEstadoCanton" LIKE 'Activo' AND pro."VarEstadoProvincia" LIKE 'Activo'
                    ''')
                resultado = cursor.fetchall()
            except oracledb.Error as err:
                error_obj, = err.args
                print(f"Conexión no exitosa: {error_obj.message}")
    return render_template('/sistema/ver_queries8.html', resultado=resultado)

"""Cerrar sesion"""
@app.route("/logout")
def logout():
    return redirect(url_for('index'))


@login_manager.user_loader
def load_user(user_id):
    return model.usuarios.objects.get(usuario_id=user_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', '8080'))
