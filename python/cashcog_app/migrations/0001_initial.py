# Generated by Django 3.0.1 on 2019-12-25 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField()),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField()),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('currency', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashcog_app.Employee')),
            ],
        ),
    ]
