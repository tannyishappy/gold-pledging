# Generated by Django 3.0.4 on 2020-04-14 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_enumfield.db.fields
import management.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('citizen_id', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pledging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pledge_balanca', models.IntegerField()),
                ('contract_term', models.IntegerField()),
                ('pledge_date', models.DateField(auto_now_add=True)),
                ('expire_date', models.DateField()),
                ('type_pledging', django_enumfield.db.fields.EnumField(default=1, enum=management.models.PledgingType)),
                ('cus_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Customer')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Redeemed',
            fields=[
                ('pledging_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='management.Pledging')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('citizen_id', models.CharField(max_length=13)),
                ('redeem_date', models.DateField(auto_now_add=True)),
            ],
            bases=('management.pledging',),
        ),
        migrations.CreateModel(
            name='Gold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('pledging_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Pledging')),
            ],
        ),
    ]