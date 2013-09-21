# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Crew'
        db.create_table(u'shipmates_crew', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('arrived', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'shipmates', ['Crew'])


    def backwards(self, orm):
        # Deleting model 'Crew'
        db.delete_table(u'shipmates_crew')


    models = {
        u'shipmates.crew': {
            'Meta': {'object_name': 'Crew'},
            'arrived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'shipmates.player': {
            'Meta': {'object_name': 'Player'},
            'arrived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'ticketholder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipmates.TicketHolder']"})
        },
        u'shipmates.ticketholder': {
            'Meta': {'object_name': 'TicketHolder'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'checked_in': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'order_type': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'tickettype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipmates.TicketType']"})
        },
        u'shipmates.tickettype': {
            'Meta': {'object_name': 'TicketType'},
            'eb_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['shipmates']