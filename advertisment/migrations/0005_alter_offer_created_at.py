# Generated by Django 4.0.3 on 2022-04-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisment', '0004_offer_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
