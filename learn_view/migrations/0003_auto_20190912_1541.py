# Generated by Django 2.2.4 on 2019-09-12 15:41

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('learn_view', '0002_blogmdmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmdmodel',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterField(
            model_name='blogmdmodel',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='blogmdmodel',
            name='title',
            field=models.CharField(max_length=128, verbose_name='标题'),
        ),
    ]