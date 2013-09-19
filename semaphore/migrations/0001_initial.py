# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'semaphore_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('short', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'semaphore', ['Contact'])

        # Adding model 'Message'
        db.create_table(u'semaphore_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['semaphore.Contact'])),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'semaphore', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'semaphore_contact')

        # Deleting model 'Message'
        db.delete_table(u'semaphore_message')


    models = {
        u'semaphore.contact': {
            'Meta': {'object_name': 'Contact'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        u'semaphore.message': {
            'Meta': {'object_name': 'Message'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['semaphore.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['semaphore']