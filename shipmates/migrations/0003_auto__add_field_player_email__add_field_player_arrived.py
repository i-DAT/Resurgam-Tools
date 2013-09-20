# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Player.email'
        db.add_column(u'shipmates_player', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Player.arrived'
        db.add_column(u'shipmates_player', 'arrived',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Player.email'
        db.delete_column(u'shipmates_player', 'email')

        # Deleting field 'Player.arrived'
        db.delete_column(u'shipmates_player', 'arrived')


    models = {
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