# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 03:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Product categories',
                'db_table': 'categories',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Counter',
                'db_table': 'counters',
                'verbose_name_plural': 'Counters',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('address', models.TextField(max_length=1000)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Location',
                'db_table': 'locaitons',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('rate', models.FloatField(default=0.0)),
                ('rate_order', models.IntegerField(default=1)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Tax',
                'db_table': 'taxes',
                'verbose_name_plural': 'Taxes',
            },
        ),
        migrations.CreateModel(
            name='TaxCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Tax categories',
                'db_table': 'tax_categories',
                'verbose_name_plural': 'Tax Categories',
            },
        ),
        migrations.AddField(
            model_name='tax',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category', to='inventory.TaxCategory'),
        ),
        migrations.AddField(
            model_name='counter',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='location', to='inventory.Location'),
        ),
    ]
