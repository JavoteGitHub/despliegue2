# Generated by Django 3.1.1 on 2020-10-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TejidoMama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partP', models.IntegerField()),
                ('temperatura', models.FloatField()),
                ('color', models.FloatField()),
                ('inflamacion', models.FloatField()),
            ],
        ),
    ]
