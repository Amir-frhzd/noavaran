# Generated by Django 3.2.25 on 2024-07-20 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='no phone', max_length=11),
            preserve_default=False,
        ),
    ]
