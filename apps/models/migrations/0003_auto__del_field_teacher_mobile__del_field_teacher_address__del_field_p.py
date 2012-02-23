# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Teacher.mobile'
        db.delete_column('models_teacher', 'mobile')

        # Deleting field 'Teacher.address'
        db.delete_column('models_teacher', 'address')

        # Deleting field 'Parent.mobile'
        db.delete_column('models_parent', 'mobile')

        # Deleting field 'Parent.address'
        db.delete_column('models_parent', 'address')

        # Adding field 'TeacherProfile.email'
        db.add_column('models_teacherprofile', 'email', self.gf('django.db.models.fields.EmailField')(default='', max_length=40, blank=True), keep_default=False)

        # Adding field 'TeacherProfile.mobile'
        db.add_column('models_teacherprofile', 'mobile', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'TeacherProfile.address'
        db.add_column('models_teacherprofile', 'address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Deleting field 'ParentProfile.parentsn'
        db.delete_column('models_parentprofile', 'parentsn_id')

        # Adding field 'ParentProfile.parents'
        db.add_column('models_parentprofile', 'parents', self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['models.Parent'], unique=True), keep_default=False)

        # Adding field 'ParentProfile.address'
        db.add_column('models_parentprofile', 'address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'ParentProfile.mobile'
        db.add_column('models_parentprofile', 'mobile', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Teacher.mobile'
        db.add_column('models_teacher', 'mobile', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True), keep_default=False)

        # Adding field 'Teacher.address'
        db.add_column('models_teacher', 'address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Parent.mobile'
        db.add_column('models_parent', 'mobile', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True), keep_default=False)

        # Adding field 'Parent.address'
        db.add_column('models_parent', 'address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Deleting field 'TeacherProfile.email'
        db.delete_column('models_teacherprofile', 'email')

        # Deleting field 'TeacherProfile.mobile'
        db.delete_column('models_teacherprofile', 'mobile')

        # Deleting field 'TeacherProfile.address'
        db.delete_column('models_teacherprofile', 'address')

        # User chose to not deal with backwards NULL issues for 'ParentProfile.parentsn'
        raise RuntimeError("Cannot reverse this migration. 'ParentProfile.parentsn' and its values cannot be restored.")

        # Deleting field 'ParentProfile.parents'
        db.delete_column('models_parentprofile', 'parents_id')

        # Deleting field 'ParentProfile.address'
        db.delete_column('models_parentprofile', 'address')

        # Deleting field 'ParentProfile.mobile'
        db.delete_column('models_parentprofile', 'mobile')


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
        'models.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'models.organization': {
            'Meta': {'object_name': 'Organization'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'models.parent': {
            'Meta': {'object_name': 'Parent'},
            'child': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['models.Student']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['models.School']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'models.parentprofile': {
            'Meta': {'object_name': 'ParentProfile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parents': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['models.Parent']", 'unique': 'True'})
        },
        'models.school': {
            'Meta': {'object_name': 'School'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['models.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'org': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['models.Organization']"})
        },
        'models.school_info': {
            'Meta': {'object_name': 'School_info'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parents_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'school': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['models.School']", 'unique': 'True'}),
            'students_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'teachers_number': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'models.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['models.School']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'models.studentprofile': {
            'Meta': {'object_name': 'StudentProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['models.Student']", 'unique': 'True'})
        },
        'models.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['models.School']"}),
            'user_id': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'models.teacherprofile': {
            'Meta': {'object_name': 'TeacherProfile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '40', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'teacher': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['models.Teacher']", 'unique': 'True'})
        },
        'models.temporary': {
            'Meta': {'object_name': 'Temporary'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['models.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pwd': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'role': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['models.School']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['models']
