# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Azienda'
        db.create_table('aziende', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['Azienda'])

        # Adding M2M table for field tags on 'Azienda'
        m2m_table_name = db.shorten_name('aziende_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('azienda', models.ForeignKey(orm[u'frontend.azienda'], null=False)),
            ('tag', models.ForeignKey(orm[u'frontend.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['azienda_id', 'tag_id'])

        # Adding model 'Prodotto'
        db.create_table('prodotti', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('azienda', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='prodotti', null=True, to=orm['frontend.Azienda'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['Prodotto'])

        # Adding model 'Tag'
        db.create_table('tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
        ))
        db.send_create_signal(u'frontend', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'Azienda'
        db.delete_table('aziende')

        # Removing M2M table for field tags on 'Azienda'
        db.delete_table(db.shorten_name('aziende_tags'))

        # Deleting model 'Prodotto'
        db.delete_table('prodotti')

        # Deleting model 'Tag'
        db.delete_table('tags')


    models = {
        u'frontend.azienda': {
            'Meta': {'object_name': 'Azienda', 'db_table': "'aziende'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['frontend.Tag']", 'symmetrical': 'False'})
        },
        u'frontend.prodotto': {
            'Meta': {'object_name': 'Prodotto', 'db_table': "'prodotti'"},
            'azienda': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'prodotti'", 'null': 'True', 'to': u"orm['frontend.Azienda']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'frontend.tag': {
            'Meta': {'object_name': 'Tag', 'db_table': "'tags'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['frontend']