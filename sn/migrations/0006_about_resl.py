# Generated by Django 5.1.4 on 2025-01-07 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sn', '0005_home_fav'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='resl',
            field=models.URLField(default='https://drive.google.com/file/d/1zcba3G7v706wHnIUsJtunsIUPb8arb-_/view'),
        ),
    ]
