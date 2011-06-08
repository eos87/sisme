# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Informe.anio_desde'
        db.add_column('contraparte_informe', 'anio_desde', self.gf('django.db.models.fields.IntegerField')(default=2011), keep_default=False)

        # Adding field 'Informe.mes_desde'
        db.add_column('contraparte_informe', 'mes_desde', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Adding field 'Informe.anio_hasta'
        db.add_column('contraparte_informe', 'anio_hasta', self.gf('django.db.models.fields.IntegerField')(default=2011), keep_default=False)

        # Adding field 'Informe.mes_hasta'
        db.add_column('contraparte_informe', 'mes_hasta', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Informe.anio_desde'
        db.delete_column('contraparte_informe', 'anio_desde')

        # Deleting field 'Informe.mes_desde'
        db.delete_column('contraparte_informe', 'mes_desde')

        # Deleting field 'Informe.anio_hasta'
        db.delete_column('contraparte_informe', 'anio_hasta')

        # Deleting field 'Informe.mes_hasta'
        db.delete_column('contraparte_informe', 'mes_hasta')


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
        'contraparte.informe': {
            'Meta': {'object_name': 'Informe'},
            'anio_desde': ('django.db.models.fields.IntegerField', [], {}),
            'anio_hasta': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes_desde': ('django.db.models.fields.IntegerField', [], {}),
            'mes_hasta': ('django.db.models.fields.IntegerField', [], {}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Organizacion']"}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Proyecto']"})
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
        }
    }

    complete_apps = ['contraparte']
