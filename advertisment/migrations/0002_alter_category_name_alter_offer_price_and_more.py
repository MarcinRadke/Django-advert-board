# Generated by Django 4.0.3 on 2022-04-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='offer',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='offer',
            name='title',
            field=models.TextField(max_length=20),
        ),
    ]
