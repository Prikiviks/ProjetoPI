# Generated by Django 5.0.2 on 2024-07-30 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_pagamento_valor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagamento',
            options={'ordering': ['-data_pagamento'], 'verbose_name': 'Pagamento', 'verbose_name_plural': 'Pagamentos'},
        ),
    ]
