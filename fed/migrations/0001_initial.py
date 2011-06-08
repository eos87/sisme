# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Organizacion'
        db.create_table('fed_organizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nombre_corto', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('direccion', self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.date(2011, 6, 8), blank=True)),
            ('no_mingob', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('no_ruc', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('no_inss', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('representante_legal', self.gf('django.db.models.fields.CharField')(default='', max_length=120, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(default='', max_length=15, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(default='email@example.com', max_length=75, blank=True)),
            ('contacto', self.gf('django.db.models.fields.CharField')(default='', max_length=120, blank=True)),
            ('telefono_contacto', self.gf('django.db.models.fields.CharField')(default='', max_length=15, blank=True)),
            ('sitio_web', self.gf('django.db.models.fields.URLField')(default='www.example.com', max_length=200, blank=True)),
            ('obj_gral', self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True)),
            ('estrategias', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('antecedentes', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('fed', ['Organizacion'])

        # Adding model 'Donante'
        db.create_table('fed_donante', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nombre_corto', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal('fed', ['Donante'])

        # Adding model 'Tema'
        db.create_table('fed_tema', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('fed', ['Tema'])

        # Adding model 'Proyecto'
        db.create_table('fed_proyecto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fed.Organizacion'])),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('nombre', self.gf('django.db.models.fields.TextField')()),
            ('modalidad', self.gf('django.db.models.fields.IntegerField')()),
            ('cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')(default=datetime.date(2011, 6, 8))),
            ('fecha_fin', self.gf('django.db.models.fields.DateField')(default=datetime.date(2011, 6, 8))),
            ('monto_fed', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('monto_contrapartida', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('monto_otros', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
        ))
        db.send_create_signal('fed', ['Proyecto'])

        # Adding M2M table for field otros_donantes on 'Proyecto'
        db.create_table('fed_proyecto_otros_donantes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm['fed.proyecto'], null=False)),
            ('donante', models.ForeignKey(orm['fed.donante'], null=False))
        ))
        db.create_unique('fed_proyecto_otros_donantes', ['proyecto_id', 'donante_id'])


    def backwards(self, orm):
        
        # Deleting model 'Organizacion'
        db.delete_table('fed_organizacion')

        # Deleting model 'Donante'
        db.delete_table('fed_donante')

        # Deleting model 'Tema'
        db.delete_table('fed_tema')

        # Deleting model 'Proyecto'
        db.delete_table('fed_proyecto')

        # Removing M2M table for field otros_donantes on 'Proyecto'
        db.delete_table('fed_proyecto_otros_donantes')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'fed.donante': {
            'Meta': {'object_name': 'Donante'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'fed.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            'antecedentes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'contacto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '120', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "'email@example.com'", 'max_length': '75', 'blank': 'True'}),
            'estrategias': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2011, 6, 8)', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_inss': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'no_mingob': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'no_ruc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'obj_gral': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '120', 'blank': 'True'}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'default': "'www.example.com'", 'max_length': '200', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'telefono_contacto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'fed.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'fecha_fin': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2011, 6, 8)'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2011, 6, 8)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modalidad': ('django.db.models.fields.IntegerField', [], {}),
            'monto_contrapartida': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'monto_fed': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'monto_otros': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.TextField', [], {}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Organizacion']"}),
            'otros_donantes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fed.Donante']", 'null': 'True', 'blank': 'True'})
        },
        'fed.tema': {
            'Meta': {'object_name': 'Tema'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['fed']
