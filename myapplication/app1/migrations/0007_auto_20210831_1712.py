# Generated by Django 3.2.6 on 2021-08-31 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_budget_annee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='annee',
        ),
        migrations.AlterField(
            model_name='budget',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
