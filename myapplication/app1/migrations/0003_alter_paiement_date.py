# Generated by Django 3.2.6 on 2021-08-28 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_paiement_mode_paiement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
