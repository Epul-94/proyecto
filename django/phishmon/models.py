# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Codigoestadohistorico(models.Model):
    id_codigo = models.AutoField(primary_key=True)
    id_sitio = models.ForeignKey('SitiosPhishing', models.DO_NOTHING, db_column='id_sitio')
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'codigoestadohistorico'


class Comentarios(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_sitio = models.ForeignKey('SitiosPhishing', models.DO_NOTHING, db_column='id_sitio')
    numlinea = models.IntegerField(blank=True, null=True)
    hash = models.CharField(max_length=32, blank=True, null=True)
    tipo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'comentarios'


class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    id_ip = models.ForeignKey('Ipwhois', models.DO_NOTHING, db_column='id_ip', blank=True, null=True)
    entidad = models.CharField(max_length=30, blank=True, null=True)
    kind = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacto'


class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    id_contacto = models.ForeignKey(Contacto, models.DO_NOTHING, db_column='id_contacto', blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dominiowhois(models.Model):
    id_dominio = models.AutoField(primary_key=True)
    domain_name = models.CharField(max_length=50)
    created_on = models.CharField(max_length=30, blank=True, null=True)
    expiration_date = models.CharField(max_length=30, blank=True, null=True)
    last_updated_on = models.CharField(max_length=30, blank=True, null=True)
    registrar = models.CharField(max_length=30, blank=True, null=True)
    url = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dominiowhois'


class Email(models.Model):
    id_email = models.AutoField(primary_key=True)
    id_sitio = models.ForeignKey('SitiosPhishing', models.DO_NOTHING, db_column='id_sitio', blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email'


class Entidades(models.Model):
    id_entidades = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    sector = models.ForeignKey('Sector', models.DO_NOTHING, db_column='sector', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entidades'


class Ipwhois(models.Model):
    id_ip = models.AutoField(primary_key=True)
    asn = models.CharField(max_length=30, blank=True, null=True)
    asn_cidr = models.CharField(max_length=30, blank=True, null=True)
    asn_country_code = models.CharField(max_length=30, blank=True, null=True)
    asn_date = models.CharField(max_length=30, blank=True, null=True)
    asn_registry = models.CharField(max_length=30, blank=True, null=True)
    asn_description = models.CharField(max_length=30, blank=True, null=True)
    ip = models.CharField(unique=True, max_length=15)

    class Meta:
        managed = False
        db_table = 'ipwhois'


class Lineas(models.Model):
    id_linea = models.AutoField(primary_key=True)
    id_sitio = models.ForeignKey('SitiosPhishing', models.DO_NOTHING, db_column='id_sitio')
    numlinea = models.IntegerField(blank=True, null=True)
    hash = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lineas'


class Network(models.Model):
    id_network = models.AutoField(primary_key=True)
    id_ip = models.ForeignKey(Ipwhois, models.DO_NOTHING, db_column='id_ip', blank=True, null=True)
    cidr_field = models.CharField(db_column='cidr_', max_length=30, blank=True, null=True)  # Field renamed because it ended with '_'.
    country = models.CharField(max_length=30, blank=True, null=True)
    end_address = models.CharField(max_length=30, blank=True, null=True)
    handle = models.CharField(max_length=50, blank=True, null=True)
    ip_version = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    parent_handle = models.CharField(max_length=30, blank=True, null=True)
    start_address = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'network'


class Sector(models.Model):
    id_sector = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sector'


class SitiosPhishing(models.Model):
    id_sitio = models.AutoField(primary_key=True)
    url = models.CharField(max_length=100)
    id_ip = models.ForeignKey(Ipwhois, models.DO_NOTHING, db_column='id_ip', blank=True, null=True)
    id_dominio = models.ForeignKey(Dominiowhois, models.DO_NOTHING, db_column='id_dominio', blank=True, null=True)
    nombre_archivo = models.CharField(max_length=50, blank=True, null=True)
    ofuscacion = models.CharField(max_length=10, blank=True, null=True)
    md5_archivo = models.CharField(max_length=32, blank=True, null=True)
    estado = models.CharField(max_length=25, blank=True, null=True)
    captura = models.CharField(max_length=128, blank=True, null=True)
    captura_dom = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sitios_phishing'


class Telefono(models.Model):
    id_telefono = models.AutoField(primary_key=True)
    id_contacto = models.ForeignKey(Contacto, models.DO_NOTHING, db_column='id_contacto', blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefono'
