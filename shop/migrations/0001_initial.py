# Generated by Django 4.1 on 2022-09-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Remera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('talle', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('lisa', models.BooleanField()),
                ('genero', models.IntegerField()),
            ],
        ),
    ]
