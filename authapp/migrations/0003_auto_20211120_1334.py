# Generated by Django 3.2.8 on 2021-11-20 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_alter_shopuser_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='activate_key',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Ключ активации'),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activate_key_expired',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
