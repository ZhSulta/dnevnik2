# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'City'
        db.create_table('models_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('models', ['City'])

        # Adding model 'Organization'
        db.create_table('models_organization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('models', ['Organization'])

        # Adding model 'School'
        db.create_table('models_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['models.City'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('org', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['models.Organization'])),
        ))
        db.send_create_signal('models', ['School'])

        # Adding model 'School_info'
        db.create_table('models_school_info', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['models.School'], unique=True)),
            ('teachers_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('students_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('parents_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('models', ['School_info'])

        # Adding model 'Student'
        db.create_table('models_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['models.School'])),
        ))
        db.send_create_signal('models', ['Student'])

        # Adding model 'StudentProfile'
        db.create_table('models_studentprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['models.Student'], unique=True)),
        ))
        db.send_create_signal('models', ['StudentProfile'])

        # Adding model 'Teacher'
        db.create_table('models_teacher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['models.School'])),
        ))
        db.send_create_signal('models', ['Teacher'])

        # Adding model 'TeacherProfile'
        db.create_table('models_teacherprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teacher', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['models.Teacher'], unique=True)),
            ('birth', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('models', ['TeacherProfile'])

        # Adding model 'Parent'
        db.create_table('models_parent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['models.School'])),
            ('child', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['models.Student'], unique=True)),
        ))
        db.send_create_signal('models', ['Parent'])

        # Adding model 'ParentProfile'
        db.create_table('models_parentprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parentsn', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['models.Parent'], unique=True)),
        ))
        db.send_create_signal('models', ['ParentProfile'])

        # Adding model 'Temporary'
        db.create_table('models_temporary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('pwd', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('school', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['models.School'], unique=True)),
            ('city', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['models.City'], unique=True)),
            ('role', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('models', ['Temporary'])


    def backwards(self, orm):
        
        # Deleting model 'City'
        db.delete_table('models_city')

        # Deleting model 'Organization'
        db.delete_table('models_organization')

        # Deleting model 'School'
        db.delete_table('models_school')

        # Deleting model 'School_info'
        db.delete_table('models_school_info')

        # Deleting model 'Student'
        db.delete_table('models_student')

        # Deleting model 'StudentProfile'
        db.delete_table('models_studentprofile')

        # Deleting model 'Teacher'
        db.delete_table('models_teacher')

        # Deleting model 'TeacherProfile'
        db.delete_table('models_teacherprofile')

        # Deleting model 'Parent'
        db.delete_table('models_parent')

        # Deleting model 'ParentProfile'
        db.delete_table('models_parentprofile')

        # Deleting model 'Temporary'
        db.delete_table('models_temporary')


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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'child': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['models.Student']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['models.School']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'models.parentprofile': {
            'Meta': {'object_name': 'ParentProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parentsn': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['models.Parent']", 'unique': 'True'})
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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['models.School']"}),
            'user_id': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'models.teacherprofile': {
            'Meta': {'object_name': 'TeacherProfile'},
            'birth': ('django.db.models.fields.DateField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'teacher': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['models.Teacher']", 'unique': 'True'})
        },
        'models.temporary': {
            'Meta': {'object_name': 'Temporary'},
            'city': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['models.City']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pwd': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'role': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'school': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['models.School']", 'unique': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['models']
