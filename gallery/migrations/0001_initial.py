# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Galeria'
        db.create_table(u'gallery_galeria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'gallery', ['Galeria'])

        # Adding model 'Foto'
        db.create_table(u'gallery_foto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('galeria', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fotos', to=orm['gallery.Galeria'])),
            ('foto', self.gf('versatileimagefield.fields.VersatileImageField')(max_length=100)),
        ))
        db.send_create_signal(u'gallery', ['Foto'])


    def backwards(self, orm):
        # Deleting model 'Galeria'
        db.delete_table(u'gallery_galeria')

        # Deleting model 'Foto'
        db.delete_table(u'gallery_foto')


    models = {
        u'gallery.foto': {
            'Meta': {'object_name': 'Foto'},
            'foto': ('versatileimagefield.fields.VersatileImageField', [], {'max_length': '100'}),
            'galeria': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fotos'", 'to': u"orm['gallery.Galeria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'gallery.galeria': {
            'Meta': {'object_name': 'Galeria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['gallery']