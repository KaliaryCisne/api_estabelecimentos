# Generated by Django 2.2.3 on 2019-07-14 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua_numero', models.CharField(blank=True, max_length=150, null=True)),
                ('bairro', models.CharField(max_length=150)),
                ('cidade', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=150)),
                ('pais', models.CharField(max_length=150)),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitude', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
