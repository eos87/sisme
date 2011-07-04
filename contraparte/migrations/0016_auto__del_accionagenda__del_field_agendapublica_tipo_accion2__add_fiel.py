# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'AccionAgenda'
        db.delete_table('contraparte_accionagenda')

        # Deleting field 'AgendaPublica.tipo_accion2'
        db.delete_column('contraparte_agendapublica', 'tipo_accion2')

        # Adding field 'AgendaPublica.tipo_accion'
        db.add_column('contraparte_agendapublica', 'tipo_accion', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'AccionAgenda'
        db.create_table('contraparte_accionagenda', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('contraparte', ['AccionAgenda'])

        # User chose to not deal with backwards NULL issues for 'AgendaPublica.tipo_accion2'
        raise RuntimeError("Cannot reverse this migration. 'AgendaPublica.tipo_accion2' and its values cannot be restored.")

        # Deleting field 'AgendaPublica.tipo_accion'
        db.delete_column('contraparte_agendapublica', 'tipo_accion')


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
        'contraparte.acciondemanda': {
            'Meta': {'object_name': 'AccionDemanda'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'contraparte.accionimplementada': {
            'Meta': {'object_name': 'AccionImplementada'},
            'accion': ('django.db.models.fields.IntegerField', [], {}),
            'estado': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Tema']"})
        },
        'contraparte.accionimpulsada': {
            'Meta': {'object_name': 'AccionImpulsada'},
            'ambito': ('django.db.models.fields.IntegerField', [], {}),
            'hombres': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Tema']"}),
            'tipo_accion': ('django.db.models.fields.IntegerField', [], {})
        },
        'contraparte.agendapublica': {
            'Meta': {'object_name': 'AgendaPublica'},
            'ambito': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Tema']"}),
            'tipo_accion': ('django.db.models.fields.IntegerField', [], {})
        },
        'contraparte.atencionmujer': {
            'Meta': {'object_name': 'AtencionMujer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'organizacion': ('django.db.models.fields.IntegerField', [], {}),
            'plan_vida': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_poblacion': ('django.db.models.fields.IntegerField', [], {})
        },
        'contraparte.capacidadadmitiva': {
            'Meta': {'object_name': 'CapacidadAdmitiva'},
            'atraves': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ha_mejorado': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"})
        },
        'contraparte.casoatendido': {
            'Meta': {'object_name': 'CasoAtendido'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'situacion_caso': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_caso': ('django.db.models.fields.IntegerField', [], {})
        },
        'contraparte.demandajusticia': {
            'Meta': {'object_name': 'DemandaJusticia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'poblacion_discriminada': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_accion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.AccionDemanda']"})
        },
        'contraparte.denuncia': {
            'Meta': {'object_name': 'Denuncia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'situacion': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_poblacion': ('django.db.models.fields.IntegerField', [], {})
        },
        'contraparte.denunciainterpuesta': {
            'Meta': {'object_name': 'DenunciaInterpuesta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'instancia_administra': ('django.db.models.fields.IntegerField', [], {}),
            'situacion_denuncia': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_denuncia': ('django.db.models.fields.IntegerField', [], {})
        },
        'contraparte.informe': {
            'Meta': {'object_name': 'Informe'},
            'anio': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes': ('django.db.models.fields.IntegerField', [], {}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Organizacion']"}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Proyecto']"})
        },
        'contraparte.masculinidadlibre': {
            'Meta': {'object_name': 'MasculinidadLibre'},
            'hombres': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'segmento_poblacional': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_accion': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_poblacion': ('django.db.models.fields.IntegerField', [], {})
        },
        'contraparte.medirreportar': {
            'Meta': {'object_name': 'MedirReportar'},
            'ha_mejorado': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'manera': ('django.db.models.fields.IntegerField', [], {})
        },
        'contraparte.observatorio': {
            'Meta': {'object_name': 'Observatorio'},
            'accion': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'tipo_observatorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.TipoObservatorio']"})
        },
        'contraparte.participacioncomision': {
            'Meta': {'object_name': 'ParticipacionComision'},
            'ambito': ('django.db.models.fields.IntegerField', [], {}),
            'comision': ('django.db.models.fields.IntegerField', [], {}),
            'estado': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'contraparte.planestrategico': {
            'Meta': {'object_name': 'PlanEstrategico'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'manera': ('django.db.models.fields.IntegerField', [], {}),
            'utiliza_plan': ('django.db.models.fields.IntegerField', [], {})
        },
        'contraparte.poseeninfo': {
            'Meta': {'object_name': 'PoseenInfo'},
            'hom_adols': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hom_adultos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hom_disca_adols': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hom_disca_adultos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hom_disca_jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hom_disca_ninos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hom_etnia_adols': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hom_etnia_adultos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hom_etnia_jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hom_etnia_ninos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hom_jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hom_ninos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hom_vih_adols': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hom_vih_adultos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hom_vih_jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hom_vih_ninos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'lgbt_gay': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lgbt_hsh': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lgbt_lesbi': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lgbt_trans': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_adols': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_adultas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_disca_adols': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_disca_adultas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_disca_jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_disca_ninas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_etnia_adols': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_etnia_adultas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_etnia_jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_etnia_ninas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_ninas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_vih_adols': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_vih_adultas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_vih_jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'muj_vih_ninas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Tema']"}),
            'tipo_accion': ('django.db.models.fields.IntegerField', [], {})
        },
        'contraparte.prevencionvbg': {
            'Meta': {'object_name': 'PrevencionVBG'},
            'hombres': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'segmento_poblacional': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_accion': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_poblacion': ('django.db.models.fields.IntegerField', [], {})
        },
        'contraparte.recibeninfo': {
            'Meta': {'object_name': 'RecibenInfo'},
            'hombres': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'segmento_poblacional': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_accion': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_poblacion': ('django.db.models.fields.IntegerField', [], {})
        },
        'contraparte.referenciacontrareferencia': {
            'Meta': {'object_name': 'ReferenciaContraReferencia'},
            'atendido_personal_pertinente': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'instancia': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_referencia': ('django.db.models.fields.IntegerField', [], {})
        },
        'contraparte.tipoobservatorio': {
            'Meta': {'object_name': 'TipoObservatorio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
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
            'contacto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '120', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "'email@example.com'", 'max_length': '75', 'blank': 'True'}),
            'estrategias': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2011, 7, 4)', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_inss': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'no_mingob': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'no_ruc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'obj_gral': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '120', 'blank': 'True'}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'default': "'www.example.com'", 'max_length': '200', 'blank': 'True'}),
            'telefono_1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'telefono_2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'telefono_contacto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'fed.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'fecha_fin': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2011, 7, 4)'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2011, 7, 4)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modalidad': ('django.db.models.fields.IntegerField', [], {}),
            'monto_contrapartida': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '30', 'decimal_places': '2', 'blank': 'True'}),
            'monto_fed': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '30', 'decimal_places': '2', 'blank': 'True'}),
            'monto_otros': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '30', 'decimal_places': '2', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.TextField', [], {}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Organizacion']"}),
            'otros_donantes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fed.Donante']", 'null': 'True', 'blank': 'True'}),
            'resultados': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fed.Resultado']", 'null': 'True', 'blank': 'True'})
        },
        'fed.resultado': {
            'Meta': {'object_name': 'Resultado'},
            'codigo': ('django.db.models.fields.IntegerField', [], {}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        'fed.tema': {
            'Meta': {'object_name': 'Tema'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contraparte']
