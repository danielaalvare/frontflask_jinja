# =========================================================
# Proyecto Flask con Jinja2 — CRUD completo
# =========================================================
from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(_name_)

# =========================================================
# "BASE DE DATOS" SIMULADA EN MEMORIA
# =========================================================
productos = [
    {"codigo": "P001", "nombre": "Teclado", "valorunitario": 80000, "stock": 15},
    {"codigo": "P002", "nombre": "Mouse", "valorunitario": 50000, "stock": 25},
]
clientes = []
empresas = []
personas = []
vendedores = []
facturas = []

# =========================================================
# RUTAS GENERALES (Inicio y Acerca)
# =========================================================
@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/acerca")
def acerca():
    return render_template("acerca.html")

# =========================================================
# PRODUCTOS
# =========================================================
@app.route("/productos")
def vista_productos():
    return render_template("productos.html", productos=productos)

@app.route("/crear_producto_form", methods=["POST"])
def crear_producto_form():
    """Crea un producto desde el formulario HTML (nombre igual al tutorial)"""
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    valorunitario = request.form["valorunitario"]
    stock = request.form["stock"]
    productos.append({
        "codigo": codigo,
        "nombre": nombre,
        "valorunitario": valorunitario,
        "stock": stock
    })
    return redirect(url_for("vista_productos"))

@app.route("/eliminar_producto/<string:codigo>", methods=["POST"])
def eliminar_producto_form(codigo):
    """Elimina un producto por código (desde formulario HTML)"""
    global productos
    productos = [p for p in productos if p["codigo"] != codigo]
    return redirect(url_for("vista_productos"))

@app.route("/api/productos")
def api_productos():
    return jsonify(productos)

# =========================================================
# CLIENTES
# =========================================================
@app.route("/clientes")
def vista_clientes():
    return render_template("clientes.html", clientes=clientes)

@app.route("/crear_cliente", methods=["POST"])
def crear_cliente():
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    telefono = request.form["telefono"]
    clientes.append({"codigo": codigo, "nombre": nombre, "correo": correo, "telefono": telefono})
    return redirect(url_for("vista_clientes"))

@app.route("/eliminar_cliente/<string:codigo>", methods=["POST"])
def eliminar_cliente(codigo):
    global clientes
    clientes = [c for c in clientes if c["codigo"] != codigo]
    return redirect(url_for("vista_clientes"))

@app.route("/api/clientes")
def api_clientes():
    return jsonify(clientes)

# =========================================================
# EMPRESAS
# =========================================================
@app.route("/empresas")
def vista_empresas():
    return render_template("empresas.html", empresas=empresas)

@app.route("/crear_empresa", methods=["POST"])
def crear_empresa():
    nit = request.form["nit"]
    nombre = request.form["nombre"]
    direccion = request.form["direccion"]
    telefono = request.form["telefono"]
    empresas.append({"nit": nit, "nombre": nombre, "direccion": direccion, "telefono": telefono})
    return redirect(url_for("vista_empresas"))

@app.route("/eliminar_empresa/<string:nit>", methods=["POST"])
def eliminar_empresa(nit):
    global empresas
    empresas = [e for e in empresas if e["nit"] != nit]
    return redirect(url_for("vista_empresas"))

@app.route("/api/empresas")
def api_empresas():
    return jsonify(empresas)

# =========================================================
# PERSONAS
# =========================================================
@app.route("/personas")
def vista_personas():
    return render_template("personas.html", personas=personas)

@app.route("/crear_persona_form", methods=["POST"])
def crear_persona_form():
    """Mantiene el formato del tutorial (nombre del endpoint con _form)"""
    id = request.form["id"]
    nombre = request.form["nombre"]
    edad = request.form["edad"]
    correo = request.form["correo"]
    personas.append({"id": id, "nombre": nombre, "edad": edad, "correo": correo})
    return redirect(url_for("vista_personas"))

@app.route("/eliminar_persona/<string:id>", methods=["POST"])
def eliminar_persona_form(id):
    global personas
    personas = [p for p in personas if p["id"] != id]
    return redirect(url_for("vista_personas"))

@app.route("/api/personas")
def api_personas():
    return jsonify(personas)

# =========================================================
# VENDEDORES
# =========================================================
@app.route("/vendedores")
def vista_vendedores():
    return render_template("vendedores.html", vendedores=vendedores)

@app.route("/crear_vendedor_form", methods=["POST"])
def crear_vendedor_form():
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    zona = request.form["zona"]
    ventas = request.form["ventas"]
    vendedores.append({"codigo": codigo, "nombre": nombre, "zona": zona, "ventas": ventas})
    return redirect(url_for("vista_vendedores"))

@app.route("/eliminar_vendedor/<string:codigo>", methods=["POST"])
def eliminar_vendedor_form(codigo):
    global vendedores
    vendedores = [v for v in vendedores if v["codigo"] != codigo]
    return redirect(url_for("vista_vendedores"))

@app.route("/api/vendedores")
def api_vendedores():
    return jsonify(vendedores)

# =========================================================
# FACTURAS
# =========================================================
@app.route("/facturas")
def vista_facturas():
    return render_template("facturas.html", facturas=facturas)

@app.route("/crear_factura_form", methods=["POST"])
def crear_factura_form():
    id = request.form["id"]
    cliente = request.form["cliente"]
    producto = request.form["producto"]
    total = request.form["total"]
    facturas.append({"id": id, "cliente": cliente, "producto": producto, "total": total})
    return redirect(url_for("vista_facturas"))

@app.route("/eliminar_factura/<string:id>", methods=["POST"])
def eliminar_factura_form(id):
    global facturas
    facturas = [f for f in facturas if f["id"] != id]
    return redirect(url_for("vista_facturas"))

@app.route("/api/facturas")
def api_facturas():
    return jsonify(facturas)

# =========================================================
# EJECUCIÓN DEL SERVIDOR
# =========================================================
if _name_ == "_main_":
    app.run(debug=True, port=5000)