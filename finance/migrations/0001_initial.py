# Generated by Django 5.0.6 on 2024-05-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Nome')),
                ('price', models.FloatField(verbose_name='Valor')),
                ('due_date', models.DateField(verbose_name='Vencimento')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Nome')),
                ('doc', models.IntegerField(verbose_name='CPF')),
                ('income', models.FloatField(verbose_name='Renda')),
            ],
        ),
    ]
