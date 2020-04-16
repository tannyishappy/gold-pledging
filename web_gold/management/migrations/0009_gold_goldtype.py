# Generated by Django 3.0.4 on 2020-04-16 18:24

from django.db import migrations
import django_enumfield.db.fields
import management.models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_auto_20200415_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='gold',
            name='goldtype',
            field=django_enumfield.db.fields.EnumField(default=0, enum=management.models.GoldType),
        ),
    ]
