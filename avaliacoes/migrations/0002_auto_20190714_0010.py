# Generated by Django 2.2.3 on 2019-07-14 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaliacao',
            old_name='user',
            new_name='usuario',
        ),
    ]
