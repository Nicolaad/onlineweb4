# Generated by Django 2.1.11 on 2019-11-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20190506_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privacy',
            name='visible_as_attending_events',
            field=models.BooleanField(default=False, verbose_name='vis på påmeldingsarrangement'),
        ),
    ]
