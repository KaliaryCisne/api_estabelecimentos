# Generated by Django 2.2.3 on 2019-07-14 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0005_estabelecimento_avaliacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='estabelecimento',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enderecos.Endereco'),
            preserve_default=False,
        ),
    ]
