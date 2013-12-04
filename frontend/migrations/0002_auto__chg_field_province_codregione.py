# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Province.codregione'
        db.alter_column('province', 'codRegione', self.gf('django.db.models.fields.related.ForeignKey')(max_length=50, db_column='codRegione', to=orm['frontend.Regioni']))
        # Adding index on 'Province', fields ['codregione']
        db.create_index('province', ['codRegione'])


    def backwards(self, orm):
        # Removing index on 'Province', fields ['codregione']
        db.delete_index('province', ['codRegione'])


        # Changing field 'Province.codregione'
        db.alter_column('province', 'codRegione', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='codRegione'))

    models = {
        u'frontend.account': {
            'Meta': {'object_name': 'Account', 'db_table': "'account'"},
            'backup_password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'data_inserimento': ('django.db.models.fields.DateTimeField', [], {}),
            'data_ultima_modifica': ('django.db.models.fields.DateTimeField', [], {}),
            'hashcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'password': ('django.db.models.fields.TextField', [], {})
        },
        u'frontend.annunci': {
            'Meta': {'object_name': 'Annunci', 'db_table': "'annunci'"},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'data_inserimento': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_scadenza': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_ultima_modifica': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'descrizione': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'idazienda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Aziende']", 'null': 'True', 'db_column': "'idAzienda'", 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parametro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tipologia': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'frontend.annuncitagoccorrenze': {
            'Meta': {'object_name': 'AnnunciTagOccorrenze', 'db_table': "'annunci_tag_occorrenze'"},
            'homepage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'primary_key': 'True', 'db_column': "'idTag'"}),
            'livello': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'frontend.annuncitagoccorrenzecomuni': {
            'Meta': {'object_name': 'AnnunciTagOccorrenzeComuni', 'db_table': "'annunci_tag_occorrenze_comuni'"},
            'codprovincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Province']", 'db_column': "'codProvincia'"}),
            'comune': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'frontend.annuncitagoccorrenzeprovince': {
            'Meta': {'object_name': 'AnnunciTagOccorrenzeProvince', 'db_table': "'annunci_tag_occorrenze_province'"},
            'codprovincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Province']", 'db_column': "'codProvincia'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'frontend.annuncitagoccorrenzeregioni': {
            'Meta': {'object_name': 'AnnunciTagOccorrenzeRegioni', 'db_table': "'annunci_tag_occorrenze_regioni'"},
            'codregione': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Regioni']", 'db_column': "'codRegione'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'frontend.annuncitags': {
            'Meta': {'object_name': 'AnnunciTags', 'db_table': "'annunci_tags'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idannuncio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Annunci']", 'db_column': "'idAnnuncio'"}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"})
        },
        u'frontend.aziende': {
            'Meta': {'object_name': 'Aziende', 'db_table': "'aziende'"},
            'backup_password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bonus_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'codice_analytics': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'codprovincia': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'codProvincia'", 'blank': 'True'}),
            'codregione': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'codRegione'", 'blank': 'True'}),
            'comune': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'data_inserimento': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_ultima_modifica': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_update_kassy': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'descrizione_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'hashcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'hotfrog_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'indirizzo_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'indirizzo_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'indirizzo_3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'invio_dem': ('django.db.models.fields.IntegerField', [], {}),
            'invio_dem_diretto': ('django.db.models.fields.IntegerField', [], {}),
            'invio_dem_tramite_reedbusiness': ('django.db.models.fields.IntegerField', [], {}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'localita': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parametro': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'blank': 'True'}),
            'password': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'privacy': ('django.db.models.fields.IntegerField', [], {}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'richiamabile': ('django.db.models.fields.IntegerField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['frontend.Tags']", 'through': u"orm['frontend.AziendeTags']", 'symmetrical': 'False'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'frontend.aziendecontatti': {
            'Meta': {'object_name': 'AziendeContatti', 'db_table': "'aziende_contatti'"},
            'data_ora': ('django.db.models.fields.DateTimeField', [], {}),
            'email_mittente': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'idazienda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Aziende']", 'db_column': "'idAzienda'"}),
            'idelemento': ('django.db.models.fields.IntegerField', [], {'db_column': "'idElemento'"}),
            'letto': ('django.db.models.fields.IntegerField', [], {}),
            'messaggio': ('django.db.models.fields.TextField', [], {}),
            'nome_mittente': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipologia': ('django.db.models.fields.IntegerField', [], {}),
            'visibile': ('django.db.models.fields.IntegerField', [], {})
        },
        u'frontend.aziendeeliminate': {
            'Meta': {'object_name': 'AziendeEliminate', 'db_table': "'aziende_eliminate'"},
            'codprovincia': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'codProvincia'"}),
            'comune': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'data_eliminazione': ('django.db.models.fields.DateTimeField', [], {}),
            'idazienda': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idAzienda'"}),
            'indirizzo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'frontend.aziendeprovinceregioni': {
            'Meta': {'object_name': 'AziendeProvinceRegioni', 'db_table': "'aziende_province_regioni'"},
            'azienda': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'comune': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'descrizione_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'regione': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '202', 'blank': 'True'})
        },
        u'frontend.aziendetags': {
            'Meta': {'object_name': 'AziendeTags', 'db_table': "'aziende_tags'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idazienda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Aziende']", 'db_column': "'idAzienda'"}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"})
        },
        u'frontend.comuniitaliani': {
            'Meta': {'object_name': 'ComuniItaliani', 'db_table': "'comuni_italiani'"},
            'cap': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'CAP'"}),
            'codprovincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Province']", 'db_column': "'codProvincia'"}),
            'codregione': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Regioni']", 'db_column': "'codRegione'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parametro': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'frontend.faq': {
            'Meta': {'object_name': 'Faq', 'db_table': "'faq'"},
            'domanda': ('django.db.models.fields.TextField', [], {}),
            'gruppo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'idlingua': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_column': "'idLingua'"}),
            'ordine': ('django.db.models.fields.IntegerField', [], {}),
            'risposta': ('django.db.models.fields.TextField', [], {})
        },
        u'frontend.lingue': {
            'Meta': {'object_name': 'Lingue', 'db_table': "'lingue'"},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'frontend.macrocategorie': {
            'Meta': {'object_name': 'Macrocategorie', 'db_table': "'macrocategorie'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'id_dbi': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'frontend.meta': {
            'Meta': {'object_name': 'Meta', 'db_table': "'meta'"},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'geo': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pagina': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'paginazione': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'versione': ('django.db.models.fields.IntegerField', [], {})
        },
        u'frontend.news': {
            'Meta': {'object_name': 'News', 'db_table': "'news'"},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'data': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_inserimento': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_ultima_modifica': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'descrizione': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'idazienda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Aziende']", 'null': 'True', 'db_column': "'idAzienda'", 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parametro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'frontend.newstagoccorrenze': {
            'Meta': {'object_name': 'NewsTagOccorrenze', 'db_table': "'news_tag_occorrenze'"},
            'homepage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'primary_key': 'True', 'db_column': "'idTag'"}),
            'livello': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'frontend.newstagoccorrenzecomuni': {
            'Meta': {'object_name': 'NewsTagOccorrenzeComuni', 'db_table': "'news_tag_occorrenze_comuni'"},
            'codprovincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Province']", 'db_column': "'codProvincia'"}),
            'comune': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'frontend.newstagoccorrenzeprovince': {
            'Meta': {'object_name': 'NewsTagOccorrenzeProvince', 'db_table': "'news_tag_occorrenze_province'"},
            'codprovincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Province']", 'db_column': "'codProvincia'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'frontend.newstagoccorrenzeregioni': {
            'Meta': {'object_name': 'NewsTagOccorrenzeRegioni', 'db_table': "'news_tag_occorrenze_regioni'"},
            'codregione': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Regioni']", 'db_column': "'codRegione'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'frontend.newstags': {
            'Meta': {'object_name': 'NewsTags', 'db_table': "'news_tags'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idnews': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.News']", 'db_column': "'idNews'"}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"})
        },
        u'frontend.prodotti': {
            'Meta': {'object_name': 'Prodotti', 'db_table': "'prodotti'"},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'data_inserimento': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_ultima_modifica': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'descrizione': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'idazienda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Aziende']", 'null': 'True', 'db_column': "'idAzienda'", 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nome_originale_pdf': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parametro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'frontend.prodottitagoccorrenze': {
            'Meta': {'object_name': 'ProdottiTagOccorrenze', 'db_table': "'prodotti_tag_occorrenze'"},
            'homepage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'primary_key': 'True', 'db_column': "'idTag'"}),
            'livello': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'frontend.prodottitagoccorrenzecomuni': {
            'Meta': {'object_name': 'ProdottiTagOccorrenzeComuni', 'db_table': "'prodotti_tag_occorrenze_comuni'"},
            'codprovincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Province']", 'db_column': "'codProvincia'"}),
            'comune': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'frontend.prodottitagoccorrenzeprovince': {
            'Meta': {'object_name': 'ProdottiTagOccorrenzeProvince', 'db_table': "'prodotti_tag_occorrenze_province'"},
            'codprovincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Province']", 'db_column': "'codProvincia'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'frontend.prodottitagoccorrenzeregioni': {
            'Meta': {'object_name': 'ProdottiTagOccorrenzeRegioni', 'db_table': "'prodotti_tag_occorrenze_regioni'"},
            'codregione': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Regioni']", 'db_column': "'codRegione'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'frontend.prodottitags': {
            'Meta': {'object_name': 'ProdottiTags', 'db_table': "'prodotti_tags'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idprodotto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Prodotti']", 'db_column': "'idProdotto'"}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"})
        },
        u'frontend.province': {
            'Meta': {'object_name': 'Province', 'db_table': "'province'"},
            'codprovincia': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True', 'db_column': "'codProvincia'"}),
            'codregione': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'province'", 'max_length': '50', 'db_column': "'codRegione'", 'to': u"orm['frontend.Regioni']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parametro': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'frontend.regioni': {
            'Meta': {'object_name': 'Regioni', 'db_table': "'regioni'"},
            'codregione': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True', 'db_column': "'codRegione'"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parametro': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'frontend.registrazioni': {
            'Meta': {'object_name': 'Registrazioni', 'db_table': "'registrazioni'"},
            'backup_password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cap': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'codprovincia': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'codProvincia'", 'blank': 'True'}),
            'comune': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'conferma_reed': ('django.db.models.fields.IntegerField', [], {}),
            'data_ultima_modifica': ('django.db.models.fields.DateTimeField', [], {}),
            'descrizione_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email_login': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'hashcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'idazienda': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'idAzienda'", 'blank': 'True'}),
            'indirizzo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'invio_dem': ('django.db.models.fields.IntegerField', [], {}),
            'invio_dem_diretto': ('django.db.models.fields.IntegerField', [], {}),
            'invio_dem_tramite_reedbusiness': ('django.db.models.fields.IntegerField', [], {}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'password': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'privacy': ('django.db.models.fields.IntegerField', [], {}),
            'step': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'frontend.registrazioniservizi': {
            'Meta': {'object_name': 'RegistrazioniServizi', 'db_table': "'registrazioni_servizi'"},
            'cod_provincia': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'conclusa': ('django.db.models.fields.IntegerField', [], {}),
            'data_inserimento': ('django.db.models.fields.DateTimeField', [], {}),
            'email_login': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'id_azienda': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id_codice_sconto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id_ordine': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id_servizio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id_servizio_acquistato': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id_tipo_pagamento': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id_tipo_servizio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'invio_dem': ('django.db.models.fields.IntegerField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.TextField', [], {}),
            'step': ('django.db.models.fields.IntegerField', [], {})
        },
        u'frontend.registrazioniservizitag': {
            'Meta': {'object_name': 'RegistrazioniServiziTag', 'db_table': "'registrazioni_servizi_tag'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_registrazione_servizio': ('django.db.models.fields.IntegerField', [], {}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'frontend.registrazionitag': {
            'Meta': {'object_name': 'RegistrazioniTag', 'db_table': "'registrazioni_tag'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'idregistrazione': ('django.db.models.fields.IntegerField', [], {'db_column': "'idRegistrazione'"}),
            'idtag': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'idTag'", 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'frontend.settori': {
            'Meta': {'object_name': 'Settori', 'db_table': "'settori'"},
            'data_inserimento': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_ultima_modifica': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'descrizione': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parametro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'frontend.settoritags': {
            'Meta': {'object_name': 'SettoriTags', 'db_table': "'settori_tags'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'idsettore': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Settori']", 'null': 'True', 'db_column': "'idSettore'", 'blank': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'null': 'True', 'db_column': "'idTag'", 'blank': 'True'})
        },
        u'frontend.stopwords': {
            'Meta': {'object_name': 'Stopwords', 'db_table': "'stopwords'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'stopword': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'frontend.taglegami': {
            'Meta': {'object_name': 'TagLegami', 'db_table': "'tag_legami'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtag_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tag1'", 'db_column': "'idTag_1'", 'to': u"orm['frontend.Tags']"}),
            'idtag_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tag2'", 'db_column': "'idTag_2'", 'to': u"orm['frontend.Tags']"}),
            'legame': ('django.db.models.fields.IntegerField', [], {}),
            'legame_percent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'frontend.tagmaxlegame': {
            'Meta': {'object_name': 'TagMaxLegame', 'db_table': "'tag_max_legame'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtag_1': ('django.db.models.fields.IntegerField', [], {'db_column': "'idTag_1'"}),
            'massimo': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'frontend.tagoccorrenze': {
            'Meta': {'object_name': 'TagOccorrenze', 'db_table': "'tag_occorrenze'"},
            'homepage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'primary_key': 'True', 'db_column': "'idTag'"}),
            'livello': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'frontend.tags': {
            'Meta': {'object_name': 'Tags', 'db_table': "'tags'"},
            'classification': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'data_inserimento': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_ultima_modifica': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'hotfrog_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'parametro': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'frontend.video': {
            'Meta': {'object_name': 'Video', 'db_table': "'video'"},
            'abstract': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'data_inserimento': ('django.db.models.fields.DateTimeField', [], {}),
            'data_ultima_modifica': ('django.db.models.fields.DateTimeField', [], {}),
            'descrizione': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'idazienda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Aziende']", 'db_column': "'idAzienda'"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parametro': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sorgente': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'frontend.videotagoccorrenze': {
            'Meta': {'object_name': 'VideoTagOccorrenze', 'db_table': "'video_tag_occorrenze'"},
            'homepage': ('django.db.models.fields.IntegerField', [], {}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'primary_key': 'True', 'db_column': "'idTag'"}),
            'livello': ('django.db.models.fields.IntegerField', [], {}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {})
        },
        u'frontend.videotagoccorrenzecomuni': {
            'Meta': {'object_name': 'VideoTagOccorrenzeComuni', 'db_table': "'video_tag_occorrenze_comuni'"},
            'codprovincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Province']", 'db_column': "'codProvincia'"}),
            'comune': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {})
        },
        u'frontend.videotagoccorrenzeprovince': {
            'Meta': {'object_name': 'VideoTagOccorrenzeProvince', 'db_table': "'video_tag_occorrenze_province'"},
            'codprovincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Province']", 'db_column': "'codProvincia'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {})
        },
        u'frontend.videotagoccorrenzeregioni': {
            'Meta': {'object_name': 'VideoTagOccorrenzeRegioni', 'db_table': "'video_tag_occorrenze_regioni'"},
            'codregione': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Regioni']", 'db_column': "'codRegione'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"}),
            'occorrenze': ('django.db.models.fields.IntegerField', [], {})
        },
        u'frontend.videotags': {
            'Meta': {'object_name': 'VideoTags', 'db_table': "'video_tags'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idtag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Tags']", 'db_column': "'idTag'"}),
            'idvideo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Video']", 'db_column': "'idVideo'"})
        }
    }

    complete_apps = ['frontend']