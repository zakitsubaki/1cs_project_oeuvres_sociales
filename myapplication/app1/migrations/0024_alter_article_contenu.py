# Generated by Django 3.2.6 on 2021-09-07 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_auto_20210907_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='contenu',
            field=models.TextField(),
        ),
    ]