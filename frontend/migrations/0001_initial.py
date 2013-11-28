# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table('account', (
            ('login', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('password', self.gf('django.db.models.fields.TextField')()),
            ('backup_password', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('hashcode', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('data_inserimento', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_ultima_modifica', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'frontend', ['Account'])

        # Adding model 'Annunci'
        db.create_table('annunci', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('idazienda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Aziende'], null=True, db_column='idAzienda', blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('abstract', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('descrizione', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parametro', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('data_inserimento', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('data_ultima_modifica', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('data_scadenza', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('tipologia', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['Annunci'])

        # Adding model 'AnnunciTagOccorrenze'
        db.create_table('annunci_tag_occorrenze', (
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], primary_key=True, db_column='idTag')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('livello', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('homepage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['AnnunciTagOccorrenze'])

        # Adding model 'AnnunciTagOccorrenzeComuni'
        db.create_table('annunci_tag_occorrenze_comuni', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
            ('codprovincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Province'], db_column='codProvincia')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('comune', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'frontend', ['AnnunciTagOccorrenzeComuni'])

        # Adding model 'AnnunciTagOccorrenzeProvince'
        db.create_table('annunci_tag_occorrenze_province', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
            ('codprovincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Province'], db_column='codProvincia')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['AnnunciTagOccorrenzeProvince'])

        # Adding model 'AnnunciTagOccorrenzeRegioni'
        db.create_table('annunci_tag_occorrenze_regioni', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
            ('codregione', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Regioni'], db_column='codRegione')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['AnnunciTagOccorrenzeRegioni'])

        # Adding model 'AnnunciTags'
        db.create_table('annunci_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idannuncio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Annunci'], db_column='idAnnuncio')),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
        ))
        db.send_create_signal(u'frontend', ['AnnunciTags'])

        # Adding model 'Aziende'
        db.create_table('aziende', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('indirizzo_1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('indirizzo_2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('indirizzo_3', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('localita', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('provincia', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('descrizione_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('hotfrog_id', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('login', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('password', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('backup_password', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('data_inserimento', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('data_ultima_modifica', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('data_update_kassy', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('comune', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('codprovincia', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='codProvincia', blank=True)),
            ('parametro', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, blank=True)),
            ('codregione', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='codRegione', blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hashcode', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('richiamabile', self.gf('django.db.models.fields.IntegerField')()),
            ('bonus_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('invio_dem_diretto', self.gf('django.db.models.fields.IntegerField')()),
            ('invio_dem', self.gf('django.db.models.fields.IntegerField')()),
            ('codice_analytics', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('invio_dem_tramite_reedbusiness', self.gf('django.db.models.fields.IntegerField')()),
            ('privacy', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'frontend', ['Aziende'])

        # Adding model 'AziendeContatti'
        db.create_table('aziende_contatti', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('idazienda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Aziende'], db_column='idAzienda')),
            ('idelemento', self.gf('django.db.models.fields.IntegerField')(db_column='idElemento')),
            ('tipologia', self.gf('django.db.models.fields.IntegerField')()),
            ('nome_mittente', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email_mittente', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('messaggio', self.gf('django.db.models.fields.TextField')()),
            ('letto', self.gf('django.db.models.fields.IntegerField')()),
            ('data_ora', self.gf('django.db.models.fields.DateTimeField')()),
            ('visibile', self.gf('django.db.models.fields.IntegerField')()),
            ('referer', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'frontend', ['AziendeContatti'])

        # Adding model 'AziendeEliminate'
        db.create_table('aziende_eliminate', (
            ('idazienda', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idAzienda')),
            ('referer', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('data_eliminazione', self.gf('django.db.models.fields.DateTimeField')()),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('indirizzo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('comune', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('codprovincia', self.gf('django.db.models.fields.CharField')(max_length=255, db_column='codProvincia')),
        ))
        db.send_create_signal(u'frontend', ['AziendeEliminate'])

        # Adding model 'AziendeProvinceRegioni'
        db.create_table('aziende_province_regioni', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=202, blank=True)),
            ('azienda', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('descrizione_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('comune', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('provincia', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('regione', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'frontend', ['AziendeProvinceRegioni'])

        # Adding model 'AziendeTags'
        db.create_table('aziende_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idazienda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Aziende'], db_column='idAzienda')),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
        ))
        db.send_create_signal(u'frontend', ['AziendeTags'])

        # Adding model 'ComuniItaliani'
        db.create_table('comuni_italiani', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('codprovincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Province'], db_column='codProvincia')),
            ('codregione', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Regioni'], db_column='codRegione')),
            ('cap', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='CAP')),
            ('parametro', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['ComuniItaliani'])

        # Adding model 'Faq'
        db.create_table('faq', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('idlingua', self.gf('django.db.models.fields.CharField')(max_length=2, db_column='idLingua')),
            ('gruppo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('domanda', self.gf('django.db.models.fields.TextField')()),
            ('risposta', self.gf('django.db.models.fields.TextField')()),
            ('ordine', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'frontend', ['Faq'])

        # Adding model 'Lingue'
        db.create_table('lingue', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['Lingue'])

        # Adding model 'Macrocategorie'
        db.create_table('macrocategorie', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('id_dbi', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['Macrocategorie'])

        # Adding model 'Meta'
        db.create_table('meta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pagina', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geo', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('paginazione', self.gf('django.db.models.fields.IntegerField')()),
            ('versione', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'frontend', ['Meta'])

        # Adding model 'News'
        db.create_table('news', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('idazienda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Aziende'], null=True, db_column='idAzienda', blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('abstract', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('descrizione', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parametro', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('data', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('data_inserimento', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('data_ultima_modifica', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['News'])

        # Adding model 'NewsTagOccorrenze'
        db.create_table('news_tag_occorrenze', (
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], primary_key=True, db_column='idTag')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('livello', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('homepage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['NewsTagOccorrenze'])

        # Adding model 'NewsTagOccorrenzeComuni'
        db.create_table('news_tag_occorrenze_comuni', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
            ('codprovincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Province'], db_column='codProvincia')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('comune', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'frontend', ['NewsTagOccorrenzeComuni'])

        # Adding model 'NewsTagOccorrenzeProvince'
        db.create_table('news_tag_occorrenze_province', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
            ('codprovincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Province'], db_column='codProvincia')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['NewsTagOccorrenzeProvince'])

        # Adding model 'NewsTagOccorrenzeRegioni'
        db.create_table('news_tag_occorrenze_regioni', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
            ('codregione', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Regioni'], db_column='codRegione')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['NewsTagOccorrenzeRegioni'])

        # Adding model 'NewsTags'
        db.create_table('news_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idnews', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.News'], db_column='idNews')),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
        ))
        db.send_create_signal(u'frontend', ['NewsTags'])

        # Adding model 'Prodotti'
        db.create_table('prodotti', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('idazienda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Aziende'], null=True, db_column='idAzienda', blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('abstract', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('descrizione', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parametro', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('data_inserimento', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('data_ultima_modifica', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('nome_originale_pdf', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'frontend', ['Prodotti'])

        # Adding model 'ProdottiTagOccorrenze'
        db.create_table('prodotti_tag_occorrenze', (
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], primary_key=True, db_column='idTag')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('livello', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('homepage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['ProdottiTagOccorrenze'])

        # Adding model 'ProdottiTagOccorrenzeComuni'
        db.create_table('prodotti_tag_occorrenze_comuni', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
            ('codprovincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Province'], db_column='codProvincia')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('comune', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'frontend', ['ProdottiTagOccorrenzeComuni'])

        # Adding model 'ProdottiTagOccorrenzeProvince'
        db.create_table('prodotti_tag_occorrenze_province', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
            ('codprovincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Province'], db_column='codProvincia')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['ProdottiTagOccorrenzeProvince'])

        # Adding model 'ProdottiTagOccorrenzeRegioni'
        db.create_table('prodotti_tag_occorrenze_regioni', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
            ('codregione', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Regioni'], db_column='codRegione')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['ProdottiTagOccorrenzeRegioni'])

        # Adding model 'ProdottiTags'
        db.create_table('prodotti_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idprodotto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Prodotti'], db_column='idProdotto')),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
        ))
        db.send_create_signal(u'frontend', ['ProdottiTags'])

        # Adding model 'Province'
        db.create_table('province', (
            ('codprovincia', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True, db_column='codProvincia')),
            ('codregione', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='codRegione')),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('parametro', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['Province'])

        # Adding model 'Regioni'
        db.create_table('regioni', (
            ('codregione', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True, db_column='codRegione')),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('parametro', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['Regioni'])

        # Adding model 'Registrazioni'
        db.create_table('registrazioni', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('idazienda', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='idAzienda', blank=True)),
            ('step', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('indirizzo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('comune', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('codprovincia', self.gf('django.db.models.fields.CharField')(max_length=255, db_column='codProvincia', blank=True)),
            ('cap', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('descrizione_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('email_login', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('password', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('backup_password', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('hashcode', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('data_ultima_modifica', self.gf('django.db.models.fields.DateTimeField')()),
            ('conferma_reed', self.gf('django.db.models.fields.IntegerField')()),
            ('privacy', self.gf('django.db.models.fields.IntegerField')()),
            ('invio_dem', self.gf('django.db.models.fields.IntegerField')()),
            ('invio_dem_tramite_reedbusiness', self.gf('django.db.models.fields.IntegerField')()),
            ('invio_dem_diretto', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'frontend', ['Registrazioni'])

        # Adding model 'RegistrazioniServizi'
        db.create_table('registrazioni_servizi', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('id_tipo_servizio', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('id_servizio', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('step', self.gf('django.db.models.fields.IntegerField')()),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cod_provincia', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('email_login', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('password', self.gf('django.db.models.fields.TextField')()),
            ('conclusa', self.gf('django.db.models.fields.IntegerField')()),
            ('id_tipo_pagamento', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('id_codice_sconto', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('data_inserimento', self.gf('django.db.models.fields.DateTimeField')()),
            ('id_servizio_acquistato', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('id_ordine', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('id_azienda', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('invio_dem', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'frontend', ['RegistrazioniServizi'])

        # Adding model 'RegistrazioniServiziTag'
        db.create_table('registrazioni_servizi_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_registrazione_servizio', self.gf('django.db.models.fields.IntegerField')()),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'frontend', ['RegistrazioniServiziTag'])

        # Adding model 'RegistrazioniTag'
        db.create_table('registrazioni_tag', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('idregistrazione', self.gf('django.db.models.fields.IntegerField')(db_column='idRegistrazione')),
            ('idtag', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='idTag', blank=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['RegistrazioniTag'])

        # Adding model 'Settori'
        db.create_table('settori', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('descrizione', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('parametro', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('data_inserimento', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('data_ultima_modifica', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['Settori'])

        # Adding model 'SettoriTags'
        db.create_table('settori_tags', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('idsettore', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Settori'], null=True, db_column='idSettore', blank=True)),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], null=True, db_column='idTag', blank=True)),
        ))
        db.send_create_signal(u'frontend', ['SettoriTags'])

        # Adding model 'Stopwords'
        db.create_table('stopwords', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('stopword', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['Stopwords'])

        # Adding model 'TagLegami'
        db.create_table('tag_legami', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idtag_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tag1', db_column='idTag_1', to=orm['frontend.Tags'])),
            ('idtag_2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tag2', db_column='idTag_2', to=orm['frontend.Tags'])),
            ('legame', self.gf('django.db.models.fields.IntegerField')()),
            ('legame_percent', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['TagLegami'])

        # Adding model 'TagMaxLegame'
        db.create_table('tag_max_legame', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idtag_1', self.gf('django.db.models.fields.IntegerField')(db_column='idTag_1')),
            ('massimo', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['TagMaxLegame'])

        # Adding model 'TagOccorrenze'
        db.create_table('tag_occorrenze', (
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], primary_key=True, db_column='idTag')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('livello', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('homepage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['TagOccorrenze'])

        # Adding model 'Tags'
        db.create_table('tags', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('hotfrog_id', self.gf('django.db.models.fields.IntegerField')()),
            ('parametro', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, blank=True)),
            ('data_inserimento', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('data_ultima_modifica', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('classification', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['Tags'])

        # Adding model 'Video'
        db.create_table('video', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('idazienda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Aziende'], db_column='idAzienda')),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abstract', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('descrizione', self.gf('django.db.models.fields.TextField')()),
            ('parametro', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('data_inserimento', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_ultima_modifica', self.gf('django.db.models.fields.DateTimeField')()),
            ('youtube_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sorgente', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'frontend', ['Video'])

        # Adding model 'VideoTagOccorrenze'
        db.create_table('video_tag_occorrenze', (
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], primary_key=True, db_column='idTag')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')()),
            ('livello', self.gf('django.db.models.fields.IntegerField')()),
            ('homepage', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'frontend', ['VideoTagOccorrenze'])

        # Adding model 'VideoTagOccorrenzeComuni'
        db.create_table('video_tag_occorrenze_comuni', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
            ('codprovincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Province'], db_column='codProvincia')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')()),
            ('comune', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'frontend', ['VideoTagOccorrenzeComuni'])

        # Adding model 'VideoTagOccorrenzeProvince'
        db.create_table('video_tag_occorrenze_province', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
            ('codprovincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Province'], db_column='codProvincia')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'frontend', ['VideoTagOccorrenzeProvince'])

        # Adding model 'VideoTagOccorrenzeRegioni'
        db.create_table('video_tag_occorrenze_regioni', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
            ('codregione', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Regioni'], db_column='codRegione')),
            ('occorrenze', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'frontend', ['VideoTagOccorrenzeRegioni'])

        # Adding model 'VideoTags'
        db.create_table('video_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idvideo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Video'], db_column='idVideo')),
            ('idtag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tags'], db_column='idTag')),
        ))
        db.send_create_signal(u'frontend', ['VideoTags'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table('account')

        # Deleting model 'Annunci'
        db.delete_table('annunci')

        # Deleting model 'AnnunciTagOccorrenze'
        db.delete_table('annunci_tag_occorrenze')

        # Deleting model 'AnnunciTagOccorrenzeComuni'
        db.delete_table('annunci_tag_occorrenze_comuni')

        # Deleting model 'AnnunciTagOccorrenzeProvince'
        db.delete_table('annunci_tag_occorrenze_province')

        # Deleting model 'AnnunciTagOccorrenzeRegioni'
        db.delete_table('annunci_tag_occorrenze_regioni')

        # Deleting model 'AnnunciTags'
        db.delete_table('annunci_tags')

        # Deleting model 'Aziende'
        db.delete_table('aziende')

        # Deleting model 'AziendeContatti'
        db.delete_table('aziende_contatti')

        # Deleting model 'AziendeEliminate'
        db.delete_table('aziende_eliminate')

        # Deleting model 'AziendeProvinceRegioni'
        db.delete_table('aziende_province_regioni')

        # Deleting model 'AziendeTags'
        db.delete_table('aziende_tags')

        # Deleting model 'ComuniItaliani'
        db.delete_table('comuni_italiani')

        # Deleting model 'Faq'
        db.delete_table('faq')

        # Deleting model 'Lingue'
        db.delete_table('lingue')

        # Deleting model 'Macrocategorie'
        db.delete_table('macrocategorie')

        # Deleting model 'Meta'
        db.delete_table('meta')

        # Deleting model 'News'
        db.delete_table('news')

        # Deleting model 'NewsTagOccorrenze'
        db.delete_table('news_tag_occorrenze')

        # Deleting model 'NewsTagOccorrenzeComuni'
        db.delete_table('news_tag_occorrenze_comuni')

        # Deleting model 'NewsTagOccorrenzeProvince'
        db.delete_table('news_tag_occorrenze_province')

        # Deleting model 'NewsTagOccorrenzeRegioni'
        db.delete_table('news_tag_occorrenze_regioni')

        # Deleting model 'NewsTags'
        db.delete_table('news_tags')

        # Deleting model 'Prodotti'
        db.delete_table('prodotti')

        # Deleting model 'ProdottiTagOccorrenze'
        db.delete_table('prodotti_tag_occorrenze')

        # Deleting model 'ProdottiTagOccorrenzeComuni'
        db.delete_table('prodotti_tag_occorrenze_comuni')

        # Deleting model 'ProdottiTagOccorrenzeProvince'
        db.delete_table('prodotti_tag_occorrenze_province')

        # Deleting model 'ProdottiTagOccorrenzeRegioni'
        db.delete_table('prodotti_tag_occorrenze_regioni')

        # Deleting model 'ProdottiTags'
        db.delete_table('prodotti_tags')

        # Deleting model 'Province'
        db.delete_table('province')

        # Deleting model 'Regioni'
        db.delete_table('regioni')

        # Deleting model 'Registrazioni'
        db.delete_table('registrazioni')

        # Deleting model 'RegistrazioniServizi'
        db.delete_table('registrazioni_servizi')

        # Deleting model 'RegistrazioniServiziTag'
        db.delete_table('registrazioni_servizi_tag')

        # Deleting model 'RegistrazioniTag'
        db.delete_table('registrazioni_tag')

        # Deleting model 'Settori'
        db.delete_table('settori')

        # Deleting model 'SettoriTags'
        db.delete_table('settori_tags')

        # Deleting model 'Stopwords'
        db.delete_table('stopwords')

        # Deleting model 'TagLegami'
        db.delete_table('tag_legami')

        # Deleting model 'TagMaxLegame'
        db.delete_table('tag_max_legame')

        # Deleting model 'TagOccorrenze'
        db.delete_table('tag_occorrenze')

        # Deleting model 'Tags'
        db.delete_table('tags')

        # Deleting model 'Video'
        db.delete_table('video')

        # Deleting model 'VideoTagOccorrenze'
        db.delete_table('video_tag_occorrenze')

        # Deleting model 'VideoTagOccorrenzeComuni'
        db.delete_table('video_tag_occorrenze_comuni')

        # Deleting model 'VideoTagOccorrenzeProvince'
        db.delete_table('video_tag_occorrenze_province')

        # Deleting model 'VideoTagOccorrenzeRegioni'
        db.delete_table('video_tag_occorrenze_regioni')

        # Deleting model 'VideoTags'
        db.delete_table('video_tags')


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
            'codregione': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'codRegione'"}),
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