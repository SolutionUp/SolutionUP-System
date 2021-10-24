# Generated by Django 3.2.6 on 2021-10-24 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0005_reestrutura_pedido_produto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comissaopedido',
            name='percentual_comissao',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='percentual_comissao',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='funcionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vendas.funcionario'),
        ),
    ]
