from peewee import *
import datetime


db = MySQLDatabase('aws_mysql', host='localhost', port=3306, user='root', password='root')

class Producto(Model):
    cod_prod = PrimaryKeyField()
    nombre_prod = CharField()
    inventario = IntegerField()
    presentacion = CharField()
    precio_und = IntegerField()
    desc_promo = IntegerField(default = 0)
    und_vendidas = IntegerField()
    total_venta = IntegerField()
    calif_prom = DoubleField()
    apl_desc = CharField()
    acum_desc = IntegerField()
    id_coment = IntegerField()
    activo = BooleanField(default = True)

    class Meta:
        database = db
        db_table = 'productos'

    def crearTabla():
        if not Producto.table_exists():
            return Producto.create_table()

class Lote(Model):
    id_lote = PrimaryKeyField()
    cod_prod = ForeignKeyField(Producto, related_name='cod_prod')
    cant_lote = IntegerField()

    class Meta:
        database = db
        db_table = 'lotes'

    def crearTabla():
        if not Lote.table_exists():
            return Lote.create_table()

class Usuario(Model):
    id_usuario = PrimaryKeyField()
    cedula = CharField(max_length=50, unique=True)
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    sexo = CharField(max_length=1)
    fecha_nac = DateField()
    direccion = CharField(max_length=250)
    ciudad = CharField(max_length=250)
    acum_compras = DoubleField(default=0)
    n_bonos = IntegerField(default=0)
    username = CharField(max_length=50)
    email = CharField(max_length=250, unique=True)
    password = CharField(max_length=250)
    role = CharField(max_length=50, default='usuario externo')

    class Meta:
        database = db
        db_table = 'usuarios'

    def crearTabla():
        if not Usuario.table_exists():
            Usuario.create_table()


def crearTablas():
    Producto.crearTabla()
    Lote.crearTabla()
    Usuario.crearTabla()
    
# def registrar(usuario, contraseña, email, nombre, apellido, cedula, sexo, fecha_nac, direccion, ciudad):
#     persona = Usuario(
#         username = usuario,
#         password = contraseña,
#         email = email,
#         nombre = nombre,
#         apellido = apellido,
#         cedula = cedula,
#         sexo = sexo,
#         fecha_nac = fecha_nac,
#         direccion = direccion,
#         ciudad = ciudad)
#     persona.save()

# def registroProducto(nombre_prod, inventario, presentacion, precio_und, desc_promo ):
#     producto = Producto(
#         nombre_prod = nombre_prod,
#         inventario = inventario,
#         presentacion = presentacion,
#         precio_und = precio_und,
#         desc_promo = desc_promo)
#     producto.save()

