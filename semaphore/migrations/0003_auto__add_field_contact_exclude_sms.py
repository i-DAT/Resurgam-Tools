# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Contact.exclude_sms'
        db.add_column(u'semaphore_contact', 'exclude_sms',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Contact.exclude_sms'
        db.delete_column(u'semaphore_contact', 'exclude_sms')


    models = {
        u'semaphore.contact': {
            'Meta': {'object_name': 'Contact'},
            'exclude_sms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        u'semaphore.message': {
            'Meta': {'object_name': 'Message'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['semaphore.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recieved': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['semaphore']