# Generated by Django 3.2.6 on 2021-09-08 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0010_alter_fornecedor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='celular',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='telefone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
