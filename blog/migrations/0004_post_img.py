# Generated by Django 3.2.25 on 2024-07-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='blog/default.jpg', upload_to='blog/'),
        ),
    ]
