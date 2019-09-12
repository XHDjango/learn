# Generated by Django 2.2.4 on 2019-09-12 14:43

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('learn_view', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogMDModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', mdeditor.fields.MDTextField()),
            ],
        ),
    ]
