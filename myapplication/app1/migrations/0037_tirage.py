# Generated by Django 3.2.6 on 2021-09-11 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0036_rename_announce_inscription_annonce'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tirage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admis', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('annonce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.annonce')),
            ],
        ),
    ]