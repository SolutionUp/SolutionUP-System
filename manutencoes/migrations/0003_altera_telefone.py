# Generated by Django 3.2.6 on 2021-10-14 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manutencoes', '0002_manutencao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terceiro',
            name='telefone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]