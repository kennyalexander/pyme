# Generated by Django 4.1.3 on 2022-11-14 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='urlimage',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
