# Generated by Django 2.2 on 2019-04-04 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wags_to_wings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='toy', max_length=30),
        ),
    ]
