# Generated by Django 4.0.3 on 2022-04-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisment', '0002_alter_category_name_alter_offer_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='offer',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
