# Generated by Django 3.2.7 on 2021-11-14 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0009_alter_exam_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'ordering': ['name'], 'verbose_name_plural': 'Exams'},
        ),
    ]
