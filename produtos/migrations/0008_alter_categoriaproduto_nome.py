# Generated by Django 3.2.6 on 2021-09-03 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0007_produto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriaproduto',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
